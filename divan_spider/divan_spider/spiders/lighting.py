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