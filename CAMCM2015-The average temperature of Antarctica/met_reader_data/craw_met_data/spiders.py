# met_reader_data/crawl_met_data/spiders.py
# -*- coding:utf-8 -*-
import urlparse
from scrapy import Spider, Request
from items import StationItem, TemperatureItem
from met_reader_data.models import StationModel, DBSession

STATION_TYPES = {'Station Surface Data': 'SURFACE', 'AWS Data': 'AWS'}
MONTHS = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
BASE_URL = 'https://legacy.bas.ac.uk/met/READER/'


def convert_lat_or_lon(lat_or_lon):
    d = lat_or_lon[-1:].upper()
    v = float(lat_or_lon[:-1].strip())
    if d in ('S', 'W'):
        v = -v
    return v


class StationSpider(Spider):
    name = 'StationSpider'
    start_urls = [urlparse.urljoin(BASE_URL, 'surface/stationpt.html'),
                  urlparse.urljoin(BASE_URL, 'aws/awspt.html')]

    def parse(self, response):
        title = response.xpath('//h2[1]/text()').extract()[0]
        station_type = STATION_TYPES[title]
        trs = response.xpath('//table/tbody/tr')

        for tr in trs:
            raw_station_data = tr.xpath('th[position()<6]/text()').extract()
            station_item = StationItem(station_type=station_type,
                                       station_id=int(raw_station_data[0]),
                                       name=raw_station_data[1],
                                       latitude=convert_lat_or_lon(raw_station_data[2]),
                                       longitude=convert_lat_or_lon(raw_station_data[3]),
                                       elevation=float(raw_station_data[4].strip(' m')))
            yield station_item


class TemperatureSpider(Spider):
    name = 'TemperatureSpider'

    def start_requests(self):
        session = DBSession()
        stations = session.query(StationModel).all()
        for s in stations:
            base_data_path = urlparse.urljoin(BASE_URL, ''.join([s.station_type.lower(), '/']))
            for time in ('All', '00', '06', '12', '18'):
                temperature_url = urlparse.urljoin(base_data_path, '.'.join([s.name, time, 'temperature.txt']))
                yield Request(temperature_url, callback=lambda r: self.parse_data(r, s.id, time))

    def parse_data(self, response, station_data_id, time):
        for line in response.body.strip().split('\n')[1:]:
            row = line.split()
            year = row.pop(0)
            for m, v in zip(MONTHS, row):
                if v == '-':
                    data = None
                else:
                    data = float(v)
                temperature_item = TemperatureItem(station_data_id=station_data_id, year=year, month=m, time=time,
                                                   data=data)
                yield temperature_item
