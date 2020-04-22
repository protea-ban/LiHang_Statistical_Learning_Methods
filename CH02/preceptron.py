import numpy as np
import matplotlib.pyplot as plt


class MyPerceptron:
    def __init__(self):
        # 初始化w b为0，w是向量，所以是None
        self.w = None
        self.b = 0
        self.l_rate = 1

    def fit(self, X_train, y_train):
        # 用样本点的特征数更新初始w
        self.w = np.zeros(X_train.shape[1])
        i = 0
        # 样本点从下标0开始
        while i < X_train.shape[0]:
            X = X_train[i]
            y = y_train[i]
            # 如果y*(wx+b)<=0，样本i为误判点，更新w,b
            if y * (np.dot(self.w, X) + self.b) <= 0:
                self.w = self.w + self.l_rate * np.dot(y, X)
                self.b = self.b + self.l_rate * y
                i = 0  # 因为是误判点，所以从新开始
            else:
                i += 1


def draw(X, w, b):
    # 生产分离超平面上的两点
    X_new = np.array([[0], [6]])
    y_predict = -b - (w[0] * X_new) / w[1]
    # 绘制训练集数据的散点图
    plt.plot(X[:2, 0], X[:2, 1], "g*", label="1")
    plt.plot(X[2:, 0], X[2:, 0], "rx", label="-1")
    # 绘制分离超平面
    plt.plot(X_new, y_predict, "b-")
    # 设置两坐标轴起止值
    plt.axis([0, 6, 0, 6])
    plt.xlabel("x1")
    plt.ylabel("x2")
    # 显示图例
    plt.legend()
    # 显示图像
    plt.show()


def main():
    # 构造训练数据集
    X_train = np.array([[3, 3], [4, 3], [1, 1]])
    y_train = np.array([1, 1, -1])
    # 构建感知机对象，对数据集进行训练
    perceptron = MyPerceptron()
    perceptron.fit(X_train, y_train)
    print(perceptron.w)
    print(perceptron.b)
    # 结果图像绘制
    draw(X_train, perceptron.w, perceptron.b)


if __name__ == "__main__":
    main()
