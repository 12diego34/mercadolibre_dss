# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
import csv

class VehiculosPipeline(object):
    def __init__(self):
        self.files = {}
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline
    
    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        self.exporter.fields_to_export = ['id','categoria', 'titulo', 'imagen_urls']
        self.exporter.start_exporting()
    
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


  
class VehiculosImagenesPipeline(ImagesPipeline):

   # def get_media_requests(self, item, info):
    #    nombre_imagen = item['categoria'] + item['id']
        
     #   return [Request(x, meta={'image_name': nombre_imagen,'categoria': item['categoria']})
      #      for x in item.get('imagen_urls', [])]
    

    def get_media_requests(self, item, info):
        #lista_urls = item['imagen_urls'].split(",")
        print("======================")
        #for i in item['imagen_urls']:
        for i in range(len(item['imagen_urls'])):
            print(item['imagen_urls'][i])
            nombre_imagen = item['categoria'] + "_" + item['id'] + "_" +str(i)
            yield Request(item['imagen_urls'][i], meta={'image_name': nombre_imagen})
        print("======================")    
        #return [Request(x, meta={'image_name': item["titulo"]})
         #       for x in item.get('imagen_urls', [])]

    def file_path(self, request, response=None, info=None):
        return '%s.jpg' % request.meta['image_name']
            

        
        
    #def file_path(self, request, response=None, info=None):
     #   print("======================")
      #  print(request.meta['image_name'])
       # print(request.meta['categoria'])
       # print("======================")
       # return '%s.jpg' % request.meta['image_name']


