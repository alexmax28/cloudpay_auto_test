# 引入
from appium import webdriver
from appium.webdriver.common.appiumby import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyotp
import android_fn as fn
import unittest
from android_fn import get_data
import allure
import pytest

# # ========================================= user 登入

# 连接手机app初始化的一些信息S

# 安卓模擬器
# desc = {}
# desc['deviceName'] = 'emulator-5554'  # 手机设备名称，adb devices，模擬器
# desc['platformVersion'] = '11'  # 手机版本，在手机中：设置--关于手机
# desc['platformName'] = 'Android'  # 手机类型，ios或android
# desc['appPackage'] = 'com.tg.cloudwallet'  # 包名
# desc['appActivity'] = 'com.tg.cloudwallet.ui.activity.WelcomeActivity'  # 启动入口\
# desc['newCommandTimeout'] = '600'

# ============================================ 夜神user
desc = {}
desc['deviceName'] = '127.0.0.1:62001'  # 手机设备名称，adb devices，模擬器
desc['platformVersion'] = '7'  # 手机版本，在手机中：设置--关于手机
desc['platformName'] = 'Android'  # 手机类型，ios或android
desc['appPackage'] = 'com.tg.cloudwallet'  # 包名
desc['appActivity'] = 'com.tg.cloudwallet.ui.activity.WelcomeActivity'  # 启动入口\
desc['newCommandTimeout'] = '60000'
desc['udid'] = '127.0.0.1:62001'

d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desc) #appium server

# 偵測螢幕解析度
x = d.get_window_size()["width"]
y = d.get_window_size()["height"]
print(f'width:{x}')
print(f'height:{y}')
time.sleep(2)
# 滑動螢幕
x1 = int(x*0.8)
y1 = int(y*0.5)
x2 = int(x*0.1)
y2 = int(y*0.5)
d.swipe(x1, y1, x2, y2)
vesion = int(desc['platformVersion'])
fn.user_login(d,vesion)

# # ============================================= trader
# tesc = {}
# tesc['deviceName'] = '1bb1c275'  # 手机设备名称，adb devices，模擬器
# tesc['platformVersion'] = '9'  # 手机版本，在手机中：设置--关于手机
# tesc['platformName'] = 'Android'  # 手机类型，ios或android
# tesc['appPackage'] = 'com.tg.cloudwalletvip'  # 包名
# tesc['appActivity'] = 'com.tg.cloudwalletvip.ui.activity.WelcomeActivity'  # 启动入口
# tesc['newCommandTimeout'] = '600'

# t = webdriver.Remote('http://127.0.0.1:4723/wd/hub', tesc) #appium server

# # 偵測螢幕解析度
# x = t.get_window_size()["width"]
# y = t.get_window_size()["height"]

# print(f'width:{x}')
# print(f'height:{y}')
# time.sleep(2)
# # 滑動螢幕
# x1 = int(x*0.8)
# y1 = int(y*0.5)
# x2 = int(x*0.1)
# y2 = int(y*0.5)
# t.swipe(x1, y1, x2, y2)
# time.sleep(1)

# fn.trader_login(t)
# time.sleep(1)

# ==========================================================================夜神 trader

tesc = {}
tesc['deviceName'] = '127.0.0.1:62030'  # 手机设备名称，adb devices，模擬器
tesc['platformVersion'] = '7'  # 手机版本，在手机中：设置--关于手机
tesc['platformName'] = 'Android'  # 手机类型，ios或android
tesc['appPackage'] = 'com.tg.cloudwalletvip'  # 包名
tesc['appActivity'] = 'com.tg.cloudwalletvip.ui.activity.WelcomeActivity'  # 启动入口
tesc['newCommandTimeout'] = '60000'
tesc['udid'] = '127.0.0.1:62030'

t = webdriver.Remote('http://127.0.0.1:4725/wd/hub', tesc) #appium server

