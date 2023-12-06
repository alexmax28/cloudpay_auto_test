# 引入
from appium import webdriver
from appium.webdriver.common.appiumby import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyotp
import yaml

def get_data():
    f = open("data.yaml",encoding="utf8")
    data = yaml.safe_load(f)
    print(data)
    return data

def user_login(d,vesion):
    
    # 點選立即體驗
    now = WebDriverWait(d, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwallet:id/item_tv"))
    )
    now.click()
    
    if vesion > 7:
        # 允許存取
        allow_button_1 = WebDriverWait(d, 10).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
        allow_button_1.click()
        time.sleep(1)
        allow_button_2 = WebDriverWait(d, 10).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
        allow_button_2.click()
        time.sleep(1)
    else:
        # 允許存取
        allow_button_1 = WebDriverWait(d, 10).until(
            EC.presence_of_element_located(
                (By.ID, "com.android.packageinstaller:id/permission_allow_button"))
        )
        allow_button_1.click()
        time.sleep(2)
        allow_button_1.click()


        

    # # 輸入手機
    # input_phone = WebDriverWait(d, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwallet:id/login_et_username"))
    # )
    # input_phone.send_keys("18177777777")
    # time.sleep(1)

    # # 輸入密碼
    # input_password = WebDriverWait(d, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwallet:id/login_et_code"))
    # )
    # input_password.send_keys("123456")
    # time.sleep(1)

    # # 登入
    # click_login_btn = WebDriverWait(d, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwallet:id/login_tv_login"))
    # )
    # click_login_btn.click()
    # time.sleep(1)

def trader_login(t):
    # 點選立即體驗
    t_now = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/item_tv"))
    )
    t_now.click()
    time.sleep(1)

    # 允許存取
    allow_button_1 = WebDriverWait(t, 10).until(
        EC.presence_of_element_located(
            (By.ID, "com.android.packageinstaller:id/permission_allow_button"))
    )
    allow_button_1.click()
    time.sleep(1)
    allow_button_1.click()
    time.sleep(1)
    # allow_button_1 = WebDriverWait(t, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
    # )
    # allow_button_1.click()
    # time.sleep(1)
    # allow_button_2 = WebDriverWait(t, 10).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.android.permissioncontroller:id/permission_allow_button"))
    # )
    # allow_button_2.click()
    # time.sleep(1)
# android 9
    # t_allow_button_1 = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.android.packageinstaller:id/permission_allow_button"))
    # )
    # time.sleep(1)
    # t_allow_button_1.click()
    # time.sleep(1)
    # t_allow_button_1.click()

    # # 輸入手機
    # t_input_phone = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/login_et_username"))
    # )
    # t_input_phone.send_keys("18199999999")
    # time.sleep(1)

    # # 輸入密碼
    # t_input_password = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/login_et_code"))
    # )
    # t_input_password.send_keys("111111")
    # time.sleep(1)

    # # 登入
    # t_click_login_btn = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/login_tv_login"))
    # )
    # t_click_login_btn.click()
    # time.sleep(1)

    # # google驗證碼

    # totp = pyotp.TOTP('v5wtd3fdxzedrdgy6hb5ab2b')
    # true_goolge_password = totp.now()
    # print(f"google驗證碼: {true_goolge_password}")

    # t_input_google_code = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/dialog_etCode"))
    # )
    # t_input_google_code.send_keys(f"{true_goolge_password}")
    # time.sleep(1)

    # # google驗證碼click
    # t_click_google_code_submit = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/dialog_tvSure"))
    # )
    # t_click_google_code_submit.click()
    # time.sleep(1)

    # # 入款 switch
    # t_click_sell_switch = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/home_iv_closeOrOpen"))
    # )
    # t_click_sell_switch.click()
    # time.sleep(1)

    # # 檢查開關
    # t_alert_text = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "/hierarchy/android.widget.Toast"))
    # )
    # print(t_alert_text.text)
    # # time.sleep(1)

    # if t_alert_text.text != "开启成功":
    #     t_click_sell_switch.click()


    # # 出款 tab
    # t_click_buy_btn = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView"))
    # )
    # t_click_buy_btn.click()
    # time.sleep(1)

    # # 出款 switch
    # t_click_buy_switch = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.ID, "com.tg.cloudwalletvip:id/home_iv_closeOrOpen"))
    # )
    # t_click_buy_switch.click()
    # time.sleep(1)

    # # 檢查開關
    # t_alert_text = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "/hierarchy/android.widget.Toast"))
    # )
    # print(t_alert_text.text)
    # # time.sleep(1)

    # if t_alert_text.text != "开启成功":
    #     t_click_buy_switch.click()
        

    # # 入款 tab
    # t_click_sell_btn = WebDriverWait(t, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView"))
    # )
    # t_click_sell_btn.click()
    # time.sleep(1)
