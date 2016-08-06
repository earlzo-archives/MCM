# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    station_id = scrapy.Field()
    station_type = scrapy.Field()
    name = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    elevation = scrapy.Field()


class TemperatureItem(scrapy.Item):
    station_data_id = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    time = scrapy.Field()
    data = scrapy.Field()