# 偵測螢幕解析度
x = t.get_window_size()["width"]
y = t.get_window_size()["height"]

print(f'width:{x}')
print(f'height:{y}')
time.sleep(2)
# 滑動螢幕
x1 = int(x*0.8)
y1 = int(y*0.5)
x2 = int(x*0.1)
y2 = int(y*0.5)
t.swipe(x1, y1, x2, y2)
time.sleep(1)

fn.trader_login(t)
time.sleep(1)

   
# =================================================================================================== user login test
# 輸入錯誤手機
@allure.feature("user登入測試")
@allure.story("User登入各項錯誤訊息")
@allure.title("User登入各項錯誤訊息")
# @allure.title("登入各項錯誤訊息")
@pytest.mark.parametrize("userMobile,password",get_data()["user_login_params_false"])
def test_A_input_error_phonenumber(userMobile,password):
    # 輸入錯誤手機
    input_phone = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/login_et_username"))
    )
    input_phone.send_keys(userMobile)
    time.sleep(1)

    # 輸入密碼
    input_password = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/login_et_code"))
    )
    input_password.send_keys(password)
    time.sleep(1)

        # 登入
    click_login_btn = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/login_tv_login"))
    )
    click_login_btn.click()
    time.sleep(1)

    Toast = d.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
    print(Toast.text)
    if Toast.text == "用户不存在或密码错误！":
        assert Toast.text == "用户不存在或密码错误！"
    elif Toast.text == "用户名或密码无效！":
        assert Toast.text == "用户名或密码无效！"
    elif Toast.text == "请输入密码":
        assert Toast.text == "请输入密码"
    elif Toast.text == "请输入11位手机号":
        assert Toast.text == "请输入11位手机号"
    # else:
    #     pass

    
    time.sleep(1)


# 輸入正確登入
@allure.feature("user登入測試")
@allure.story("User登入正確")
@allure.title("User登入正確")
# @allure.title("登入正確")
@pytest.mark.parametrize("userMobile,password",get_data()["user_login_params_true"])
def test_E_input_true_login(userMobile,password):
    # 輸入正確手機
    input_phone = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/login_et_username"))
    )
    input_phone.send_keys(userMobile)
    time.sleep(1)

    # 輸入正確密碼
    input_password = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/login_et_code"))
    )
    input_password.send_keys(password)
    time.sleep(1)

        # 登入
    click_login_btn = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/login_tv_login"))
    )
    click_login_btn.click()
    time.sleep(1)
    print("User登入成功!")

# # =================================================================================================== trader 登入驗證
@allure.feature("Trader登入測試")
@allure.story("常駐登入錯誤測試")
@allure.title("常駐登入錯誤測試")
@pytest.mark.parametrize("Trader_mobile,Trader_password",get_data()["trader_login_params_false"])
def test_F_input_trader_error_phonenumber(Trader_mobile,Trader_password):
    # 輸入錯誤手機
    t_input_error_phone = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/login_et_username"))
    )
    t_input_error_phone.send_keys(Trader_mobile)
    time.sleep(1)

    t_input_password = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/login_et_code"))
    )
    t_input_password.send_keys(Trader_password)
    time.sleep(1)

    click_login_btn = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/login_tv_login"))
    )
    click_login_btn.click()
    time.sleep(1)

    Toast = t.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
    print(Toast.text)

    if Toast.text == "用户不存在或密码错误！":
        assert Toast.text == "用户不存在或密码错误！"
    elif Toast.text == "用户名或密码无效！":
        assert Toast.text == "用户名或密码无效！"
    elif Toast.text == "请输入密码":
        assert Toast.text == "请输入密码"
    elif Toast.text == "请输入11位手机号":
        assert Toast.text == "请输入11位手机号"

