import numpy as np

# sigmoid 函数
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

# 输入数据集
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])

# 输出数据集            
y = np.array([[0,0,1,1]]).T

np.random.seed(1)

# 随机初始化权重并使均值为零
syn0 = 2*np.random.random((3,1)) - 1

for i in range(10000):
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))

#误差
    l1_error = y - l1

    l1_delta = l1_error * nonlin(l1,True)

# 更新权重
    syn0 += np.dot(l0.T,l1_delta)
print (l1)
