import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones import Funciones_Globales


class Funciones_Login():

    def __init__(self, driver):
        self.driver = driver

    def L1(self, email, clave, mensaje, t=0.1):
        driver = webdriver.Chrome(executable_path="C:\DriversAutomation\chromedriver.exe")
        f = Funciones_Globales(driver)
        f.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        driver.maximize_window()

        f.texto_mixto("id", "Email", email, t)
        f.texto_mixto("id", "Password", clave, t)
        f.click_mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        error1 = f.SEX("//li[contains(.,'No customer account found')]")
        error1 = error1.text
        print("Mensaje: "+ error1)
        if (error1 == mensaje):
            print("Prueba de validación exitosa")
        else:
            print("La prueba de validación es incorrecta")

        driver.close()