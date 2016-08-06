# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import scipy.io as sio
from pylab import *

m1 = np.matrix([
    # y7 y9  y11     y12 y13 y14
    [    1., 2., 1 / 3., 2., 2., 2.],
    [1 / 2., 1., 1 / 5., 1., 1., 1.],
    [    3., 5.,     1., 5., 5., 5.],
    [1 / 2., 1., 1 / 5., 1., 1., 1.],
    [1 / 2., 1., 1 / 5., 1., 1., 1.],
    [1 / 2., 1., 1 / 5., 1., 1., 1.]
])

m2 = np.matrix([
    [1., 1 / 3., 1 / 2., 1 / 5., 1 / 6., 1 / 2., 1 / 4., 1 / 2.],
    [3.,     1.,     2., 1 / 3., 1 / 4.,     2., 1 / 2.,     2.],
    [2., 1 / 2.,     1., 1 / 4., 1 / 5.,     1., 1 / 2.,     1.],
    [5.,     3.,     4.,     1., 1 / 2.,     4.,     2.,     4.],
    [6.,     4.,     5.,     2.,     1.,     5.,     3.,     5.],
    [2., 1 / 2.,     1., 1 / 4., 1 / 5.,     1., 1 / 2.,     1.],
    [4.,     2.,     2., 1 / 2., 1 / 3.,     2.,     1.,     2.],
    [2., 1 / 2.,     1., 1 / 4., 1 / 5.,     1., 1 / 2.,     1.]
])

m3 = np.matrix([
    [  1., 3.],
    [1/3., 1.],
])

for m in [m1, m2, m3]:
    print(m.shape)
    for i in xrange(m.shape[0]):
        for j in xrange(m.shape[1]):
            if m[i, j] != 1 / m[j, i]:
                print('列', i + 1, '行', j + 1, '\n', m[i, j])


sio.savemat('AHP_matrix.mat', dict(m1=m1, m2=m2, m3=m3))