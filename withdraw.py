from datetime import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
# from webdriver_manager.chrome import ChromeDriverManager
# import spay_fn as sf
import string
# import test_slack_bot as bot
import configparser
import fn
import pyotp
import os
from dotenv import load_dotenv
load_dotenv()

user_id = os.getenv("ENV_USER_ID")


# PATH = r"/home/alex/python/spay/chromedriver"
# PATH = "./chromedriver.exe"


option = webdriver.ChromeOptions()
# # option.add_argument('headless')
# option.add_argument('no-sandbox')
# option.add_argument('disable-dev-shm-usage')


# ============================================================ trader 登入開啟充值提現開關
t = webdriver.Chrome()
t.get('http://cloudpay.traderwebportal.tyche/#/login')

# ===================================== trader google驗證
totp = pyotp.TOTP('v5wtd3fdxzedrdgy6hb5ab2b')
true_goolge_password = totp.now()
print(f"google驗證碼: {true_goolge_password}")

t_phone = os.getenv("ENV_TRADER_PHONE")
t_password = os.getenv("ENV_TRADER_PASSWORD")

fn.input_trader_number(t,t_phone)
time.sleep(1)
fn.input_trader_password(t,t_password)
time.sleep(1)
fn.click_login_btn(t)
time.sleep(1)
fn.input_google_code(t,true_goolge_password) # 輸入google驗證
time.sleep(1)
fn.click_google_secret_login_btn(t)
time.sleep(1)
fn.open_sell_switch(t) # 開啟入款按鈕
time.sleep(1)
fn.buy_btn(t)
time.sleep(1)
fn.open_buy_switch(t) # 開啟出款按鈕
fn.sell_btn(t)
time.sleep(1)

# ============================================================ user 登入 
u = webdriver.Chrome()
u.get('http://cloudpay.userwebportal.tyche/#/login')
phone = os.getenv("ENV_USER_PHONE")
password = os.getenv("ENV_USER_PASSWORD")
transaction_trader = os.getenv("ENV_TRANSACTION_TRADER")
recharg_order_money = os.getenv("ENV_RECHARG_ORDER_MONEY")

fn.input_number(u,phone)
time.sleep(1)
fn.input_password(u,password)
time.sleep(1)
fn.login_btn(u)
time.sleep(1)


# ============================================================ user 提現 
price = os.getenv("ENV_WITHDRAW_ORDER_MONEY") # 提現金額
withdraw_password = os.getenv("ENV_WITHDRAW_PASSWORD") # 提現安全密碼
fn.click_withdraw_btn(u)
time.sleep(1)
# 充值在線常駐總數

withdra_list_count = fn.withdraw_list_count(u)
print(f"提現在線常駐總數: {withdra_list_count}")

# 選擇常駐用戶交易 transaction_trader
try:
    recharge_traders = u.find_elements(By.CLASS_NAME,"box__name")
    for recharge_trader in recharge_traders:
        text_content = recharge_trader.text
        if text_content == transaction_trader:
            recharge_trader.click()
            # print("Text content:", text_content)
except:
    print(f"常駐用戶: {transaction_trader} 沒有上線")
time.sleep(1)

# ============================================================ 與常駐用戶交易下單
fn.input_click_withdraw_order_money(u,price,withdraw_password)



# ============================================================ trader 選擇訂單 
fn.move_withdraw_btn(t) # 切換到出款
time.sleep(1)
fn.trader_select_withdraw_order(t,user_id)

# ============================================================ trader 提現付款 
fn.trader_click_withdraw_btn(t)
time.sleep(1)
# ============================================================ user 確認提現到帳
fn.click_withdraw_arrival_btn(u)

time.sleep(30)

# ============================================================ 關閉瀏覽器
t.close()
u.close()



