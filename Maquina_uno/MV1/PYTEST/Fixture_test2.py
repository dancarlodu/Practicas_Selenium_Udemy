import time
import pytest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones import Funciones_Globales
from Page_Login import Funciones_Login

t=1
driver = ""
f = ""

def setup_function(function):
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.texto_mixto("id", "Email", "admin@yourstore.com", t)
    f.texto_mixto("id", "Password", "admin", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Iniciando nuestro test")


def teardown_function(function):
    print("Fin de los test")
    driver.close()

def test_uno():
    f.click_mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.click_mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.texto_mixto("xpath", "//input[contains(@id,'SearchProductName')]", "computer", t)
    f.click_mixto("xpath", "//button[@id='search-products']", t)

def test_dos():
    f = Funciones_Globales(driver)
    f.click_mixto("xpath", "//a[@href='#'][contains(.,'Catalog')]", t)
    f.click_mixto("xpath", "(//p[contains(.,'Products')])[1]", t)
    f.click_mixto("xpath", "//a[@href='/Admin/Product/Create']",t)
    f.texto_mixto("xpath","//input[@id='Name']","Laptop Dell", t)
    f.texto_mixto("xpath","//textarea[contains(@id,'ShortDescription')]","Computador portatil", t)
    f.click_mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]", t)
    f.click_mixto("xpath", "//div[@class='tox-collection__item-label'][contains(.,'New document')]", t)
    driver.switch_to.frame(0)
    f.texto_mixto("id","tinymce","descripción larga", t)
    driver.switch_to.default_content()
    f.texto_mixto("xpath","//input[contains(@id,'Sku')]","124565",t)



