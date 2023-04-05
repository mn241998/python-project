import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
class testcase_001:
    def loginopencart(username,password):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://demo.opencart.com/")
        driver.find_element(By.LINK_TEXT,"My Account").click()
        driver.find_element(By.LINK_TEXT,"Login").click()
        time.sleep(2)

        if driver.title=="Your Store":
            print("title is matched")
        else:
            print("title is  not matched")

        print(driver.title)
        driver.find_element(By.ID,"input-email").send_keys("username")
        driver.find_element(By.ID,"input-password").send_keys("password")
        driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
    loginopencart("abc@gmail.com","12345678")

