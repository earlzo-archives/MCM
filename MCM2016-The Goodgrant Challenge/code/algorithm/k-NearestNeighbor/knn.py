# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function

import hashlib
import re

from pylab import *
from sklearn import neighbors, metrics, learning_curve
from sklearn.externals import joblib

from algorithm.digits_dataset import *


# 模型持久化
def load_model(model_file_name, base_dir='saved_model'):
    if os.path.exists(os.path.join(base_dir, model_file_name)):
        return joblib.load(model_file_name)
    return None


def dump_model(model, base_dir='saved_model', model_dir=None, description=''):
    """
    模型持久化，根据模型类名和参数的md5值建立文件夹
    :param model: 模型对象
    :param base_dir: 模型储存路径
    :param model_dir: 模型储存的文件夹
    :param description: description.txt 中的额外内容
    :return: 储存的模型文件的路径
    """
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    param_hash = hashlib.md5(pickle.dumps(model.get_params())).hexdigest()
    model_class_name = re.search(r"(?<=\.)(\w*)(?='>)", unicode(type(model))).group()
    model_dir = model_dir or os.path.join(base_dir, ''.join([model_class_name, '_', param_hash]))
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)
    full_path = os.path.join(model_dir, model_class_name)

    joblib.dump(model, full_path)
    with open(os.path.join(model_dir, 'description.txt'), 'wb') as description_fp:
        description_fp.writelines((unicode(model), '\n\n', description))
    return full_path


def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):
    """
    Generate a simple plot of the test and traning learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : integer, cross-validation generator, optional
        If an integer is passed, it is the number of folds (defaults to 3).
        Specific cross-validation objects can be passed, see
        sklearn.cross_validation module for the list of possible objects

    n_jobs : integer, optional
        Number of jobs to run in parallel (default 1).
    """
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve.learning_curve(
            estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt


if __name__ == '__main__':
    X, y = training_data_sample, training_data_target
    tX, ty = test_data_sample, test_data_target

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X, y)
    # 模型评价报告
    report = metrics.classification_report(ty, clf.predict(tX))
    print(report)

    print(clf.get_params())
    print(dump_model(clf, description=report))
    # 学习曲线
    plot_learning_curve(clf, 'Learning Curve', X, y).show()
    # train_sizes, train_scores, valid_scores = learning_curve.learning_curve(clf, X, y)
    # train_scores, valid_scores = learning_curve.validation_curve(clf)

