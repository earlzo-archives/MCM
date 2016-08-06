# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from items import StationItem
from met_reader_data.models import StationModel, DBSession, TemperatureModel


class MySQLPipeline(object):
    def process_item(self, item, spider):
        session = DBSession()
        if isinstance(item, StationItem):
            m = StationModel(station_id=item['station_id'],
                             station_type=item['station_type'],
                             name=item['name'],
                             latitude=item['latitude'],
                             longitude=item['longitude'],
                             elevation=item['elevation'])
        else:
            m = TemperatureModel(station_data_id=item['station_data_id'],
                                 year=item['year'],
                                 month=item['month'],
                                 time=item['time'],
                                 data=item['data'])
        try:
            session.add(m)
        except Exception as e:
            logging.error(e)
            session.rollback()
        session.commit()
        session.close()
        return item
