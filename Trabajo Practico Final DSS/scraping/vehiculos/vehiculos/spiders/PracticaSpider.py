import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from vehiculos.items import VehiculosItem


class PracticaSpider(CrawlSpider):
    name = "practica"
    item_count_total = 0
    item_count_parcial = 0 # Vuelve a cero cuando se cambia la categoria.

    allowed_domain = ['www.mercadolibre.com.ar']
    # Nota: el resto de las urls estan en archivo en drive.
    start_urls = [
        'https://autos.mercadolibre.com.ar/hatchback/#VEHICLE_BODY_TYPE' # autos
        'https://autos.mercadolibre.com.ar/sedan/#VEHICLE_BODY_TYPE', # autos
        'https://autos.mercadolibre.com.ar/monovolumen/#VEHICLE_BODY_TYPE' # autos
    ]
    

    rules = {
		# Boton siguiente
		Rule(LinkExtractor(allow = (), restrict_xpaths = ("//li[contains(@class, 'andes-pagination__button andes-pagination__button--next')]/a")))
        # Ingreso al item
		#Rule(LinkExtractor(allow =(), restrict_xpaths = ("//div[contains(@class, 'rowItem item item--grid item--has-row-logo new')]/a")),
         #   callback = 'parse_item', follow = False)
	}
    
    

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_listado)       


    def parse_listado(self, response):
        #items
        listado_items_str = "//div[contains(@class, 'rowItem item item--grid item--has-row-logo new')]//a/@href"
        
        listado_items = response.xpath(listado_items_str)
        
        
        listado = []
        
        #print("===========================")
        for href in listado_items:
            url = href.extract()
            if not any(url in s for s in listado):
                listado.append(url)

        numero = 0
        
        for i in range(len(listado)):
            numero = i
            item = listado[i]
            yield scrapy.Request(url=item, callback = self.parse_item)
            break
            
        """
        #numero = len(listado) - numero
        numero = 1
        if(numero == 1):
            #print("===========================")
            print("ENTRE")
            #boton siguiente
            pagina_siguiente_str = "//li[contains(@class, 'andes-pagination__button andes-pagination__button--next')]//a/@href"
            pagina_siguiente = response.xpath(pagina_siguiente_str)
            url = pagina_siguiente.extract()
            yield scrapy.Request(url=url, callback=self.parse_listado)
        
        
        
            
            
            

        #print("===========================")
        if self.item_count_total > 5:
            raise CloseSpider("Scraping terminado con "  + str(self.item_count_total) + " vehiculos analizados.")
          
        else:
            #boton siguiente
            pagina_siguiente_str = "//li[contains(@class, 'andes-pagination__button andes-pagination__button--next')]//a/@href"
            pagina_siguiente = response.xpath(pagina_siguiente_str)
            url = pagina_siguiente.extract()
            yield scrapy.Request(url=url, callback='parse_listado')
        """

    
    
    def parse_item(self, response):
        item = VehiculosItem()
        item['id'] = "1"
        item['categoria'] = "auto"
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        self.item_count_total += 1
        """
        if(self.item_count_total<1000):
            item['categoria'] = "auto"
        else:
            # Si esta entre 1000 y 2000 es una camioneta, y asi.....HACER
            item['categoria'] = "camioneta"
        
        item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
        item['imagen_urls'] = response.xpath('//figure[contains(@class, "gallery-image-container")]/a/img/@src').extract()
        item['id'] = str(self.item_count_parcial)
        
        #if self.item_count_total > 2:
         #   raise CloseSpider("Scraping terminado con "  + str(self.item_count_total) + " vehiculos analizados.")
        
        self.item_count_total += 1
        self.item_count_parcial += 1
        """

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