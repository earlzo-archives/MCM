# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function

import scipy.io as sio
import pandas as pd
from pylab import *
from mcm import report_dir

# results = sio.loadmat('AHP_results.mat')['results']

# 回报率
r_m1 = dict(
    lambda_=6.003699141082742,
    cil=7.398282165484105e-04,
    crl=5.966356585067826e-04,
    w=array([
        0.174945915170389,
        0.0900538045796213,
        0.464838866511126,
        0.0900538045796212,
        0.0900538045796212,
        0.0900538045796212
    ])
)

# 资金利用率
r_m2 = dict(
    lambda_=8.118590637425990,
    cil=0.016941519632284,
    crl=0.012015262150556,
    w=array([
        0.0358755087680491,
        0.0971305910935339,
        0.0601426838092208,
        0.227085892083473,
        0.329939953872746,
        0.0601426838092209,
        0.129540002754535,
        0.0601426838092209
    ])
)

# 回报率对资金利用率
r_m3 = dict(
    lambda_=2,
    cil=0,
    crl=np.nan,
    w=array([
        0.750000000000000,
        0.250000000000000
    ])
)

Y1 = r_m3['w'][0] * r_m1['w']
Y2 = r_m3['w'][1] * r_m2['w']

Z = np.concatenate((Y1, Y2))

# 将PCA变量的权重向量重新排序
vec = pd.Series(Z, index=[7, 9, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 8, 10])
vec.sort_index(inplace=True)
