from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#Открыть страницу 
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#Дождаться загрузки страницы с помощью текста "Done!"
waiter = WebDriverWait (driver, 30)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"),"Done!")
)
#Вывести в консоль атрибут src 3 картинки
src_3_picture = driver.find_element(By.CSS_SELECTOR,"#award").get_attribute("src")
print(src_3_picture)