import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from vehiculos.items import VehiculosItem
from random import randint


class AutoElevador1Spider(CrawlSpider):
    name = "autoelevador1"
    item_count = 1
    MAX_ITEMS = 350

    allowed_domain = ['www.mercadolibre.com.ar']
    
    start_urls = [
        'https://vehiculos.mercadolibre.com.ar/maquinaria-vial/autoelevadores/'
    ]
    
    rules = {
		# Boton siguiente
		Rule(LinkExtractor(allow = (), restrict_xpaths = ("//li[contains(@class, 'andes-pagination__button andes-pagination__button--next')]/a"))),
        # Ingreso al item
		Rule(LinkExtractor(allow =(), restrict_xpaths = ("//div[contains(@class, 'rowItem item item--grid item--has-row-logo new')]/a")),
            callback = 'parse_item', follow = False)
	}

    def parse_item(self, response):
        item = VehiculosItem()
        
        item['id'] = "crawler1_" + str(self.item_count)
        item['categoria'] = "autoelevador"
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        
        if self.item_count > self.MAX_ITEMS:
            raise CloseSpider("Scraping terminado con "  + str(self.item_count - 1) + " vehiculos analizados.")
        
        self.item_count += 1
        
        yield item


