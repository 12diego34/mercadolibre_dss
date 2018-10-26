import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from vehiculos.items import VehiculosItem


class VehiculoSpider(CrawlSpider):
    name = "vehiculo"
    item_count_total = 0
    item_count_parcial = 0 # Vuelve a cero cuando se cambia la categoria.

    allowed_domain = ['www.mercadolibre.com.ar']
    # Nota: el resto de las urls estan en archivo en drive.
    start_urls = [
        'https://autos.mercadolibre.com.ar/hatchback/#VEHICLE_BODY_TYPE', # autos
        'https://autos.mercadolibre.com.ar/sedan/#VEHICLE_BODY_TYPE', # autos
        'https://autos.mercadolibre.com.ar/monovolumen/#VEHICLE_BODY_TYPE' # autos
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
        
        if(self.item_count_total<1000):
            item['categoria'] = "auto"
        else:
            # Si esta entre 1000 y 2000 es una camioneta, y asi.....HACER
            item['categoria'] = "camioneta"
        
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        item['id'] = str(self.item_count_parcial)
        
        if self.item_count_total > 5:
            raise CloseSpider("Scraping terminado con "  + str(self.item_count_total) + " vehiculos analizados.")
        
        self.item_count_total += 1
        self.item_count_parcial += 1

        yield item
    

# Problema de ahora: no se por que hay imagenes que no me descarga.
################## Tareas #####
# 1. limitar la cantidad de imagenes que capturamos dentro de un item 
# 2. separar las imagenes en carpetas separadas: autos, motos, etc.
# 3. Seria mas eficiente tener mas de un scrawler, y que nos dividamos pq la descarga de imagenes tarda mucho.
# 4. Vamos a tener que borrar a manopla las imagenes que no sirven: por ejemplo las que te muestran el volante, o tienen una marca de agua, etc.
