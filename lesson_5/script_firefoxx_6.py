from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()
#Открыть страницу 
driver.get("http://the-internet.herokuapp.com/login")
username_locator = driver.find_element(By.CSS_SELECTOR, "input#username")
username_locator.send_keys("tomsmith")
password_locator = driver.find_element(By.CSS_SELECTOR, "input#password")
password_locator.send_keys("SuperSecretPassword!")
login_click = driver.find_element(By.CSS_SELECTOR,"button.radius").click()
sleep(10)
