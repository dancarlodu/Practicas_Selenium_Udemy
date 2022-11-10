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
        f.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",t)

        f.texto_mixto("xpath", "//input[contains(@name,'username')]", "Admin", t)
        f.texto_mixto("xpath", "//input[contains(@name,'password')]", "admin123", t)
        f.click_mixto("xpath","//button[contains(@type,'submit')]", t)


        #f.click_mixto("xpath","//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]",t)

        admin= driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][contains(.,'Admin')]")



        action = ActionChains(driver)
        action.move_to_element(admin).click().perform()
        time.sleep(3)

        sub1 = driver.find_element(By.XPATH,
                                   "//span[@class='oxd-topbar-body-nav-tab-item'][contains(.,'User Management')]")
        action.move_to_element(sub1).click().perform()

        time.sleep(3)
        sub2 = driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Users')]")
        action.move_to_element(sub2).click().perform()

        time.sleep(3)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
