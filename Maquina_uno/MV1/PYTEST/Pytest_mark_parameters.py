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
t=0.5

def get_Data():
    return [
        ("rodrigo", "1234"),
        ("juan", "xsd21"),
        ("pedro", "4512"),
        ("daniel", "d52"),
        ("marcela", "1234"),
        ("Admin", "admin123")
    ]

@pytest.mark.login
@pytest.mark.parametrize("user,clave",get_Data())
def test_login(user, clave):
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f = Funciones_Globales(driver)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.texto_mixto("xpath", "//input[@name='username']", user, t)
    f.texto_mixto("xpath", "//input[@name='password']", clave, t)
    f.click_mixto("xpath", "//button[@type='submit']", t)
    print("Entrando al sistema")

def teardown_function(functioin):
    print("Salida del test")
    driver.close()

