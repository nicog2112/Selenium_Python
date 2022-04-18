from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/driverChrome/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://python.org")
driver.close()
