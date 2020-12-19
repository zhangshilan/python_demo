# -*- codeing = utf-8 -*-
#@Time :2020/12/16 11:11
#@Author :张士澜
#@File :KNN_test.py
#@Software :PyCharm

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd
import mglearn
import matplotlib.pyplot as plt
import numpy as np
from KNN import KNN

if __name__ == '__main__':
    iris = load_iris()

    # 从使用train_test_split，利用随机种子random_state采样25%的数据作为测试集。
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2,random_state=0)
    iris_dataframe = pd.DataFrame(X_train, columns=iris.feature_names)
    # 按y_train着色
    grr = pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15), marker='o',
                                     hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
    # plt.show()

    x_train = (X_train - np.min(X_train,axis = 0)) / (np.max(X_train,axis = 0)) - np.min(X_train,axis = 0)
    x_test = (X_test - np.min(X_test, axis=0)) / (np.max(X_test, axis=0)) - np.min(X_test, axis=0)

    clf = KNN(k = 5)
    clf.fit(x_train,y_train)
    y_train_pred = clf.predict(x_train)
    print('train accuracy : {:.3}'.format(clf.score(y_train,y_train_pred)))
    y_test_pred = clf.predict(x_test)
    # print(y_test_pred)
    # print(y_test)
    print('test accuracy : {:.3}'.format(clf.score(y_test,y_test_pred)))

