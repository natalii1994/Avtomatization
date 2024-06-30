from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Открыть страницу 
driver.get("http://uitestingplayground.com/ajax")
#Подождать 16 секунд
driver.implicitly_wait(16)
#Кликнуть на синюю кнопку
driver.find_element(By.CSS_SELECTOR,"#ajaxButton").click()
#Найти текст зеленой плашки
text = driver.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(text)
#Закрыть браузер
driver.quit()
