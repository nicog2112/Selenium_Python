from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service('C:/driverChrome/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://gmail.com")

usuario = driver.find_element(By.ID, "identifierId")
usuario.send_keys("gaunanicolas911@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3);

clave  = driver.find_element(By.NAME, "password")

clave.send_keys("Nico41382")
usuario.send_keys(Keys.ENTER)
