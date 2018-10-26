# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VehiculosItem(scrapy.Item):
    # define the fields for your item here like:
    categoria = scrapy.Field()
    titulo = scrapy.Field()
    imagen_urls = scrapy.Field()
    id = scrapy.Field() # para formar el path de la imagen-->ejemplo: auto1.jpg
    
    