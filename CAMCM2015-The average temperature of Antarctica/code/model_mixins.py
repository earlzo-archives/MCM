# -*- coding:utf-8 -*-
from sqlalchemy import Column, String, Integer, Float, ForeignKey, CheckConstraint, create_engine
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class StationModelMixin(object):
    __tablename__ = 'station'
    id = Column(Integer(), primary_key=True)
    station_id = Column(Integer())
    name = Column(String(50), nullable=False)
    latitude = Column(Float(), nullable=False)
    longitude = Column(Float(), nullable=False)
    elevation = Column(Float(), nullable=False)

    @declared_attr
    def all_temperature(self):
        return relationship('TemperatureModel', backref='station', lazy='dynamic')


class TemperatureModelMixin(object):
    __tablename__ = 'temperature'
    id = Column(Integer(), primary_key=True)
    data = Column(Float())

    @declared_attr
    def station_data_id(self):
        return Column(Integer(), ForeignKey('station.id'))
