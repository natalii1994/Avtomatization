from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Firefox()
#Открыть страницу 
driver.get("http://uitestingplayground.com/classattr")
#Кликнуть на синюю кнопку 3 раза
for click in range(3):
    click_locator = driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
#При выполнении нажатия на синюю кнопку она меняет свое местоположение
sleep(10)