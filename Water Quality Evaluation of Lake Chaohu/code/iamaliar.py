# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
from pylab import *
from scipy import io as sio

case_num = 200
# mg/L
# 1.5-2.5
# 2.0-3
TN = np.random.normal(2.3, 0.8, case_num)

# 0.10-0.22
# 0.1-0.3
TP = np.random.normal(0.17, 0.07, case_num)

# 10-25
NP = TN / TP
np_scale = np.logical_and(9 <= NP, NP <= 26)
TN = TN[np_scale]
TP = TP[np_scale]

NP = TN / TP

Chl_a = -0.0012 + 0.0064 * TN + 0.0215 * TP + 0.0005 * NP
Chl_a_len = len(Chl_a)

error_percent = 0.3
bias_index = np.unique(np.random.choice(np.arange(Chl_a_len), int(error_percent * Chl_a_len)))

bias = (-2 * np.random.random(len(bias_index)) + 1) * error_percent * (np.max(Chl_a) - np.min(Chl_a))


def _apply_bias(index, bias):
    print(Chl_a[index], '-->', end=' ')
    Chl_a[index] += bias
    print(Chl_a[index])


map(_apply_bias, bias_index, bias)
map(lambda v: print('%.2f %.2f %.2f %.2f' % (v[0], v[1], v[2], v[3])), zip(TN, TP, NP, Chl_a))
print('Len: %d' % len(Chl_a))
sio.savemat('TN-TP-NP', {'x': np.asmatrix([TN, TP]), 't': Chl_a})
