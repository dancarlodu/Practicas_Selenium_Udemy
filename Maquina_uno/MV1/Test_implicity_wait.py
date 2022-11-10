import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Webdriver para Chrome
driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")


driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(15)

t=1
time.sleep(t)

nom = driver.find_element(By.XPATH,"//input[@id='userName']")
nom.send_keys("Daniel")
time.sleep(t)

driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("hectordc@audifarma.com.co")
time.sleep(t)

driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Dirección 1")
time.sleep(t)

driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Dirección 2")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)


driver.close()