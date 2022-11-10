import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class base_test(unittest.TestCase):

    def setUp(self):
       #Webdriver para Chrome
       self.driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")

    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        driver.maximize_window()
        time.sleep(2)


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
