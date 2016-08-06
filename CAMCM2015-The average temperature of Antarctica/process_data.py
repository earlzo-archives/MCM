# -*- coding:utf-8 -*-

from pylab import *


def get_station():
    station = np.genfromtxt('scar_data/site_detail.txt',
                             dtype=[('id', np.int), ('name', np.str), ('lat', np.float), ('lon', np.float)],
                             comments='%', delimiter='\t', usecols=(0, 1, 2, 3), autostrip=True, )
    return station


def get_data():
    data = np.genfromtxt('scar_data/data.txt',
                          dtype=[('id', np.int), ('date', np.float), ('temperature', np.float)],
                          comments='%', delimiter='\t', usecols=(0, 2, 3), autostrip=True, )
    return data


if __name__ == '__main__':
    get_station()
