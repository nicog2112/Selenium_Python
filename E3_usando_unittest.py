import unittest #prueba unitaria
from selenium import webdriver #para usar selenium
from selenium.webdriver.chrome.service import Service ## requerido en nueva version de selenium para chromedriver 
from selenium.webdriver.common.by import By  ## requerido en nueva version de selenium para chromedriver 
from selenium.webdriver.common.keys import Keys #enviar acciones de teclado
import time #poner tiempo a las ejecuciones



class usando_unittest(unittest.TestCase): 

	#Definicion de funciones
	
	def setUp(self): #inicializar el driver ......... Self = valor de regreso
		s = Service('C:/driverChrome/chromedriver.exe') ## iniciar navegador de google
		self.driver = webdriver.Chrome(service=s)

	def test_buscar(self): #Primera automatizacion en una funcion .......... Siempre poner test antes del nombre de la funcion
		driver = self.driver
		driver.get("https://www.google.com")
		self.assertIn("Google" , driver.title)
		elemento = driver.find_element(By.NAME, "q")
		elemento.send_keys("selenium")
		elemento.send_keys(Keys.RETURN)
		time.sleep(5)
		assert "No se encontro el elemento:" not in driver.page_source

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()