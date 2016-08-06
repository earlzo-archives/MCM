# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function

import os

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

data_dir = r'D:\Documents\工作存档\数学建模\2016美赛\ProblemCDATA'

# 候选学校名单
candidate_schools = pd.read_excel(
    os.path.join(data_dir, r'Problem C - IPEDS UID for Potential Candidate Schools.xlsx'),
    index_col=0,
)

stabbr = candidate_schools.groupby('STABBR').size()


scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'], \
       [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

data = [dict(
    # zmax='',
    # uid='',
    # stream='',
    # zsrc='',
    # text='',
    # zmin='',
    locations=stabbr.index,
    # textsrc='',
    visible=True,
    marker=dict(
        line=dict(
            color='rgb(255,255,255)',
            width=2
        )
    ),
    # reversescale='',
    showlegend=False,
    type='choropleth',
    # opacity='',
    # locationssrc='',
    # legendgroup='',
    autocolorscale=False,
    showscale=True,
    colorscale=scl,
    # hoverinfo='',
    # zauto=True,
    # colorbar=dict(title='Number of Potential Candidate School'),
    z=stabbr,
    locationmode='USA-states'
)]

layout = dict(
    # title='Number of Potential Candidate School',
    geo=dict(
        scope='usa',
        projection=dict(type='albers usa'),
        showlakes=True,
        lakecolor='rgb(255, 255, 255)',
    ),
)

fig = dict(data=data, layout=layout)
py.plot(fig)