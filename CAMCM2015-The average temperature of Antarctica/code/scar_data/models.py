# -*- coding:utf-8 -*-
import logging
from pylab import *
from model_mixins import *

# SQLALCHEMY_DATABASE_URI = 'mysql://{0:s}:{1:s}@{2:s}:{3:s}/{4:s}?charset=utf8'.format('root', 'mysqladmin',
#                                                                                       'localhost', '3306',
#                                                                                       'scar_data')

SQLALCHEMY_DATABASE_URI = 'sqlite:///scar_data.sqlite'

logger = logging.getLogger('sqlalchemy')
logger.setLevel(logging.INFO)
engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)

DBSession = sessionmaker(bind=engine)


class StationModel(StationModelMixin, Base):
    pass


class TemperatureModel(TemperatureModelMixin, Base):
    date = Column(Float(), nullable=False)
    observations = Column(Integer())


def get_station():
    station = np.genfromtxt('site_detail.txt',
                            dtype=[('station_id', np.int), ('name', np.unicode),
                                   ('latitude', np.float), ('longitude', np.float), ('elevation', np.float)],
                            # todo: 编码有问题
                            # converters={1: lambda v: v.decode('Windows-1252')},
                            # converters={1: lambda v: v.decode('ISO-8859-1')},
                            comments='%', delimiter='\t', usecols=(0, 1, 2, 3, 4), autostrip=True)
    logger.info('Got Raw Station Data!')
    return station


def get_temperature():
    temperature = np.genfromtxt('data.txt',
                                dtype=[('station_id', np.int), ('date', np.float),
                                       ('data', np.float), ('observations', np.int)],
                                converters={5: lambda v: None if v == -99 else v},
                                comments='%', delimiter='\t', usecols=(0, 2, 3, 5), autostrip=True)
    logger.info('Got Raw Temperature Data!')
    return temperature


def setup_database():
    Base.metadata.drop_all(engine)
    logger.info('Database dropped!')
    Base.metadata.create_all(engine)
    logger.info('Database created!')
    session = DBSession()
    try:
        stations = map(lambda value: StationModel(station_id=value[0],
                                                  name=value[1],
                                                  latitude=value[2],
                                                  longitude=value[3],
                                                  elevation=value[4]), get_station())
        logger.info('Station data was processed!')
        session.add_all(stations)
        session.commit()

        temperatures = map(
            lambda value: TemperatureModel(station=session.query(StationModel).filter_by(station_id=value[0]).one(),
                                           date=value[1],
                                           data=value[2],
                                           observations=value[3]), get_temperature())
        logger.info('Temperatures data was processed!')
        session.add_all(temperatures)
    except Exception as e:
        logger.error(e)
        session.rollback()
    session.commit()
    session.close()
    logger.info('Database was set up !')
