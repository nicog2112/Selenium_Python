import unittest #prueba unitaria
from selenium import webdriver #para usar selenium
from selenium.webdriver.chrome.service import Service ## requerido en nueva version de selenium para chromedriver 
from selenium.webdriver.common.by import By  ## requerido en nueva version de selenium para chromedriver 
from selenium.webdriver.common.keys import Keys #enviar acciones de teclado
import time #poner tiempo a las ejecuciones

class usando_unittest(unittest.TestCase): 

	#Definicion de funciones
	#BUSCAR SELENIUM EN GOOGLE Y APRETAR FLECHA HACIA ABAJO
	def setUp(self): #inicializar el driver ......... Self = valor de regreso
		s = Service('C:/driverChrome/chromedriver.exe') ## iniciar navegador de google
		self.driver = webdriver.Chrome(service=s)

	def test_cambiar_ventana(self): #Primera automatizacion en una funcion .......... Siempre poner test antes del nombre de la funcion
		driver = self.driver
		driver.get("https://www.google.com")
		time.sleep(3)
		driver.execute_script("window.open('');") #instruccion script para abrir una nueva ventana en python
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[1]) #instruccion para ubicarnos en la siguiente pestaña
		driver.get("https://stackoverflow.com")
		time.sleep(3)
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(3)


	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
