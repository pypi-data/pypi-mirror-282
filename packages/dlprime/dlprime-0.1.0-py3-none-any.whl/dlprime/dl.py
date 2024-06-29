import numpy as np
from random import shuffle
import pandas as pd
from activation import sigmoid
from sklearn.metrics import log_loss
from sklearn.utils import shuffle


class Perceptron:
    def __init__(self, weights=None, bias=None, activation_func=sigmoid, loss=log_loss):
        self.weights = weights
        self.bias = bias
        self.activation_func = activation_func
        self.loss = loss

    def predict(self, X):
        y = self.activation_func(np.matmul(X, self.weights) + self.bias)
        return y

    def fit(self, X, y, learning_rate, epochs):
        if self.weights is None:
            self.weights = np.zeros(np.array(X).shape[0])
        if self.bias is None:
            self.bias = np.zeros(1)
        for epoch in range(epochs):
            total_loss = 0
            X, y = shuffle(X, y)
            for i in range(np.array(X).shape[0]):
                pred = self.predict(X[i])
                error = y[i] - pred
                X[i] = np.array(X[i]).reshape(np.array(X).shape[0], )
                self.weights += learning_rate * error * X[i] * 2
                self.bias += learning_rate * error
                total_loss += self.loss([y[i]], [pred], labels=[0, 1])

            print("Epochs: {0}, Loss: {1}".format(epoch, total_loss))

    def eval(self, X, y, metric=None):
        y_pred = self.predict(X)
        if metric is not None:
            return metric(y, y_pred)
        else:
            return self.loss(y, y_pred)
