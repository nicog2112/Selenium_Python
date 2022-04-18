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

	def test_buscar_por_xpath(self): #Primera automatizacion en una funcion .......... Siempre poner test antes del nombre de la funcion
		driver = self.driver
		driver.get("https://www.google.com")
		time.sleep(5)
		buscar_por_xpath= driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
		time.sleep(5)
		buscar_por_xpath.send_keys("selenium",Keys.ARROW_DOWN)
		time.sleep(5)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()



#Xpath : estructura de objetos Y EXISTEN 2 TIPOS
#Xpath relativo: Simplemente puede comenzar haciendo referencia al elemento que desea e ir desde allí. //*[@id="input"]
#Xpath absoluto: Utiliza la ruta completa desde el elemento raíz hasta el elemento deseado. /html/body/ntp-app//div/ntp-realbox//div/input