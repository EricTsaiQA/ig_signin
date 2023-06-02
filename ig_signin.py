from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#定義用到參數
#driver path給定系統上chrome driver位置
driver_path = "xxxx/chromedriver_mac64/chromedriver"
#expected url 用來會驗證是否有登入成功
expected_url = "https://www.instagram.com/accounts/onetap/?next=%2F"
#username, password 可以在這邊輸入
username = "xxxx"
password = "xxxx"

#new一個webdriver物件
driver = webdriver.Chrome(driver_path)

#打開IG
driver.get("https://www.instagram.com/")

try:
    #確認在IG頁面找到username欄位
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    #輸入名稱跟密碼,密碼輸入完後送出
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.submit()
    
    #等待執行登入結果, 用url to be 驗證登入後url要是我們期待的
    time.sleep(10)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(expected_url)
    )

    #登入成功就打印訊息
    print("登入成功")

#登入沒成功就走except這條路
except Exception as e:
    print("登入發生錯誤 請檢查:", e)

finally:
    #截圖最後畫面
    driver.save_screenshot("snapshot_result.png")
    #結束webdriver物件
    driver.quit()
