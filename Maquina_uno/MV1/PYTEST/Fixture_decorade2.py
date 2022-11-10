import time

import allure
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
from allure_commons.types import AttachmentType

t=1

#Imagenes con error
@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope="module")
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f = Funciones_Globales(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
    driver.maximize_window()
    driver.implicitly_wait(20)
    f.texto_mixto("id", "Email", "admin@yourstore.com", t)
    f.texto_mixto("id", "Password", "admin", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Entrando al sistema")

    yield
    print("Salida del login uno")
    driver.close()


@pytest.fixture(scope="module")
def setup_login_dos():
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

    yield
    print("Salida del login dos")
    driver.close()

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando el sistema uno")
    f.click_mixto("xpath", "//a[@href='#'][contains(.,'Customers')]",t)
    f.click_mixto("xpath","(//p[contains(.,'Customers')])[2]", t)
    f.texto_mixto("xpath","//input[contains(@id,'SearchFirstName')]","victoria",t)
    allure.attach(driver.get_screenshot_as_png(), name="buscando_nombre", attachment_type=AttachmentType.PNG)
    f.click_mixto("xpath","//button[contains(@id,'search-customers')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="customers", attachment_type=AttachmentType.PNG)
    #creando un nuevo usuario
    f.click_mixto("xpath","//a[@href='/Admin/Customer/Create']",t)
    email=driver.find_element(By.XPATH,"//input[contains(@id,'Email')]")
    email.send_keys("cardona@gmail.com"+Keys.TAB+"12345"+Keys.TAB+"Juan"+Keys.TAB+"Perez")
    allure.attach(driver.get_screenshot_as_png(), name="customers", attachment_type=AttachmentType.PNG)
    f.click_mixto("xpath","//input[contains(@id,'Gender_Male')]",t)
    #f.click_mixto("xpath","//span[@class='k-icon k-i-calendar']",t)
    f.texto_mixto("xpath","//input[@id='DateOfBirth']","10/12/2022",t)
    assert 1 == 2
    time.sleep(2)

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando el sistema dos")
    f.click_mixto("xpath","//span[contains(.,'Admin')]",t)
    f.click_mixto("xpath","(//span[contains(.,'User Management')])[2]",t)
    allure.attach(driver.get_screenshot_as_png(), name="Menú_admin", attachment_type=AttachmentType.PNG)
    f.click_mixto("xpath","//a[@href='#'][contains(.,'Users')]",t)
    f.texto_mixto("xpath","(//input[@class='oxd-input oxd-input--active'])[2]", "Fiona.Grace", t)
    f.click_mixto("xpath","//button[@type='submit']", t)
    allure.attach(driver.get_screenshot_as_png(), name="buscando", attachment_type=AttachmentType.PNG)
    f.click_mixto("xpath","//button[contains(.,'Add')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="agregando", attachment_type=AttachmentType.PNG)
    assert 1==2
    time.sleep(3)