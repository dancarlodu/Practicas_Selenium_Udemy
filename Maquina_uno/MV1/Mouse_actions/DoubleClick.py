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
        f.navegar("https://demoqa.com/buttons",t)

        '''
        elemento = driver.find_element(By.ID, "doubleClickBtn")
        action = ActionChains(driver)
        action.double_click(elemento).perform()
        '''
        #f.mouse_doble("id","doubleClickBtn",t)
        f.mouse_doble("xpath", "//button[@id='doubleClickBtn']")
        time.sleep(t)





    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
