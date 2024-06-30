from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()
#Открыть страницу 
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(5)

#Нажать кнопку "Close" в модальном окне
click_locator = driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
sleep(10)