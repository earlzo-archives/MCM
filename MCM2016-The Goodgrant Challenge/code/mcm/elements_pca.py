# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import os
import pandas as pd
import scipy.io as sio
import seaborn as sns
from pylab import plt, np
from sklearn.cross_validation import cross_val_score
from sklearn.decomposition import PCA

from mcm import data_dir, report_dir

# 评价数据
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

print(number_elements.shape)

# 填充空白值
X = number_elements.fillna(number_elements.mean())
# pca = PCA(10)
# pca.fit(number_elements.keys(), number_elements)
# n_components = np.arange(0, len(X.keys()))
#
#
# def compute_scores(X):
#     pca = PCA()
#     pca_scores = []
#     for n in n_components:
#         pca.n_components = n
#         pca_scores.append(np.mean(cross_val_score(pca, X)))
#
#     return pca_scores
#
#
# pca_scores = compute_scores(X)
#
# plt.plot(n_components, pca_scores, label='PCA scores')
#
# n_components_pca = n_components[np.argmax(pca_scores)]
#
# plt.axvline(n_components_pca, color='b', label='PCA CV: %d' % n_components_pca, linestyle='--')
# plt.xlabel('nb of components')
# plt.ylabel('CV scores')
# plt.legend(loc='lower right')
# plt.title('Noise')
# plt.show()

sio.savemat('number_elements.mat', dict(X=X.values))
