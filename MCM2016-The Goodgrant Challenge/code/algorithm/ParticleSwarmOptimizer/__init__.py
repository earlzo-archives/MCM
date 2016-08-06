# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
from pylab import *
from pybrain.optimization.populationbased.pso import ParticleSwarmOptimizer, Particle

cities = array([(37, 52), (49, 49), (52, 64), (20, 26), (40, 30), (21, 47), (17, 63), (31, 62), (52, 33), (51, 21),
                (42, 41), (31, 32), (5, 25), (12, 42), (36, 16), (52, 41), (27, 23), (17, 33), (13, 13), (57, 58),
                (62, 42), (42, 57), (16, 57), (8, 52), (7, 38), (27, 68), (30, 48), (43, 67), (58, 48), (58, 27)])

city_num = len(cities)
city_code = arange(city_num)


def fitness(c):
    city = cities[c]
    return sum([((cities[i][0] - city[0]) ** 2 + (cities[i][1] - city[1]) ** 2) ** 0.5 for i in city_code])


# simple function
sf = lambda x: x ** 2
xlist2 = list(xrange(-10, 10))
pso = ParticleSwarmOptimizer(sf, xlist2, verbose=True,
                             size=10,  # 粒子数
                             boundaries='',  # 每个变量的范围
                             # how much the velocity of a particle is affected by its previous best position
                             # memory=[(),],
                             # how much the velocity of a particle is affected by its neighbours best position
                             # sociality=1,
                             inertia=''
                             )
print(pso.bestEvaluable)
print(pso.bestEvaluation)
print(pso.best(xlist2))
