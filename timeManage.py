import configparser

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


time.sleep(25)

driver.quit()