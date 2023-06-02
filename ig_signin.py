from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Specify the path to your web driver executable
driver_path = "/Users/erict/Desktop/api_testing/webdriver/chromedriver_mac64/chromedriver"
expected_url = "https://www.instagram.com/accounts/onetap/?next=%2F"
username = "grabangoo"
password = "Gakct1868"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(driver_path)

# Open Instagram
driver.get("https://www.instagram.com/")

try:
    # Find the username and password input fields
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    # Enter your username and password
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form
    password_field.submit()

    time.sleep(10)
    # Wait until the user is logged in
    WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/accounts/activity/']"))
        EC.url_to_be(expected_url)
    )

    # Successful login
    print("Login successful!")

except Exception as e:
    # Handle sign-in error
    print("Error occurred during login:", e)

finally:
    driver.save_screenshot("snapshot_result.png")
    # Close the browser
    driver.quit()
