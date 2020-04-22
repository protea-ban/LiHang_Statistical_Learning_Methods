# -*- coding: utf-8 -*-
from sklearn.linear_model import Perceptron
import numpy as np

# 构造训练数据集
X_train = np.array([[3, 3], [4, 3], [1, 1]])
y = np.array([1, 1, -1])

perceptron = Perceptron()
# perceptron=Perceptron(penalty="l2",alpha=0.01,eta0=1,max_iter=50,tol=1e-3)
perceptron.fit(X_train, y)
# 查看训练后感知机的各个参数
print(
    "w:", perceptron.coef_, "\n", "b:", perceptron.intercept_,
)

res = perceptron.score(X_train, y)
print("correct rate:{:.0%}".format(res))
