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


@pytest.mark.run
def test_uno():
    print("Primer test")
    assert True

@pytest.mark.run
def test_dos():
    a=10
    b=10
    assert a==b, "No son iguales"
    assert a!=b, "Son iguales"
    assert a < b, "A no es menor que B"
    assert a > b, "A no es menor que B"

@pytest.mark.run
def test_tres():
    a = 5
    b = 10
    assert a == b, "No son iguales"

@pytest.mark.run
def test_cuatro():
    a = 15
    b = 10
    assert a > b, "A no es mayor que b"

@pytest.mark.run
def test_cinco():
    nombre = "DanielC"

    assert nombre=="Daniel", "El nombre no es Daniel"