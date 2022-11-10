import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import Funciones_Globales

class Pagina_login():

    def __init__(self, driver):
        self.driver = driver

    def login_master(self,url, name, clave, t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar(url, t)
        f.texto_Xpath_Validar("//input[contains(@id,'user-name')]", name, t)
        f.texto_Xpath_Validar("//input[contains(@id,'password')]", clave, t)
        f.click_Xpath_Validar("//input[contains(@id,'login-button')]", t)





