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

t=4

class base_test(unittest.TestCase):

    def setUp(self):
       #Webdriver para Chrome
       self.driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://demoqa.com/automation-practice-form",t)

        f.texto_mixto("xpath","//input[contains(@id,'firstName')]","Daniel",t)

        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
        action.send_keys(Keys.TAB)
        action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).send_keys("@gmail.com").perform()
        time.sleep(2)



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
