import numpy as np

# sigmoid 函数 
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x) 
    return 1/(1+np.exp(-x))

# 输入数据集 
X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1],
            [1,1,1]])

# 输出数据集 
y = np.array([[0],
            [1],
            [1],
            [0]])

np.random.seed(1)

# 随机初始化权重并使均值为零
syn0 = 2*np.random.random((3,5)) - 1
syn1 = 2*np.random.random((5,1)) - 1

for j in range(50000):
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

#l2层
    l2_error = y - l2 
    l2_delta = l2_error*nonlin(l2,deriv=True)

#l1层 
    l1_error = l2_delta.dot(syn1.T) 
    l1_delta = l1_error * nonlin(l1,deriv=True)

# 更新权重
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)
print(l2)
