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
fn.input_google_code(t,true_goolge_password)
time.sleep(1)
fn.click_google_secret_login_btn(t)
time.sleep(1)
fn.open_sell_switch(t)
time.sleep(1)
fn.buy_btn(t)
time.sleep(1)
fn.open_buy_switch(t)
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


# ============================================================ user 充值 
fn.recharge_btn(u)
# 充值在線常駐總數
recharge_list_count = fn.recharge_list_count(u)
print(f"充值在線常駐總數: {recharge_list_count}")

# 選擇常駐用戶交易 transaction_trader
try:
    recharge_traders = u.find_elements(By.CLASS_NAME,"box__name")
    for recharge_trader in recharge_traders:
        text_content = recharge_trader.text
        if text_content == transaction_trader:
            recharge_trader.click()
            print("Text content:", text_content)
except:
    print(f"常駐用戶: {transaction_trader} 沒有上線")
time.sleep(1)

# 與常駐用戶交易下單
fn.input_click_recharg_order_money(u,recharg_order_money)





# ============================================================ trader 選擇訂單 
fn.trader_select_order(t,user_id)
# ============================================================ trader 確認到帳 

fn.trader_click_confirm_arrival_btn(t)





time.sleep(30)
# d.close()
