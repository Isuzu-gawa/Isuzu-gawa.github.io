import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# https://stackoverflow.com/questions/65638246/dismiss-wants-to-know-your-location-dialog

prefs = {
        'googlegeolocationaccess.enabled': True,
        'profile.default_content_setting_values.geolocation':1,
        'profile.default_content_setting_values.notifications':1,
        'profile.managed_default_content_settings':1
    }

options = Options()
# options.add_argument("--start-maximized")
options.headless = True
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
# options.add_argument('--incognito')  # これ入れると毎回位置情報の許可を求められるダルい
options.add_argument('--enable-geolocation')  # 意味ない?
options.add_experimental_option('prefs', prefs)  # なんか全く役に立ってないような?

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

url = "https://isuzu-gawa.github.io/getlocation/gps-json.html" 

driver.get(url)

# 位置情報の許可を求めるメッセージはアラート扱いではないらしい
"""
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except TimeoutException:
    print("アラートは発生しませんでした")
except Exception as e:
    print(e)
"""
time.sleep(5)

print(driver.find_element(By.ID, "resdiv").text)

var = input("続けるにはエンターキーを押してください : ")


driver.quit()