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
    print("Test uno")

@pytest.mark.run
def test_dos():
    print("Test dos")

@pytest.mark.run
def test_tres():
    print("Test tres")

@pytest.mark.notrun
def test_cuatro():
    print("Test cuatro")

@pytest.mark.run
def test_cinco():
    print("Test cinco")

@pytest.mark.notrun
def test_seis():
    print("Test seis")

@pytest.mark.skip
def test_siete():
    print("Test siete")