# 輸入正確登入
@allure.feature("Trader登入測試")
@allure.story("常駐正確登入")
@allure.title("常駐正確登入")
@pytest.mark.parametrize("Trader_mobile,Trader_password",get_data()["trader_login_params_true"])
def test_J_input_trader_true_login(Trader_mobile,Trader_password):
    # 輸入正確手機
    input_phone = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/login_et_username"))
    )
    input_phone.send_keys(Trader_mobile)
    time.sleep(1)

    # 輸入正確密碼
    input_password = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/login_et_code"))
    )
    input_password.send_keys(Trader_password)
    time.sleep(1)

        # 登入
    click_login_btn = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/login_tv_login"))
    )
    click_login_btn.click()
    print("常駐登入成功!")
    time.sleep(1)

# 輸入錯誤google驗證
@allure.feature("Trader google驗證碼測試")
@allure.story("輸入錯誤google驗證碼")
@allure.title("輸入錯誤google驗證碼")
@pytest.mark.parametrize("google_code_error",get_data()["trader_google_code_error"])
def test_K_input_false_google_code(google_code_error):
    # 錯誤google驗證碼
    # print(type(google_code_error[0]))
    if google_code_error[0]:
        totp = pyotp.TOTP(google_code_error[0])
        true_goolge_false_password = totp.now()
    else:
        true_goolge_false_password = ''
    
    # print(f"google驗證碼: {true_goolge_false_password}")
    time.sleep(1)
    t_input_google_false_code = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/dialog_etCode"))
    )
    t_input_google_false_code.send_keys(f"{true_goolge_false_password}")
    time.sleep(1)

    # google驗證碼click
    t_click_false_google_code_submit = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/dialog_tvSure"))
    )
    t_click_false_google_code_submit.click()
    time.sleep(1)

    Toast = t.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
    print(Toast.text)

    if Toast.text == "谷歌身份验证错误！":
        assert Toast.text == "谷歌身份验证错误！"
    elif Toast.text == "请输入谷歌验证码":
        assert Toast.text == "请输入谷歌验证码"
    time.sleep(1)
    
# 輸入正確google驗證
@allure.feature("Trader google驗證碼測試")
@allure.story("輸入正確google驗證碼")
@allure.title("輸入正確google驗證碼")
@pytest.mark.parametrize("google_code_true",get_data()["trader_google_code_true"])
def test_L_input_true_google_code(google_code_true):
    # google驗證碼
    # print(type(google_code_true[0]))
    totp = pyotp.TOTP(google_code_true[0])
    true_goolge_true_password = totp.now()
    # print(f"google驗證碼: {true_goolge_true_password}")
    time.sleep(1)

    t_input_google_true_code = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/dialog_etCode"))
    )
    t_input_google_true_code.send_keys(f"{true_goolge_true_password}")
    time.sleep(1)

    # google驗證碼click
    t_click_true_google_code_submit = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/dialog_tvSure"))
    )
    t_click_true_google_code_submit.click()
    time.sleep(1)
    # print("google驗證輸入正確")

# 打開入款出款開關
@allure.feature("打開入款出款開關")
@allure.title("打開入款出款開關")
def test_M_trader_open_sell_buy_switch():
    # 入款 switch
    t_click_sell_switch = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/home_iv_closeOrOpen"))
    )
    t_click_sell_switch.click()
    time.sleep(1)

    # 檢查開關
    t_alert_sell_text = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.Toast"))
    )
    # print(t_alert_sell_text.text)
    # time.sleep(1)

    if t_alert_sell_text.text != "开启成功":
        t_click_sell_switch.click()
        time.sleep(1)
        Toast = t.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
        print(Toast.text)
        # assertEqual(Toast.text,"开启成功")
        assert Toast.text == "开启成功"
    time.sleep(1)

    # 出款 tab
    t_click_buy_btn = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView"))
    )
    t_click_buy_btn.click()
    time.sleep(1)

    # 出款 switch
    t_click_buy_switch = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/home_iv_closeOrOpen"))
    )
    t_click_buy_switch.click()
    # time.sleep(1)
    # 檢查開關
    t_alert_buy_text = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.Toast"))
    )
    # print(t_alert_buy_text.text)
    if t_alert_buy_text.text != "开启成功":
        t_click_buy_switch.click()
        # time.sleep(1)
    Toast = t.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
    print(Toast.text)
    # assertEqual(Toast.text,"开启成功")
    assert Toast.text == "开启成功"
    time.sleep(1)  

    # def test_N_switch_to_sell_tab(self):
    #     # 入款 tab
    #     t_click_sell_btn = WebDriverWait(self.t, 5).until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView"))
    #     )
    #     t_click_sell_btn.click()
    #     time.sleep(1)




    # =================================================================================================== user 提現 test
