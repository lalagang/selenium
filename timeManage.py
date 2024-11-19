import configparser
from datetime import date

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# ログイン情報読み込み
inifile = configparser.ConfigParser()
inifile.read(r'D:\config.ini', 'UTF-8')

# webdriver
chrome_driver_path  = webdriver.Chrome()

# WebDriverを初期化
driver = webdriver.Chrome()

# urlにアクセス
url = 'https://p.ieyasu.co/careritzit/login'
driver.get(url)

# ログイン情報入力
driver.find_element('id','user_login_id').send_keys(inifile.get('user', 'name'))
driver.find_element('id','user_password').send_keys(inifile.get('user', 'password'))
driver.find_element('name','Submit').click()

# 勤怠画面遷移
driver.find_element('id','work_navi').click()

# TODO:日付を特定する
day = date.today()
b = driver.find_element('xpath','/html/body/div[1]/div[2]/div/div/div/form/div[1]/table[2]/tbody/tr[2]/td[1]/span[1]').get_attribute("textContent")
# /html/body/div[1]/div[2]/div/div/div/form/div[1]/table[2]/tbody/tr[2]/td[1]/span[1]
print(b)

# TODO:特定した日の鉛筆マークをクリック
driver.find_element('id','work_edit_514400').click()

# 業務時間入力
driver.find_element('id','work_start_at_str').send_keys('8:30')
driver.find_element('id','work_end_at_str').send_keys('17:45')
driver.find_element('name','commit').click()


time.sleep(25)

driver.quit()