from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Открыть страницу 
driver.get("http://the-internet.herokuapp.com/inputs")
input_locator = driver.find_element(By.CSS_SELECTOR, "input")
input_locator.send_keys("1000")
sleep(5)
input_locator.clear()
sleep(5)
input_locator.send_keys("999")