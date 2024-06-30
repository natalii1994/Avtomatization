from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Открыть страницу 
driver.get("http://uitestingplayground.com/textinput")
#Выбрать локатор и ввести текст
input_locator = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
input_locator.send_keys("SkyPro")
#Нажать на синюю кнопку
btn_locator = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
#Текст новой кнопки
btn_locator = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(btn_locator)