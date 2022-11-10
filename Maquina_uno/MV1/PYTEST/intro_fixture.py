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

def setup_function(function):
    print("Esto va al inicio de cada test \n")

def teardown_function(function):
    print("Esto es al final de cada test \n")

def test_uno():
    print("Test Uno")

def test_dos():
    print("Test dos")

def test_tres():
    print("Test tres")

def test_cuatro():
    print("Test cuatro")