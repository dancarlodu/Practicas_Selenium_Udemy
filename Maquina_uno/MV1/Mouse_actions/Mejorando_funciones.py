import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..Funciones.Funciones import Funciones_Globales
from selenium.webdriver.common.action_chains import ActionChains

t=2

class base_test(unittest.TestCase):

    def setUp(self):
       #Webdriver para Chrome
       self.driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://www.saucedemo.com/",t)

        '''
        f.texto_mixto("xpath", "//input[@id='user-name']", "Admin", t)
        f.texto_mixto("xpath", "//input[@id='password']", "admin123", t)
        f.click_mixto("xpath","//input[@id='login-button']", t)
        '''

        f.texto_mixto("id", "user-name", "Admin", t)
        f.texto_mixto("id", "password", "admin123", t)
        f.click_mixto("id", "login-button", t)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
