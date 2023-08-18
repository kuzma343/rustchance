from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Ініціалізація драйвера браузера Chrome
driver = webdriver.Chrome()
# Відкриття веб-сторінки
url = "https://rustchance.com/bonuses"  # Ваша URL-адреса
driver.get(url)
try:
    # Знаходження елементу, на який потрібно клікнути (за допомогою CSS селектора, ID, XPath тощо)
    element = driver.find_element(By.CSS_SELECTOR, "button.my-button-class")

    # Виконання кліку на елементі
    element.click()
finally:
    # Завершення роботи драйвера
    driver.quit()