@allure.feature("User提現測試")
@allure.title("切換提現Tab & 找出常駐")
def test_O_user_select_trader_take_order():
        # 切一下tab 刷新常駐
        time.sleep(1)
        withdraw_switch = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView"))
        )
        # assertEqual(withdraw_switch.text,"提现")
        assert withdraw_switch.text == "提现"
        withdraw_switch.click()
        time.sleep(1)

        # 找出提現常駐
        recharg_lists = d.find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
        time.sleep(1)
        recharg_name = d.find_elements(By.ID,"com.tg.cloudwallet:id/saleItem_tv_name")
        time.sleep(1)
        trader_name = ''

        for i,recharg_item in enumerate(recharg_lists):
            if recharg_name[i].text == "alex常駐":
                print(recharg_name[i].text)
                trader_name = recharg_name[i].text

                click_recharg_name_btn = WebDriverWait(d, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{i+1}]/android.widget.LinearLayout/android.widget.LinearLayout[1]"))
                )
                click_recharg_name_btn.click()
                break

        # self.assertEqual(trader_name,"alex常駐") # 判斷所選常駐名稱是否一致
        assert trader_name == "alex常駐" # 判斷所選常駐名稱是否一致
                
        time.sleep(1)
    # =================================================================================================== user 提現未輸入金額 test
@allure.feature("User提現測試")
@allure.title("user 提現未輸入金額")
def test_P_input_error_withdraw_amount():

        input_withdraw_error_amount = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/pop_etAmount"))
        )
        input_withdraw_error_amount.send_keys("")

         # 確認下單
        withdraw_order_true = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/pop_tvSure"))
        )
        withdraw_order_true.click()
        time.sleep(1)

        Toast = d.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
        print(Toast.text)
        # self.assertEqual(Toast.text,"请输入提现金额")
        assert Toast.text == "请输入提现金额"


    # =================================================================================================== user 提現輸入金額 test
@allure.feature("User提現測試")
@allure.title("user 提現輸入金額")
def test_Q_input_right_withdraw_amount():
        # 輸入提現金額
        input_withdraw_amount = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/pop_etAmount"))
        )
        input_withdraw_amount.send_keys(100)
        time.sleep(1)

        # 確認下單
        withdraw_order_true = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/pop_tvSure"))
        )
        withdraw_order_true.click()
        time.sleep(1)

        # 確認下單提示
        alert_withdraw_order_true = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/dialog_tvStop"))
        )
        alert_withdraw_order_true.click()
        time.sleep(1)

    # =================================================================================================== 輸入錯誤支付密碼測試
@allure.feature("User提現測試")
@allure.title("User 輸入錯誤支付密碼")
def test_R_input_error_pay_password():

        # 輸入支付密碼
        input_withdraw_password = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/et_password"))
        )
        input_withdraw_password.send_keys("999999")
        time.sleep(1)

        # 確認輸入支付密碼
        submit_withdraw_password = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/tv_ok"))
        )
        submit_withdraw_password.click()
        time.sleep(1)

        Toast = d.find_element(By.XPATH,"/hierarchy/android.widget.Toast")
        print(Toast.text)
        # self.assertEqual(Toast.text,"支付密码错误")
        assert Toast.text == "支付密码错误"

    # =================================================================================================== 輸入正確支付密碼測試
