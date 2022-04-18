import unittest #prueba unitaria
from selenium import webdriver #para usar selenium
from selenium.webdriver.chrome.service import Service ## requerido en nueva version de selenium para chromedriver 
from selenium.webdriver.common.by import By  ## requerido en nueva version de selenium para chromedriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys #enviar acciones de teclado
import cv2
import time #poner tiempo a las ejecuciones

class usando_unittest(unittest.TestCase): 

	#Definicion de funciones
	#BUSCAR SELENIUM EN GOOGLE Y APRETAR FLECHA HACIA ABAJO
	def setUp(self): #inicializar el driver ......... Self = valor de regreso
		s = Service('C:/driverChrome/chromedriver.exe') ## iniciar navegador de google
		self.driver = webdriver.Chrome(service=s)

	def test_usando_implicit_wait(self): #Primera automatizacion en una funcion .......... Siempre poner test antes del nombre de la funcion
		driver = self.driver
		driver.implicitly_wait(5) #segundos
		driver.get("https://www.google.com")
		myDynamicElement = driver.find_element(By.NAME,"q")



	

if __name__ == '__main__':
	unittest.main()