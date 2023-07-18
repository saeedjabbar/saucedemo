#importing time module
import time

# importing selenium webdriver and By class
from selenium import webdriver
from selenium.webdriver.common.by import By

#setting up chrome driver
driver = webdriver.Chrome()

#opening the website
driver.get("https://www.saucedemo.com/")

#find username field and enter username
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

#find password field and enter password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

#find login button and click
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

#wait for 3 seconds
time.sleep(3)

#check if login was successful with basic logging
if driver.current_url == "https://www.saucedemo.com/inventory.html":
    print("Login successful!")
else:
    print("Login failed!")

# Close browser
driver.quit()
