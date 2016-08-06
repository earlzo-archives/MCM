# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import numpy as np
import os
from string import whitespace

base_dir = os.path.dirname(__file__)


def load_data(path):
    """
    载入训练数据或者测试数据
    :param path: 数据文件夹路径
    :return: 分离好的输入输出数据
    """
    path = os.path.join(base_dir, path)
    files = os.listdir(path)
    x_axis = []
    y_axis = []
    for filename in files:
        file_path = os.path.join(path, filename)
        fp = open(file_path, 'rb')
        x = map(int, fp.read().translate(None, whitespace))
        # print(x)
        x = np.array(x)
        x_axis.append(x)
        y_axis.append(int(filename[0]))
    return np.array(x_axis, np.float), np.array(y_axis, np.float)


training_data_sample, training_data_target = load_data('testDigits')
test_data_sample, test_data_target = load_data('trainingDigits')


def convert_target_for_matlab(target):
    u = np.unique(target).tolist()
    nda = np.zeros((len(u), len(target)), np.bool)
    for i, v in enumerate(target):
        nda[u.index(v), i] = True
    print(nda, '\n', nda.shape)
    return nda


if __name__ == '__main__':
    import scipy.io as sio

    sio.savemat('didits.mat', {'training_data_sample': training_data_sample.T,
                               'training_data_target': convert_target_for_matlab(training_data_target),
                               'test_data_sample': test_data_sample.T,
                               'test_data_target': convert_target_for_matlab(test_data_target)})
