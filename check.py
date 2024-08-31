import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

url = 'https://lu.ru/rasprodazhi/ucenka/'

driver.get(url)

time.sleep(3)

lights = driver.find_elements(By.CLASS_NAME, 'product-block')

parsed_data = []

for light in lights:
    try:
        title = light.find_element(By.CSS_SELECTOR, 'span.name_good_item').text
        price = light.find_element(By.CLASS_NAME, 'new-price').text
        link = light.find_element(By.CSS_SELECTOR, 'a.product-name').get_attribute('href')
    except:
        print('Ошибка при парсинге')
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open('lights.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)