import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Webdriver para Chrome
driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
t=2

#dias = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'select-demo')]")))
diaSelect= driver.find_element(By.XPATH, "//select[contains(@id,'select-demo')]")

ds = Select(diaSelect)

ds.select_by_visible_text("Sunday")
time.sleep(t)

ds.select_by_index(3)
time.sleep(t)

ds.select_by_value("Saturday")
time.sleep(t)

ciudad = Select(driver.find_element(By.ID, "multi-select"))

ciudad.select_by_index(1)
time.sleep(t)
ciudad.select_by_index(2)
time.sleep(t)
ciudad.select_by_index(3)
time.sleep(t)

driver.close()