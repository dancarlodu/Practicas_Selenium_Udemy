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


@pytest.mark.validar
def test_validar():
    nom1 = "Rodrigo"
    nom2 = "Rodrigo"

    assert nom1==nom2, "Los nombres no son iguales"

@pytest.mark.validar2
def test_validar2():
    a=200
    b=50
    c=20

    assert a<=b and a<=c, "A es menor que B"

@pytest.mark.validar_in
def test_validar_in():
    dato="Ram"
    frase="Dentro de las computadoras hay memoria RAM"


    assert dato in frase, "El dato no esta dentro de la frase"

@pytest.mark.validar_doble
def test_validar_doble():
    a=20
    b=20
    if(a==b):
        assert True, "Los datos son iguales"
    else:
        assert False, "No son iguales"