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

@pytest.fixture(scope="module")
def setup_login_uno():
    print("Empezando login del sistema")
    yield
    print("Saliendo del sistema prueba ok")

@pytest.fixture(scope="module")
def setup_login_dos():
    print("Empezando login del sistema dos")
    yield
    print("Saliendo del sistema dos prueba ok")

def test_uno(setup_login_uno):
    print("####### Empezando test uno #############")

def test_dos(setup_login_dos):
    print("####### Empezando test dos #############")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("prueba tres del modulo login dos")