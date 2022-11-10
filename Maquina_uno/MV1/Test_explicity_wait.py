import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Webdriver para Chrome
driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()
#driver.implicitly_wait(10)
t=0.5

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
except:
    pass

driver.find_element(By.XPATH, "//input[@id='user-message']").send_keys("Bienvenidos a Selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.find_element(By.XPATH, "//input[@id='sum1']").send_keys("5" + Keys.TAB + "5" + Keys.TAB + Keys.ENTER)
time.sleep(t)


driver.close()