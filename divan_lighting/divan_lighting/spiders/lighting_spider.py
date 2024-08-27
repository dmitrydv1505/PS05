import scrapy

class LightingSpider(scrapy.Spider):
    name = 'lighting_spider'
    allowed_domains = ['https://divan.ru']
    start_urls = ['https://www.divan.ru/category/svetilniki']

    def parse(self, response):
        # Отбираем все элементы с источниками освещения
        products = response.css('div._Ud0k')
        for product in products:
            yield {
                'name': product.css('div.wYUX2 span::text').get().strip(),
                'price': product.css('div.q5Uds span::text').get().strip(),
                'url': product.css('a').attrib['href'],
            }

        # Переход на следующую страницу, если она существует
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)