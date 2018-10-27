import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.crawler import CrawlerProcess
from vehiculos.items import VehiculosItem
from random import randint


class Auto1Spider(CrawlSpider):
    name = "auto1"
    item_count = 1
    MAX_ITEMS = 350

    allowed_domain = ['www.mercadolibre.com.ar']
    
    start_urls = [
        'https://autos.mercadolibre.com.ar/hatchback/#VEHICLE_BODY_TYPE' 
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
        item['categoria'] = "auto"
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        
        if self.item_count > self.MAX_ITEMS:
            raise CloseSpider("Scraping terminado con "  + str(self.item_count - 1) + " vehiculos analizados.")
        
        self.item_count += 1
        
        yield item


class Auto2Spider(CrawlSpider):
    name = "auto2"
    item_count = 1
    MAX_ITEMS = 350
    
    allowed_domain = ['www.mercadolibre.com.ar']
    
    start_urls = [
        'https://autos.mercadolibre.com.ar/sedan/#VEHICLE_BODY_TYPE'
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
        
        item['id'] = "crawler2_" + str(self.item_count)
        item['categoria'] = "auto"
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        
        if self.item_count > self.MAX_ITEMS:
            raise CloseSpider("Scraping terminado con "  + str(self.item_count - 1) + " vehiculos analizados.")
        
        self.item_count += 1
        
        yield item


class Auto3Spider(CrawlSpider):
    name = "auto3"
    item_count = 1
    MAX_ITEMS = 300

    allowed_domain = ['www.mercadolibre.com.ar']
    
    start_urls = [
        'https://autos.mercadolibre.com.ar/monovolumen/#VEHICLE_BODY_TYPE'
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
        
        item['id'] = "crawler3_" + str(self.item_count)
        item['categoria'] = "auto"
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        
        if self.item_count > self.MAX_ITEMS:
            raise CloseSpider("Scraping terminado con "  + str(self.item_count - 1) + " vehiculos analizados.")
        
        self.item_count += 1
        
        yield item




# Problema de ahora: no se por que hay imagenes que no me descarga.
################## Tareas #####
# 1. limitar la cantidad de imagenes que capturamos dentro de un item 
# 2. separar las imagenes en carpetas separadas: autos, motos, etc.
# 3. Seria mas eficiente tener mas de un scrawler, y que nos dividamos pq la descarga de imagenes tarda mucho.
# 4. Vamos a tener que borrar a manopla las imagenes que no sirven: por ejemplo las que te muestran el volante, o tienen una marca de agua, etc.



        #https://stackoverflow.com/questions/39365131/running-multiple-spiders-in-scrapy-for-1-website-in-parallel
        #https://kirankoduru.github.io/python/multiple-scrapy-spiders.html
        #scrapy multiple crawlers with own pipeline

#process = CrawlerProcess()
#process.crawl(Auto1Spider)
#process.crawl(Auto2Spider)
#process.start() # the script will block here until all crawling jobs are finished

"""
start_urls = [
        #'https://autos.mercadolibre.com.ar/hatchback/#VEHICLE_BODY_TYPE' # autos
        'https://autos.mercadolibre.com.ar/sedan/#VEHICLE_BODY_TYPE' # autos
        #'https://autos.mercadolibre.com.ar/monovolumen/#VEHICLE_BODY_TYPE' # autos
    ]
"""