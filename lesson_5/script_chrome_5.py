from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Открыть страницу 
driver.get("http://the-internet.herokuapp.com/inputs")
i