# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function

from pybrain.datasets import ClassificationDataSet
from pybrain.structure.modules import SoftmaxLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork
from pybrain.utilities import percentError
from pylab import *

# from sklearn.datasets import load_digits
from algorithm.digits_dataset import training_data_sample, training_data_target, test_data_sample, test_data_target

# digits = load_digits()

# ds = ClassificationDataSet(digits.data.shape[1], 1, 10)
ds = ClassificationDataSet(1024, 1, 10)
# map(lambda v: ds.addSample(v[0], [v[1]]), zip(digits.data, digits.target))
map(lambda v: ds.addSample(v[0], [v[1]]), zip(training_data_sample, training_data_target))

# 随机分离测试数据与训练数据，参数为测试数据比例
# tstdata, trndata = ds.splitWithProportion(0.25)
trndata = ds
tstdata = ClassificationDataSet(1024, 1, 10)
map(lambda v: tstdata.addSample(v[0], [v[1]]), zip(test_data_sample, test_data_target))

# For neural network classification,
# it is highly advisable to encode classes with one output neuron per class.
# Note that this operation duplicates the original targets and stores them in an (integer) field named ‘class’.
trndata._convertToOneOfMany()
tstdata._convertToOneOfMany()

print("Number of training patterns: ", len(trndata))
print("Input and output dimensions: ", trndata.indim, trndata.outdim)
print("First sample (input, target, class):")
print(trndata['input'][0], trndata['target'][0], trndata['class'][0])

fnn = buildNetwork(trndata.indim, np.log2(trndata.indim), trndata.outdim, outclass=SoftmaxLayer)

trainer = BackpropTrainer(fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)
# trainer = RPropMinusTrainer(fnn, dataset=trndata, momentum=0.1, verbose=True, weightdecay=0.01)
acceptable_percentError = 0.1
unacceptable = True
while unacceptable:
    # 每次训练一个阶段
    trainer.trainEpochs(1)
    trnresult = percentError(trainer.testOnClassData(),
                             trndata['class'])
    tstresult = percentError(trainer.testOnClassData(
            dataset=tstdata), tstdata['class'])

    print(
            "epoch: %4d" % trainer.totalepochs,
            "  train error: %5.2f%%" % trnresult,
            "  test error: %5.2f%%" % tstresult)
    if trnresult < acceptable_percentError:
        unacceptable = False
