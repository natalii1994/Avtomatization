from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Открыть страницу 
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
#Нажать 5 раз на кнопку
for click in range(0,5):
    click_locator = driver.find_element(By.CSS_SELECTOR, "button").click()
#Собрать список кнопок "Delete" со страницы 
button_list = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")
#Вывод размера списка
print(len(button_list))
