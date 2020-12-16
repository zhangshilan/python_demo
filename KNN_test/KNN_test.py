# -*- codeing = utf-8 -*-
#@Time :2020/12/16 11:11
#@Author :张士澜
#@File :KNN_test.py
#@Software :PyCharm

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from mpl_toolkits.mplot3d import Axes3D

iris = load_iris()
x = iris.data
y = iris.target
k_range = range(1,31)
k_error = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,x,y,cv=5,scoring='accuracy')
    #5:1划分训练集和验证集，进行交叉验证得出评估分数
    #print("%d:%s" % (k,scores))
    k_error.append(1-scores.mean())

#plt.plot(k_range,k_error)
#plt.xlabel('Value of K for KNN')
#plt.ylabel('Error')
#plt.show()
'''
上述代码求出不同k取值对误差的影响
'''
K = {num:i for i,num in enumerate(k_error)}[min(k_error)]
#print(n_neighbors)
#将k_error中最小值的下标取出，将它作为K（代码参考Leecode:Two Sum）
figure = plt.figure().add_subplot(projection='3d')
figure.scatter(x[:,0],x[:,1],x[:,2],c=y)
figure.set_xlabel("1st eigenvector")
figure.set_ylabel("2nd eigenvector")
figure.set_zlabel("3rd eigenvector")
#三维图形绘制
clf = KNeighborsClassifier(n_neighbors = K)

X = x[:,:3]
clf.fit(X,y)

point = [[7.1,3,4]]

answer = clf.predict(point)
figure.scatter(point[0][0],point[0][1],point[0][2],c = 'r')
print("结果是：%d" % answer)
plt.show()
#预测输入点，并且输出结果
