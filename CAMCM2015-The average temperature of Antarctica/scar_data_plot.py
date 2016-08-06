# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from process_data import get_data
from scar_data.models import StationModel, DBSession


def draw_map():
    # lon lat
    # stations = dict(((0, -90),  # 阿蒙森-斯科特
    #                  (-34.62, -77.874),  # 贝尔拉格诺将军2号站
    #                  (76.38, -69.38),  # 中山站
    #                  (-136.87, -74.71),  # 俄罗斯站
    #                  (166.67, -77.845),  # 麦科摩多站
    #                  (140., -66.663),  # 迪蒙·迪维尔站
    #                  (11.824, -70.777),  # 新拉扎列夫站
    #                  (39.59, -69.006),  # 昭和站
    #                  (-58.964, -62.21639),  # 长城站
    #                  ))
    # setup north polar stereographic basemap.
    # The longitude lon_0 is at 6-o'clock, and the
    # latitude circle boundinglat is tangent to the edge
    # of the map at lon_0. Default value of lat_ts
    # (latitude of true scale) is pole.
    session = DBSession()
    stations = session.query(StationModel).all()

    m = Basemap(projection='spstere', boundinglat=-60, lon_0=180, resolution='l')

    for s in stations:
        xpt, ypt = m(s.longitude, s.latitude)
        m.plot(xpt, ypt, 'bo')
        plt.text(xpt, ypt, '(%.1f,%.1f)' % (s.longitude, s.latitude))
    # m.contourf()
    # 海岸线
    m.drawcoastlines()
    m.fillcontinents(color='coral', lake_color='aqua')
    # m.bluemarble()
    # 平行线和子午线
    m.drawparallels(np.arange(-80., 81., 10.))
    m.drawmeridians(np.arange(-180., 181., 10.))
    # 边界
    m.drawmapboundary(fill_color='aqua')
    # draw tissot's indicatrix to show distortion.
    plt.title("South Polar Stereographic Projection")


def draw_data():
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    data = filter(lambda v: v[0] == 81390, get_data())

    ax.plot(map(lambda v: v[1], data), map(lambda v: v[2], data))


if __name__ == '__main__':
    draw_map()
    # draw_data()
    plt.show()
