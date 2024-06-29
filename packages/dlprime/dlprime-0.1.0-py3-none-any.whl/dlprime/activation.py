import numpy as np


# relu
def relu(X):
    new_X = [max(0, x) for x in X]
    return new_X


# leaky_relu
def leaky_relu(X):
    new_X = [max(0.1*x, x) for x in X]
    return new_X


# sigmoid
def sigmoid(X):
    new_X = 1 / (1+np.exp(-X))
    return new_X


# softmax
def softmax(X):
    new_X = np.exp(X) / sum(np.exp(X))
    return new_X
