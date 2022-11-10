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


@pytest.mark.validar_if
def test_validar_if():
    nom1 = "Rodrigo"
    nom2 = "Juan"

    if(nom1==nom2):
        print("el test paso")
    else:
        print("el test no paso")