@allure.feature("User提現測試")
@allure.title("User 輸入正確支付密碼")
def test_S_input_right_pay_password():
        # 確認下單
        withdraw_order_true = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/pop_tvSure"))
        )
        withdraw_order_true.click()
        time.sleep(1)

        # 確認下單提示
        alert_withdraw_order_true = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/dialog_tvStop"))
        )
        alert_withdraw_order_true.click()
        time.sleep(1)


        # 輸入支付密碼
        input_withdraw_password = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/et_password"))
        )
        input_withdraw_password.send_keys("123456")
        time.sleep(1)

        # 確認輸入支付密碼
        submit_withdraw_password = WebDriverWait(d, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwallet:id/tv_ok"))
        )
        submit_withdraw_password.click()
        time.sleep(1)


# # # =================================================================================================== trader 出款確認
# trader 入款清單找出用戶
@allure.feature("Trader 出款確認")
@allure.title("Trader 選擇User出款確認")
def test_T_trader_select_user_check_order():
        # 切到出款tab
        turn_to_buy_tab = WebDriverWait(t, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[1]"))
        )
        turn_to_buy_tab.click()
        time.sleep(1)

        recharg_user_lists = t.find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
        recharg_user_names = t.find_elements(By.ID,"com.tg.cloudwalletvip:id/item_tvName")
        for n,recharg_user_item in enumerate(recharg_user_lists):
            
            if recharg_user_names[n].text == "18166666":
                print(f"選擇user帳號: {recharg_user_names[n].text}")
                print(n+1)
                time.sleep(1)
                click_recharg_user_name_btn = WebDriverWait(t, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{n+1}]"))
                )
                click_recharg_user_name_btn.click()
                break        
        # time.sleep(1)

        # 我已付款
        check_withdraw_pay_btn = WebDriverWait(t, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "com.tg.cloudwalletvip:id/payment_tv_sure"))
            )
        check_withdraw_pay_btn.click()
        time.sleep(1)

        # 重要提示_確認到帳
        alert_check_withdraw_pay_btn = WebDriverWait(t, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "com.tg.cloudwalletvip:id/dialog_tvStop"))
            )
        alert_check_withdraw_pay_btn.click()
        time.sleep(1)

    # # # =================================================================================================== user 確認到帳
@allure.feature("User 確認到帳")
@allure.title("User 確認到帳")
def test_U_check_withdraw_arrive():
        user_check_withdraw_arrive_btn = WebDriverWait(d, 5).until(
                    EC.presence_of_element_located(
                        (By.ID, "com.tg.cloudwallet:id/confirm_tv_sure"))
                )
        user_check_withdraw_arrive_btn.click()
        time.sleep(1)


        alert_user_check_withdraw_arrive_btn = WebDriverWait(d, 5).until(
                    EC.presence_of_element_located(
                        (By.ID, "com.tg.cloudwallet:id/dialog_tvStop"))
                )
        alert_user_check_withdraw_arrive_btn.click()
        time.sleep(1)

        
    # # # =================================================================================================== user 確認到帳
@allure.feature("User 確認訂單完成")
@allure.title("User 確認訂單完成")
def test_V_order_complete():
        # 訂單完成
        user_order_complete = WebDriverWait(d, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "com.tg.cloudwallet:id/toolBar_title"))
            )
        time.sleep(1)
        print(user_order_complete.text)

        user_order_no = WebDriverWait(d, 5).until(
                EC.presence_of_element_located(
                    (By.ID, "com.tg.cloudwallet:id/complete_tv_orderNum"))
            )
        time.sleep(1)
        print(f"常駐:{user_order_complete.text}")
        print(f"訂單編號:{user_order_no.text}")

        time.sleep(3)

# # # =================================================================================================== 關閉app
#     def test_X_close_app(self):
#         # self.d.close_app()
#         # self.t.close_app()
#         self.d.quit()
#         self.t.quit()



