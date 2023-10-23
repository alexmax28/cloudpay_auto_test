# 引入
from appium import webdriver
from appium.webdriver.common.appiumby import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyotp
import android_fn as fn


# # # ========================================= user 登入

# # 连接手机app初始化的一些信息
# desc = {}
# desc['deviceName'] = 'emulator-5554'  # 手机设备名称，adb devices，模擬器
# desc['platformVersion'] = '11'  # 手机版本，在手机中：设置--关于手机
# desc['platformName'] = 'Android'  # 手机类型，ios或android
# desc['appPackage'] = 'com.tg.cloudwallet'  # 包名
# desc['appActivity'] = 'com.tg.cloudwallet.ui.activity.WelcomeActivity'  # 启动入口

# d = webdriver.Remote('127.0.0.1:4722/wd/hub', desc) #appium server

# # 偵測螢幕解析度
# x = d.get_window_size()["width"]
# y = d.get_window_size()["height"]
# print(f'width:{x}')
# print(f'height:{y}')
# time.sleep(2)
# # 滑動螢幕
# x1 = int(x*0.8)
# y1 = int(y*0.5)
# x2 = int(x*0.1)
# y2 = int(y*0.5)
# d.swipe(x1, y1, x2, y2)

# fn.user_login(d)

# # # ==================================================== trader 登入

# 连接手机app初始化的一些信息
tesc = {}
tesc['deviceName'] = '1bb1c275'  # 手机设备名称，adb devices，模擬器
tesc['platformVersion'] = '9'  # 手机版本，在手机中：设置--关于手机
tesc['platformName'] = 'Android'  # 手机类型，ios或android
tesc['appPackage'] = 'com.tg.cloudwalletvip'  # 包名
tesc['appActivity'] = 'com.tg.cloudwalletvip.ui.activity.WelcomeActivity'  # 启动入口

t = webdriver.Remote('127.0.0.1:4723/wd/hub', tesc) #appium server



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

# # ========================================= user 充值

# # 找出充直常駐
# recharg_lists = d.find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
# time.sleep(1)

# recharg_name = d.find_elements(By.ID,"com.tg.cloudwallet:id/saleItem_tv_name")
# time.sleep(1)

# for i,recharg_item in enumerate(recharg_lists):
#     if recharg_name[i].text == "alex常駐":
#         print(recharg_name[i].text)

#         print(i+1)

#         click_recharg_name_btn = WebDriverWait(d, 5).until(
#             EC.presence_of_element_located(
#                 (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{i+1}]/android.widget.LinearLayout/android.widget.LinearLayout[1]"))
#         )
#         click_recharg_name_btn.click()
#         break
        
# time.sleep(1)

# # 輸入充值金額
# input_recharg_amount = WebDriverWait(d, 10).until(
#     EC.presence_of_element_located(
#         (By.ID, "com.tg.cloudwallet:id/pop_etAmount"))
# )
# input_recharg_amount.send_keys(100)
# time.sleep(1)

# # 確認下單
# recharg_order_true = WebDriverWait(d, 10).until(
#     EC.presence_of_element_located(
#         (By.ID, "com.tg.cloudwallet:id/pop_tvSure"))
# )
# recharg_order_true.click()
# time.sleep(1)

# # 我已付款
# recharg_payment_sure = WebDriverWait(d, 10).until(
#     EC.presence_of_element_located(
#         (By.ID, "com.tg.cloudwallet:id/payment_tv_sure"))
# )
# recharg_payment_sure.click()
# time.sleep(1)

# # 重要提示_我已付款
# alert_recharg_payment_sure = WebDriverWait(d, 10).until(
#     EC.presence_of_element_located(
#         (By.ID, "com.tg.cloudwallet:id/dialog_tvStop"))
# )
# alert_recharg_payment_sure.click()
# time.sleep(1)



# # ========================================= trader 確認充值
# trader入款清單找出用戶

recharg_user_lists = t.find_elements(By.CLASS_NAME,"android.widget.LinearLayout")
time.sleep(1)

recharg_user_names = t.find_elements(By.ID,"com.tg.cloudwalletvip:id/item_tvName")
time.sleep(1)


for n,recharg_user_item in enumerate(recharg_user_lists):
    
    if recharg_user_names[n].text == "18177777":
        print(recharg_user_names[n].text)

        print(n+1)
        click_recharg_user_name_btn = WebDriverWait(t, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[{n+1}]"))
        )
        click_recharg_user_name_btn.click()
        break        
time.sleep(1)


# 確認到賬
check_recharg_arrival_btn = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/confirm_tv_sure"))
    )
check_recharg_arrival_btn.click()
time.sleep(1)

# 重要提示_確認到賬
alert_check_recharg_arrival_btn = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/dialog_tvStop"))
    )
alert_check_recharg_arrival_btn.click()

# 訂單完成
trader_order_complete = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/toolBar_title"))
    )

trader_order_no = WebDriverWait(t, 5).until(
        EC.presence_of_element_located(
            (By.ID, "com.tg.cloudwalletvip:id/complete_tv_orderNum"))
    )
print(f"常駐:{trader_order_complete.text}")
print(f"訂單編號:{trader_order_no.text}")

time.sleep(10)





# time.sleep(30)

#關閉app
# d.close_app()
time.sleep(3)
t.close_app()
