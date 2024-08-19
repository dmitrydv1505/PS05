# PS05
 PS05. Введение в Scrapy. Web Scraping

================================================================
Время выполнить задание
Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru
Нужно взять название источника освещения, цену и ссылку
*Можно попробовать сделать это на другом сайте с продажей источников освещения
================================================================

1. Устанавливаем Scrapy:
   ```bash
   pip install scrapy
   ```
2. Создаем новый Scrapy проект:
   ```bash
   scrapy startproject divan_spider
   cd divan_spider
   ```
3. Создаем новый spider:
   ```bash
   scrapy genspider lighting divan.ru
   ```
4. Открываем файл `divan_spider/spiders/lighting.py` и заменяем его содержимое следующим кодом:

```python
import scrapy


class LightingSpider(scrapy.Spider):
    name = 'lighting'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/category/svetilniki']  # URL категории светильников, если известен

    def parse(self, response):
        # Найдите и извлеките данные о продуктах
        for product in response.css('div.product-card'):
            yield {
                'name': product.css('div.product-card__name::text').get(),
                'price': product.css('div.product-card__price::text').get(),
                'link': response.urljoin(product.css('a.product-card__link::attr(href)').get())
            }

        # Пагинация, если доступна
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

5. Измените `product-card`, `product-card__name`, `product-card__price` и `product-card__link` на реальные CSS-селекторы, соответствующие элементам на сайте. Вы можете использовать инструменты разработчика в браузере, чтобы определить правильные селекторы.

6. Запустите spider и сохраните данные в CSV файл:

   ```bash
   scrapy crawl lighting -o lighting.csv
   ```

Этот скрипт создаст файл `lighting.csv`, содержащий название, цену и ссылку для каждого источника освещения, найденного на сайте. Обратите внимание, что если сайт имеет динамическую загрузку контент