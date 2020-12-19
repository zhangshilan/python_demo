# -*- codeing = utf-8 -*-
#@Time :2020/12/19 16:04
#@Author :张士澜
#@File :KNN.py
#@Software :PyCharm

import numpy as np
import operator

class KNN(object):

    def __init__(self,k = 3):
        self.k = k

    def fit(self,x,y):
        self.x = x
        self.y = y

    def _square_distance(self,v1,v2):
        return np.sum(np.square(v1-v2))

    def _vote(self,ys):
        ys_unique = np.unique(ys)
        vote_dic = {}
        for y in ys:
            if y not in vote_dic.keys():
                vote_dic[y] = 1
            else:
                vote_dic[y] += 1
        sorted_vote_dict = sorted(vote_dic.items(),key = operator.itemgetter(1),reverse = True)
        return sorted_vote_dict[0][0]

    def predict(self,x):
        y_pred = []
        for i in range(len(x)):
            dist_arr = [self._square_distance(x[i],self.x[j]) for j in range(len(self.x))]
            sorted_index = np.argsort(dist_arr)
            top_k_index = sorted_index[:self.k]
            y_pred.append(self._vote(ys = self.y[top_k_index]))
        return np.array(y_pred)

    def score(self,y_ture = None,y_pred = None):
        if y_ture is None or y_pred is None:
            pred = self.predict(self.x)
            y_ture = self.y
        score = 0.0
        for i in range(len(y_ture)):
            if y_ture[i] == y_pred[i]:
                score += 1
        score /= len(y_ture)
        return score