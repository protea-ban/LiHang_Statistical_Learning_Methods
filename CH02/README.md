

# 感知机模型

对于下面题目，分别用自编程和 sklearn 库实现。

> 已知训练数据集D，其正实例点是x1=(3,3)T,x2=(4,3)T，负实例点是x3=(1,1)T:
>
>(1) 用python 自编程实现感知机模型，对训练数据集进行分类，并对比误分类点选择次序不同对最终结果的影响。可采用函数式编程或面向对象的编程。
>
>(2)试调用sklearn.linear_model 的Perceptron模块，对训练数据集进行分类，并对比不同学习率h对模型学习速度及结果的影响。

### 自编程

参考preceptron.py

### sklearn调参

参考skl_preceptron.py

属性-变量

| 属性        | 含义     |
| ----------- | -------- |
| coef_(权重) | 对应w    |
| intercept_  | 对应b    |
| n_iter_     | 迭代次数 |



方法-函数

| 方法  | 用处             |
| ----- | ---------------- |
| fit   | 用于训练数据集   |
| score | 用来评价训练效果 |

模型训练参数

|参数|默认值|可选值|
|-|-|-|
|penalty（正则化项）|None|'l1'or'l2'or'elasticnet'|
|alpha（正则化系数）|0.0001||
|eta0（学习率）|1|(0,1]|
|max_iter（迭代次数）|5|如果tol不为None则为1000|
|tol（终止条件）|None|(previous_loss)<tol|

Q1:学习率对迭代过程和最终结果有无影响？
Q2:无影响的条件是什么？
A：无影响，条件是 W、b 的初始值均为 0 。当二者初始值为 0 时，二者值的更新都是学习率的倍数。

Q3:L1 L2 分别有什么作用？
A: L1 使特征值更稀疏，L2 使 权值更均匀。

Q4:正则化洗漱对正则化有何影响？
A: 过小无约束效力，过大则约束的太狠。

GitHub地址：https://github.com/protea-ban/LiHang_Statistical_Learning_Methods

![](https://raw.githubusercontent.com/protea-ban/images/master/PythonStudyTogether.png)