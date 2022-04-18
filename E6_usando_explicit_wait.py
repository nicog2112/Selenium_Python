import unittest #prueba unitaria
from selenium import webdriver #para usar selenium
from selenium.webdriver.chrome.service import Service ## requerido en nueva version de selenium para chromedriver 
from selenium.webdriver.common.by import By  ## requerido en nueva version de selenium para chromedriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys #enviar acciones de teclado
import time #poner tiempo a las ejecuciones

class usando_unittest(unittest.TestCase): 

	#Definicion de funciones
	#BUSCAR SELENIUM EN GOOGLE Y APRETAR FLECHA HACIA ABAJO
	def setUp(self): #inicializar el driver ......... Self = valor de regreso
		s = Service('C:/driverChrome/chromedriver.exe') ## iniciar navegador de google
		self.driver = webdriver.Chrome(service=s)

	def test_usando_explicit_wait(self): #Primera automatizacion en una funcion .......... Siempre poner test antes del nombre de la funcion
		driver = self.driver
		driver.get("https://www.google.com")
		try:
			element = WebDriverWait(driver,10).until(
				EC.presence_of_element_located((By.NAME,"q"))
			)
		finally:
			driver.quit()


	

if __name__ == '__main__':
	unittest.main()


	
