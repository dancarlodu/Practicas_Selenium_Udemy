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

def test_login():
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    fl=Funciones_Login(driver)
    fl.L1("Daniel@gmail.com", "1234", "No customer account found")


def test_login1():
    global driver
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f=Funciones_Globales(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    driver.maximize_window()

    f.texto_mixto("id","Email","cardonal.daniel@gmail.com",t)
    f.texto_mixto("id","Password","1234", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]",t)
    error1 = f.SEX("//li[contains(.,'No customer account found')]")
    error1=error1.text
    print(error1)
    if(error1=="No customer account found"):
        print("Prueba de validación exitosa")
    else:
        print("La prueba de validación es incorrecta")
    driver.close()

def test_login2():
    global driver
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f=Funciones_Globales(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    driver.maximize_window()

    f.texto_mixto("id","Email","",t)
    f.texto_mixto("id","Password","1234", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]",t)
    error1 = f.SEX("//span[contains(@id,'Email-error')]")
    error1=error1.text
    print(error1)
    if(error1=="Please enter your email"):
        print("Prueba de Email vacio existosa")
    else:
        print("La prueba de Email vacío es incorrecta")

    driver.close()

def test_login3():
    global driver
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f=Funciones_Globales(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    driver.maximize_window()

    f.texto_mixto("id","Email","Daniel",t)
    f.texto_mixto("id","Password","1234", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]",t)
    error1 = f.SEX("//span[contains(@id,'Email-error')]")
    error1=error1.text
    print(error1)
    if(error1=="Wrong email"):
        print("Email no valido. existosa")
    else:
        print("Pruebas de email no exitosa")

    driver.close()

def test_login4():
    global driver
    driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
    f=Funciones_Globales(driver)
    f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F",t)
    driver.maximize_window()

    f.texto_mixto("id","Email","admin@yourstore.com",t)
    f.texto_mixto("id","Password","admin", t)
    f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]",t)
    error1 = f.SEX("//h1[contains(.,'Dashboard')]")
    error1=error1.text
    print(error1)
    if(error1=="Dashboard"):
        print("Loguin Exitoso")
    else:
        print("No se puede loguear")

    driver.close()