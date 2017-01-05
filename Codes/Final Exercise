import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt

class parameters:
    nn_input_dim = 2  # 输入层结点数
    nn_output_dim = 2  # 输出层结点数
    # 梯度下降法参数
    epsilon = 0.02  # 梯度下降学习速率
    reg_lambda = 0.02  # 正则化强度

def generate_data():
    np.random.seed(0)
    X, y = datasets.make_moons(200, noise=0.20)
    return X, y

def visualize(X, y, model):
    plot_decision_boundary(lambda x:predict(model,x), X, y)
    plt.title("distinguish datas")

def plot_decision_boundary(pred_func, X, y):
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # 格点间距h
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # 预测值
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # 画分割线
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.show()

    # sigmoid 函数 
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x) 
    return 1/(1+np.exp(-x))
    
def calculate_loss(model, X, y):
    num_examples = len(X)  # 训练集大小
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # 前向传播
    z1 = X.dot(W1) + b1
    a1 = nonlin(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    # 计算误差
    corect_logprobs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(corect_logprobs)
    
    data_loss += parameters.reg_lambda / 2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1. / num_examples * data_loss

def predict(model, x):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    # 前向传播
    z1 = x.dot(W1) + b1
    a1 = nonlin(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return np.argmax(probs, axis=1)

# - nn_hdim: 隐藏层结点数
# - num_passes: 通过梯度下降的训练数目
def build_model(X, y, nn_hdim, num_passes=20000):
    # 初始化 
    num_examples = len(X)
    np.random.seed(0)
    W1 = np.random.randn(parameters.nn_input_dim, nn_hdim) / np.sqrt(parameters.nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, parameters.nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, parameters.nn_output_dim))

    model = {}

    #梯度下降
    for i in range(0, num_passes):

        # 前向传播
        z1 = X.dot(W1) + b1
        a1 = nonlin(z1)
        z2 = a1.dot(W2) + b2
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

        # 后向传播
        delta3 = probs
        delta3[range(num_examples), y] -= 1
        dW2 = (a1.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)
        delta2 = delta3.dot(W2.T) * nonlin(a1,deriv=True)
        dW1 = np.dot(X.T, delta2)
        db1 = np.sum(delta2, axis=0)

        dW2 += parameters.reg_lambda * W2
        dW1 += parameters.reg_lambda * W1

        # 更新梯度下降参数
        W1 += -parameters.epsilon * dW1
        b1 += -parameters.epsilon * db1
        W2 += -parameters.epsilon * dW2
        b2 += -parameters.epsilon * db2

        # 更新
        model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}        
    return model

def main():
    X, y = generate_data()
    model = build_model(X, y, 3)
    visualize(X, y, model)

main()
