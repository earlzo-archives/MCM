# met_reader_data_plot.py
# -*- coding:utf-8 -*-
from pprint import pprint
from pylab import *
from sqlalchemy import func
from mpl_toolkits.basemap import Basemap
from met_reader_data.models import StationModel, TemperatureModel, DBSession, MONTHS

session = DBSession()


def do_nothing(*args, **kwargs):
    pass


def date2float(year, month):
    return year + (MONTHS.index(month) - 0.5) / 12


def area_average(station_data_ids, year_step=True, time='All'):
    query = session.query(TemperatureModel.station_data_id,
                          TemperatureModel.year,
                          TemperatureModel.month,
                          func.avg(TemperatureModel.data).label('average_temperature')
                          ).filter(TemperatureModel.station_data_id.in_(station_data_ids),
                                   TemperatureModel.data.isnot(None),
                                   TemperatureModel.time == time).group_by(TemperatureModel.year,
                                                                           TemperatureModel.month)
    if year_step:
        query = session.query('station_data_id', 'year',
                              func.avg('average_temperature').label('average_temperature')
                              ).select_from(query.subquery()).group_by('year')
    temperatures = query.all()
    pprint(temperatures)


def plot_station_map(stations=None, show_text=False):
    fig = plt.figure()
    m = Basemap(projection='spstere', boundinglat=-60, lon_0=180, resolution='l', ax=fig.add_subplot(111))
    if stations is None:
        stations = session.query(StationModel).all()
    show_text_func = plt.text if show_text else do_nothing
    fig_title = '{} stations in Antarctica '.format(len(stations))
    fig.canvas.set_window_title(fig_title)
    m.ax.set_title(fig_title)
    xpts = []
    ypts = []
    for s in stations:
        xpt, ypt = m(s.longitude, s.latitude)
        xpts.append(xpt)
        ypts.append(ypt)
        m.plot(xpt, ypt, 'ro')
        show_text_func(xpt, ypt, '{}'.format(s.id), color='y')
    m.bluemarble()
    m.drawparallels(np.arange(-80., 81., 5.), 'g', labels=[1, 1, 0, 1])
    m.drawmeridians(np.arange(-180., 181., 10.), 'g')
    fig.show()


def plot_elevation_contour(stations=None):
    if stations is None:
        stations = session.query(StationModel).filter(StationModel.id.notin_((77, 89, 105)),
                                                      StationModel.latitude < -60).all()
    m = Basemap(projection='spstere', boundinglat=-60, lon_0=180, resolution='l')
    xpts = []
    ypts = []
    datas = []
    for s in stations:
        xpt, ypt = m(s.longitude, s.latitude)
        xpts.append(xpt)
        ypts.append(ypt)
        datas.append(s.elevation)
        m.plot(xpt, ypt, 'bo')
        # plt.text(xpt, ypt, '(%.1f,%.1f)' % (t.station.longitude, t.station.latitude))
        plt.text(xpt, ypt, '%d' % s.id)
    x, y = np.meshgrid(xpts, ypts)
    axis_x = np.arange(min(xpts), max(xpts), 10 ** 4)
    axis_y = np.arange(min(ypts), max(ypts), 10 ** 4)
    z = griddata(xpts, ypts, datas, axis_x, axis_y, 'linear')
    # print len(z) - len(x)
    m.contourf(xpts, ypts, datas)
    m.colorbar()
    plt.title('Antarctic Elevation Map')


def plot_single_year(station_data_id, year, r=1, c=1):
    fig = plt.figure()
    fig.canvas.set_window_title('The Temperature Tendency of in a year')
    if isinstance(station_data_id, int):
        station_data_id = (station_data_id,)
    for i, id in enumerate(station_data_id):
        ax = fig.add_subplot(r, c, i + 1)
        if isinstance(year, int):
            year = (year,)
        station = session.query(StationModel).filter_by(id=id).one()

        ax_title = 'The Temperature Tendency of {} in a year'.format(station.name)
        ax.set_title(ax_title)
        for y in year:
            temperatures = station.all_temperature.filter(TemperatureModel.data.isnot(None), TemperatureModel.year == y,
                                                          TemperatureModel.time == 'All').all()
            ax.plot(map(lambda v: MONTHS.index(v.month) + 1, temperatures),
                    map(lambda v: v.data, temperatures),
                    label=y)
        ax.set_xlim(1)
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.legend(loc=4)

        ax.set_xlabel('Month')
        ax.set_ylabel(u'Temperature(℃)')
    fig.show()


def plot_contour(stations=None, show_text=False):
    from mpl_toolkits.mplot3d import axes3d
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # ax.set_xlabel('X')
    # ax.set_xlim(-40, 40)
    # ax.set_ylabel('Y')
    # ax.set_ylim(-40, 40)
    # ax.set_zlabel('Z')
    # ax.set_zlim(-100, 100)

    m = Basemap(projection='spstere', boundinglat=-60, lon_0=180, resolution='l')
    if stations is None:
        stations = session.query(StationModel).filter(StationModel.id.notin_((77, 89, 105)),
                                                      StationModel.latitude < -60).all()
    xpts = []
    ypts = []
    datas = []
    for s in stations:
        xpt, ypt = m(s.longitude, s.latitude)
        xpts.append(xpt)
        ypts.append(ypt)
        datas.append(s.elevation)
    axis_x = np.arange(min(xpts), max(xpts), 10**4)
    axis_y = np.arange(min(ypts), max(ypts), 10**4)
    X, Y = meshgrid(axis_x, axis_y)
    Z = griddata(xpts, ypts, datas, X, Y, 'linear')
    ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)

    cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)

    fig.show()


if __name__ == '__main__':
    plot_contour()
    plt.show()
