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
t=0.3

@pytest.fixture(scope="module")
def setup_login():
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.texto_mixto("xpath", "//input[@name='username']", "Admin", t)
    f.texto_mixto("xpath", "//input[@name='password']", "admin123", t)
    f.click_mixto("xpath", "//button[@type='submit']", t)
    print("Entrando al sistema")


def teardown_function():
    print("Fin de todos los test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_login")
def test_uno():
    etiqueta=f.SEX("//p[@class='oxd-userdropdown-name'][contains(.,'Paul Collings')]").text
    print(etiqueta)
    '''
    if(etiqueta=="Paul Colling"):
        print("#############################\n")
        print("Estas en la página de inicio")
        print("#############################\n")
        assert etiqueta == "Paul Colling"
    else:
        assert etiqueta=="Paul Collings", "No pudiste entrar al sistema"
    '''
    assert etiqueta == "Paul Collings", "No pudiste entrar al sistema"