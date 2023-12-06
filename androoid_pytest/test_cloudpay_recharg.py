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
@allure.feature("google驗證碼測試")
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
@allure.feature("google驗證碼測試")
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
    
@allure.title("切換到入款tab")
def test_N_switch_to_sell_tab():
    # 入款 tab
    t_click_sell_btn = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView"))
    )
    t_click_sell_btn.click()
    time.sleep(1)




# =================================================================================================== user 充值 test
@allure.title("user充值測試")
def test_O_user_select_trader_take_order():
    # 切一下tab 刷新常駐
    time.sleep(1)
    buy_switch = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView"))
    )
    # self.assertEqual(buy_switch.text,"提现")
    assert buy_switch.text == "提现"
    buy_switch.click()
    print("提现")
    time.sleep(1)
    sell_switch = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView"))
    )
    sell_switch.click()
    print("充值")
    time.sleep(1)

    # 找出充直常駐
    recharg_lists = d.find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
    time.sleep(1)
    recharg_name = d.find_elements(By.ID,"com.tg.cloudwallet:id/saleItem_tv_name")
    time.sleep(1)
    trader_name = ''

    for i,recharg_item in enumerate(recharg_lists):
        if recharg_name[i].text == "alex常駐":
            print(recharg_name[i].text)

            # print(i+1)

            trader_name = recharg_name[i].text

            click_recharg_name_btn = WebDriverWait(d, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{i+1}]/android.widget.LinearLayout/android.widget.LinearLayout[1]"))
            )
            click_recharg_name_btn.click()
            break

    # self.assertEqual(trader_name,"alex常駐") # 判斷所選常駐名稱是否一致
    assert trader_name == "alex常駐"
            
    # time.sleep(1)

    # 輸入充值金額
    input_recharg_amount = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/pop_etAmount"))
    )
    input_recharg_amount.send_keys(100)
    time.sleep(1)

    # 確認下單
    recharg_order_true = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/pop_tvSure"))
    )
    recharg_order_true.click()
    time.sleep(1)

    # 我已付款
    recharg_payment_sure = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/payment_tv_sure"))
    )
    recharg_payment_sure.click()
    time.sleep(1)

    # 重要提示_我已付款
    alert_recharg_payment_sure = WebDriverWait(d, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/dialog_tvStop"))
    )
    alert_recharg_payment_sure.click()
    time.sleep(1)


# # =================================================================================================== trader 確認到帳
# trader 入款清單找出用戶
@allure.title("常駐確認到帳測試")
def test_P_trader_select_user_check_order():
    recharg_user_lists = t.find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
    time.sleep(1)
    recharg_user_names = t.find_elements(By.ID,"com.tg.cloudwalletvip:id/item_tvName")
    time.sleep(1)
    for n,recharg_user_item in enumerate(recharg_user_lists):
        
        if recharg_user_names[n].text == "18166666":
            print(recharg_user_names[n].text)
            print(n+1)
            # time.sleep(1)
            click_recharg_user_name_btn = WebDriverWait(t, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{n+1}]"))
            )
            click_recharg_user_name_btn.click()
            break        
    # time.sleep(1)

    # 確認到帳
    check_recharg_arrival_btn = WebDriverWait(t, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwalletvip:id/confirm_tv_sure"))
        )
    check_recharg_arrival_btn.click()
    time.sleep(1)

    # 重要提示_確認到帳
    alert_check_recharg_arrival_btn = WebDriverWait(t, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwalletvip:id/dialog_tvStop"))
        )
    alert_check_recharg_arrival_btn.click()
    time.sleep(1)

    # 訂單完成
    trader_order_complete = WebDriverWait(t, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwalletvip:id/toolBar_title"))
        )
    time.sleep(1)

    trader_order_no = WebDriverWait(t, 5).until(
            EC.presence_of_element_located(
                (By.ID, "com.tg.cloudwalletvip:id/complete_tv_orderNum"))
        )
    time.sleep(1)
    print(f"常駐:{trader_order_complete.text}")
    print(f"訂單編號:{trader_order_no.text}")

    time.sleep(3)

# # # =================================================================================================== 關閉app
# def test_Q_close_app(self):
#     # self.d.close_app()
#     # self.t.close_app()
#     self.d.quit()
#     # self.t.quit()

# =================================================================================================== user 確認充值完成

# 驗證訂單完成
@allure.title("订单完成測試")
def test_compelete_order():
    compelete_order = d.find_element(By.CLASS_NAME,"android.widget.TextView")
    # self.assertEqual(compelete_order,"订单完成")
    assert compelete_order.text == "订单完成"
    print("订单完成")



# def test_find_battery(self):
#     el = self.d.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView")
#     el.click()



