# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
from pprint import pprint

import pandas as pd
import scipy.io as sio
import pandas as pd
from pylab import *

from mcm import report_dir

important_elemens_index = [
    'UGDS',
    'PPTUG_EF',
    'RET_FT4',
    'RET_FTL4',
    'RET_PT4',
    'RET_PTL4',
    'PCTFLOAN',
    'UG25abv',
    'GRAD_DEBT_MDN_SUPP',
    'GRAD_DEBT_MDN10YR_SUPP',
    'RPY_3YR_RT_SUPP',
    'C150_4_POOLED_SUPP',
    'C200_L4_POOLED_SUPP',
    'md_earn_wne_p10',
    'gt_25k_p6',
    'PCTPELL'
]

# 数值数据
number_elements = pd.read_csv(
    os.path.join(report_dir, r'NumberElements.csv'),
    skipinitialspace=True,
    index_col=0,
    na_values=['NULL', 'PrivacySuppressed'],
    # usecols=[
    #     0,  # UNITID
    #     3,  # INSTNM
    #     4,  # CITY
    #     5,  # STABBR
    #
    # ]
    dtype={
        'UNITID': np.int
    }
)

important_elemens = number_elements[important_elemens_index]
# print(important_elemens.describe())
important_elemens.to_excel(os.path.join(report_dir, 'important_elements.xls'))
# 填充空白值
X = important_elemens.fillna(important_elemens.mean())
print(X.describe())
pprint(X.keys().tolist())
sio.savemat('important_elements.mat', dict(X=X.values))
