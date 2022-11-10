import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PruebaLogin(unittest.TestCase):

    def setUp(self):
        #Webdriver para Chrome
        self.driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

    def test_login1 (self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user=driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave=driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
        btn=driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        user.send_keys("Daniel")
        clave.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos ..")
            print("Prueba Uno OK")
        time.sleep(2)

    def test_login2 (self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user=driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave=driver.find_element(By.XPATH,"//input[contains(@id,'password')]")
        btn=driver.find_element(By.XPATH,"//input[contains(@id,'login-button')]")
        user.send_keys("")
        clave.send_keys("admin123")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if error == "Epic sadface: Username is required":
            print("Falta el usuario ..")
            print("Prueba Dos OK")
        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        user.send_keys("Daniel")
        clave.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        # print(error)
        if error == "Epic sadface: Password is required":
            print("Falta el password ..")
            print("Prueba Tres OK")
        time.sleep(2)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        user.send_keys("")
        clave.send_keys("")
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        # print(error)
        if error == "Epic sadface: Username is required":
            print("Falta usuario y password ..")
            print("Prueba cuatro OK")
        time.sleep(2)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        user = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        user.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        btn.click()
        elemento = driver.find_element(By.XPATH, "//div[contains(@class,'app_logo')]")
        validacion = elemento.is_displayed()
        if validacion:
            print("Ingreso correctamnete")
            print("Prueba cinco OK")

        time.sleep(2)



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
