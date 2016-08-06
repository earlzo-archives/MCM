# -*- coding:utf-8 -*-
from model_mixins import *

# SQLALCHEMY_DATABASE_URI = 'mysql://{0:s}:{1:s}@{2:s}:{3:s}/{4:s}?charset=utf8'.format('root', 'mysqlad'
#                                                                                               'min',
#                                                                                       'localhost', '3306',
#                                                                                       'met_reader_data')
SQLALCHEMY_DATABASE_URI = 'sqlite:///met_reader_data.sqlite'
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

DBSession = sessionmaker(bind=engine)

MONTHS = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")


class StationModel(StationModelMixin, Base):
    __table_args__ = (CheckConstraint('UPPER(station_type) in ("STATION", "AWS")'),)
    station_type = Column(String(10), onupdate=lambda m: m.upper())
    # all_msl_pressure = relationship('MSLPressureModel', backref='station', lazy='dynamic')
    # all_station_pressure = relationship('StationPressureModel', backref='station', lazy='dynamic')


class TemperatureModel(TemperatureModelMixin, Base):
    __table_args__ = (
        CheckConstraint('UPPER(month) in {}'.format(MONTHS), name='month_ck'),
        CheckConstraint('UPPER(time) in ("ALL","00","06","12","18")', name='time_ck'))
    year = Column(Integer())
    month = Column(String(5), onupdate=lambda m: m.upper())
    time = Column(String(5), onupdate=lambda t: t.upper())

#
# class MSLPressureModel(TemperatureModel):
#     __tablename__ = 'msl_pressure'
#
#
# class StationPressureModel(TemperatureModel):
#     __tablename__ = 'station_pressure'
