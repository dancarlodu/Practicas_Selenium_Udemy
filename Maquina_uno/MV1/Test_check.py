import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Webdriver para Chrome
driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='isAgeSelected']")))
btn1.click()


btn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Option 2']//input[@type='checkbox']")))
btn3.click()

btn4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Option 3']//input[@type='checkbox']")))
btn4.click()

driver.execute_script("window.scrollTo(0,300)")

time.sleep(t)


driver.close()