import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def saludos(self):
        print("Bienvenidos a Page Object Model")

    def Tiempo(self,tie):
        t=time.sleep(tie)
        return t

    def navegar(self,url, Tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        print("Página abierta: "+str(url))
        t = time.sleep(Tiempo)
        return  t

    def texto_Xpath(self, xpath, texto, Tiempo):
        valor = self.driver.find_element(By.XPATH, xpath)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def texto_Xpath_Validar(self, selector, texto, tiempo):
        try:
            valor=self.SEX(selector)
            valor.clear()
            valor.send_keys(texto)
            print("Escribiendo en el campo  --> {} el texto {}".format(xpath, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + xpath)

    def texto_ID(self, ID, texto, Tiempo):
        valor = self.driver.find_element(By.ID, ID)
        valor.clear()
        valor.send_keys(texto)
        t = time.sleep(Tiempo)
        return t

    def texto_ID_Validar(self, selector, texto, tiempo):
        try:
            valor=self.SEI(selector)
            valor.clear()
            valor.send_keys(texto)
            print("Escribiendo en el campo  --> {} el texto {}".format(ID, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + ID)

    def click_Xpath_Validar(self, selector, tiempo):
        try:
            valor=self.SEX(selector)
            valor.click()
            print("Click en el campo --> {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + xpath)

    def click_ID_Validar(self, selector, tiempo):
        try:
            valor=self.SEI(selector)
            valor.click()
            print("Click en el campo {} ".format(ID))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + ID)

    def salida(self):
        print("Se termina la prueba exitosamente ...")

    def select_Xpath_texto(self, selector, texto,tiempo):
        try:
            valor=self.SEX(selector)
            valor=Select(valor)
            valor.select_by_visible_text(texto)
            print("El campo seleccionado es {} ".format(texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + xpath)

    def select_Xpath_type(self, selector, tipo, dato, tiempo):
        try:
            valor=self.SEX(selector)
            valor = Select(valor)
            if (tipo=="text"):
                valor.select_by_visible_text(dato)
            elif(tipo=="index"):
                valor.select_by_index(dato)
            elif(tipo=="value"):
                valor.select_by_value(dato)
            print("El campo seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + xpath)


    def select_ID_type(self, selector, tipo, dato, tiempo):
        try:
            valor = self.SEI(selector)
            valor = Select(valor)
            if (tipo=="text"):
                valor.select_by_visible_text(dato)
            elif(tipo=="index"):
                valor.select_by_index(dato)
            elif(tipo=="value"):
                valor.select_by_value(dato)
            print("El campo seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + ID)

    def upload_Xpath(self, selector, ruta, tiempo):
        try:
            valor = self.SEX(selector)
            valor.send_keys(ruta)
            print("Se carga imagen --> {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + xpath)

    #Función para cargar archivos por ID
    def upload_ID(self, selector, ruta, tiempo):
        try:
            valor = self.SEI(selector)
            valor.send_keys(ruta)
            print("Se carga imagen --> {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + ID)

    #Función radio y check por XPATH
    def check_Xpath(self, selector, tiempo):
        try:
            valor = self.SEX(selector)
            valor.click()
            print("Click en el elemento --> {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + xpath)

    # Función radio y check por ID
    def check_ID(self, selector, tiempo):
        try:
            valor = self.SEI(selector)
            valor.click()
            print("Click en el elemento --> {} ".format(ID))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el elemento --> " + ID)

    # Función radio y check por XPATH para multiples selecciones
    def check_Xpath_multiple(self, tiempo, *args):
        try:
            for num in args:
                valor = self.SEX(num)
                valor.click()
                print("Click en el elemento --> {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontró el elemento --> " + num)

    def SEX(self,elemento): # Seleccionar elemento por XPATH
        valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
        valor = self.driver.find_element(By.XPATH, elemento)
        return  valor

    def SEI(self,elemento): # Seleccionar elemento por ID
        valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elemento)))
        valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
        valor = self.driver.find_element(By.ID, elemento)
        return  valor

    def texto_mixto(self, tipo, selector, texto, tiempo):
        if (tipo=="xpath"):
            try:
                valor = self.SEX(selector)
                valor.clear()
                valor.send_keys(texto)
                print("Escribiendo en el campo  --> {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

        elif (tipo=="id"):
            try:
                valor = self.SEI(selector)
                valor.clear()
                valor.send_keys(texto)
                print("Escribiendo en el campo  --> {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

    def click_mixto(self, tipo, selector, tiempo):
        if(tipo=="xpath"):
            try:
                valor=self.SEX(selector)
                valor.click()
                print("Click en el campo --> {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)
        elif(tipo=="id"):
            if (tipo == "id"):
                try:
                    valor = self.SEI(selector)
                    valor.click()
                    print("Click en el campo --> {} ".format(selector))
                    t = time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontró el elemento --> " + selector)

    def existe(self, tipo, selector, tiempo):
        if (tipo=="xpath"):
            try:
                valor=self.SEX(selector)
                print("El elemento {} --> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)
                return "No Existe"

        elif (tipo=="id"):
            if (tipo == "id"):
                try:
                    valor = self.SEI(selector)
                    print("El elemento {} --> existe ".format(selector))
                    t = time.sleep(tiempo)
                    return "Existe"
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontró el elemento --> " + selector)
                    return "No Existe"

    def mouse_doble(self, tipo, selector, tiempo=0.2):
        if (tipo=="xpath"):
            try:
                valor=self.SEX(selector)
                action = ActionChains(self.driver)
                action.double_click(valor).perform()
                print("Double click  en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

        elif (tipo=="id"):
            try:
                valor=self.SEI(selector)
                action = ActionChains(self.driver)
                action.double_click(valor).perform()
                print("Double click  en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

    def mouse_derecho(self, tipo, selector, tiempo=0.2):
        if (tipo == "xpath"):
            try:
                valor = self.SEX(selector)
                action = ActionChains(self.driver)
                action.context_click(valor).perform()
                print("click derecho en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

        elif (tipo == "id"):
            try:
                valor = self.SEI(selector)
                action = ActionChains(self.driver)
                action.context_click(valor).perform()
                print("click derecho  en {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

    def mouse_dragDrop(self, tipo, selector, destino,tiempo=0.2):
        if (tipo == "xpath"):
            try:
                valor = self.SEX(selector)
                valor2 = self.SEX(destino)
                action = ActionChains(self.driver)
                action.drag_and_drop(valor, valor2).perform()
                print("Se solto el elemento {} en destino {} ".format(selector,destino))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

        elif (tipo == "id"):
            try:
                valor = self.SEI(selector)
                valor2= self.SEI(destino)
                action = ActionChains(self.driver)
                action.drag_and_drop(valor, valor2).perform()
                print("Se solto el elemento {} en destino {} ".format(selector,destino))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

    def mouse_dragDropXY(self, tipo, selector, x, y, tiempo=0.2):
        if (tipo == "xpath"):
            try:
                self.driver.switch_to.frame(0)
                valor = self.SEX(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(valor, x,y).perform()
                print("Se solto el elemento {}  ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)


        elif (tipo == "id"):
            try:
                self.driver.switch_to.frame(0)
                valor = self.SEX(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(valor, x, y).perform()
                print("Se solto el elemento {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)

    def clickXY(self, tipo, selector, x, y, tiempo=0.2):
        if (tipo == "xpath"):
            try:
                valor = self.SEX(selector)
                action = ActionChains(self.driver)
                action.move_to_element_with_offset(valor, x, y).click().perform()
                print("Click al elemento {} coordinada {} {}  ".format(selector,x,y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)


        elif (tipo == "id"):
            try:
                valor = self.SEX(selector)
                action = ActionChains(self.driver)
                action.drag_and_drop_by_offset(valor, x, y).click().perform()
                print("Click al elemento {} coordinada {} {}  ".format(selector,x,y))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el elemento --> " + selector)