from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
import time


# 登入===================================================================== user
# 登入
def input_number(d,phone):
    input_number = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/input')
        )
    )
    input_number.send_keys(phone)

def input_password(d,password):
    input_password = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/input')
        )
    )
    input_password.send_keys(password)


def login_btn(d):
    login_btn = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/button')
        )
    )
    login_btn.click()

# user 目錄
def menu_btn(d):
    menu_btn = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div[2]/div/img')
        )
    )
    menu_btn.click()
# ===================================================================== user 充值
# 充值
def recharge_btn(d):
    recharge_btn = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div[1]')
        )
    )
    recharge_btn.click()


# 充值list總數
def recharge_list_count(d):
    recharge_list_count = len(d.find_elements(By.CLASS_NAME,"box__name"))
    
    # print(f"充值在線常駐總數: {recharge_list_count}")
    return recharge_list_count



# 充值下單
def input_click_recharg_order_money(d,price):
    # 輸入充值金額
    input_recharg_order_money = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div/div[2]/div[3]/div/div[2]/input')
        )
    )
    input_recharg_order_money.send_keys(price)

    # 提交充值訂單
    click_recharg_order_btn = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div/div[2]/div[4]/div/div[2]')
        )
    )
    click_recharg_order_btn.click()
    
    # # 獲取訂單號
    # order_no = d.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[4]/div[6]/div[1]/span')
    # print(f"order_no: {order_no}")

    # 我已付款
    click_recharg_already_pay = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[4]')
        )
    )
    click_recharg_already_pay.click()

    # 我已付款 check
    click_recharg_already_pay_check = WebDriverWait(d,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[3]/div[2]')
        )
    )
    click_recharg_already_pay_check.click()

    # # 取消交易
    # click_recharg_cancel_the_deal = WebDriverWait(t,5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[3]')
    #     )
    # )
    # click_recharg_cancel_the_deal.click() 
    # # 立即取消
    # click_recharg_cancel_the_deal_now = WebDriverWait(t,5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH,'//*[@id="app"]/div/div[2]/div[5]')
    #     )
    # )
    # click_recharg_cancel_the_deal_now.click() 

# ===================================================================== user 提現
def click_withdraw_btn(u):
    click_withdraw_btn = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div[2]')
        )
    )
    click_withdraw_btn.click()

# 提現值list總數
def withdraw_list_count(u):
    withdraw_list_count = len(u.find_elements(By.CLASS_NAME,"box__name"))
    return withdraw_list_count

# 提現下單
def input_click_withdraw_order_money(u,price,withdraw_password):
    input_withdraw_order_money = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div/div[2]/div[3]/div/div[2]/input')
        )
    )
    input_withdraw_order_money.send_keys(price)
    time.sleep(1)
# 輸入安全密碼
    input_withdraw_order_password = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div/div[2]/div[3]/div/div[3]/input')
        )
    )
    input_withdraw_order_password.send_keys(withdraw_password)
# 提現下單
    click_withdraw_order = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div/div[2]/div[4]/div/div[2]')
        )
    )
    click_withdraw_order.click()
# 提現下單 again
    click_withdraw_order_again = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[6]/div/div[3]/div/div/div[3]/div[2]')
        )
    )
    click_withdraw_order_again.click()

# 用戶提現確認到帳
def click_withdraw_arrival_btn(u):
    click_withdraw_arrival_btn = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[2]/div[5]/div[3]/div[2]')
        )
    )
    click_withdraw_arrival_btn.click()

    click_withdraw_arrival_btn_again = WebDriverWait(u,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div[3]/div/div[3]/div[2]')
        )
    )
    click_withdraw_arrival_btn_again.click()





# ===================================================================== 常駐登入

def input_trader_number(t,phone):
    input_trader_number = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/input')
        )
    )
    input_trader_number.send_keys(phone)

def input_trader_password(t,password):
    input_trader_password = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/input')
        )
    )
    input_trader_password.send_keys(password)

def click_login_btn(t):
    click_login_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/button')
        )
    )
    click_login_btn.click()


def input_google_code(t,google_code):
    input_google_code = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[6]/div/div[2]/div[4]/input')
        )
    )
    input_google_code.send_keys(google_code)

def click_google_secret_login_btn(t):
    click_google_secret_login_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[6]/div/div[2]/button')
        )
    )
    click_google_secret_login_btn.click()



# 入款按鈕tab
def sell_btn(t):
    sell_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[1]/div[1]')
        )
    )
    sell_btn.click()

# 出款按鈕tab
def buy_btn(t):
    buy_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[1]/div[2]')
        )
    )
    buy_btn.click()
    
# 開啟入款
def open_sell_switch(t):
    # sell_switch = t.find_elements(By.CLASS_NAME, "home_content_footer_info trader_open_background")
    sell_switch = t.find_elements(By.CLASS_NAME, "trader_open_background")

    if len(sell_switch) > 0:
        print("入款已經打開!!")
    else:
        open_sell_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/img')
        )
        )
        open_sell_btn.click()
        print("入款開啟成功!!")

# 開啟出款
def open_buy_switch(t):
    buy_switch = t.find_elements(By.CLASS_NAME, "trader_open_background")

    if len(buy_switch) > 0:
        print("出款已經打開!!")
    else:
        open_buy_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/img')
        )
        )
        open_buy_btn.click()
        print("出款開啟成功!!")


# ===================================================================== 常駐確認充值訂單

# 常駐用戶選擇充值訂單
def trader_select_order(t,user_id):
    try:
        trader_orders = t.find_elements(By.CLASS_NAME,"home_recharge_item_row")
        for order in trader_orders:
            text_content = order.text
            # print(text_content)
            if user_id in text_content:
                order.click()
    except:
        print(f"沒有 {user_id} 用戶訂單")
    time.sleep(1)

# 常駐確認充值到帳
def trader_click_confirm_arrival_btn(t):
    trader_click_confirm_arrival_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[3]/div[3]')
        )
    )
    trader_click_confirm_arrival_btn.click()
    time.sleep(1)
# 常駐再次確認充值到帳
    trader_click_confirm_arrival_btn_again = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[4]/div/div[3]/div/button[2]')
        )
    )
    trader_click_confirm_arrival_btn_again.click()
    time.sleep(1)
    
# ===================================================================== 常駐確認提現訂單
# 切換到出款
def move_withdraw_btn(t):
    move_withdraw_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[1]/div[1]/div[2]')
        )
    )
    move_withdraw_btn.click()

# 常駐用戶選擇提現訂單
def trader_select_withdraw_order(t,user_id):
    try:
        trader_orders = t.find_elements(By.CLASS_NAME,"home_withdraw_item_row")
        for order in trader_orders:
            text_content = order.text
            # print(text_content)
            if user_id in text_content:
                order.click()
    except:
        print(f"沒有 {user_id} 用戶訂單")
    time.sleep(1)


# 常駐提現付款
def trader_click_withdraw_btn(t):
    trader_click_withdraw_btn = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[3]/div[3]')
        )
    )
    trader_click_withdraw_btn.click()
    time.sleep(1)
# 常駐再次確認提現付款
    trader_click_withdraw_btn_again = WebDriverWait(t,5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="app"]/div/div/div[4]/div/div[3]/div/button[2]')
        )
    )
    trader_click_withdraw_btn_again.click()
    time.sleep(1)
