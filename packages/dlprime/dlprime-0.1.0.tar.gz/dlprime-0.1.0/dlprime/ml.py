from activation import sigmoid
import numpy as np
import pandas as pd
from random import shuffle
from sklearn.metrics import log_loss


class LinearRegression:
    def __init__(self, weights, bias, loss):
        self.weights = weights
        self.bias = bias
        self.loss = loss

    def predict(self, X):
        y = np.matmul(X, self.weights) + self.bias
        return y

    def fit(self, X, y, learning_rate, epochs):
        if self.weights is None:
            self.weights = np.zeros(np.array(X).shape[0])
        if self.bias is None:
            self.bias = np.zeros(1)
        for epoch in range(epochs):
            total_loss = 0
            for i in range(np.array(X).shape[0]):
                shuffle(X)
                pred = self.predict(X[i])
                error = y[i] - pred
                X[i] = np.array(X[i]).reshape(np.array(X).shape[0], )
                self.weights += learning_rate * error * X[i]
                self.bias += learning_rate * error
                pd.DataFrame(X).drop(i, inplace=True)
                total_loss += self.loss([y[i]], [pred], labels=[0, 1])

            print("Epochs: {0}, Loss: {1}".format(epoch, total_loss))

    def eval(self, X, y, metric=None):
        y_pred = self.predict(X)
        if metric is not None:
            return metric(y, y_pred)
        else:
            return self.loss(y, y_pred)


class LogisticRegression:
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
            for i in range(np.array(X).shape[0]):
                shuffle(X)
                pred = self.predict(X[i])
                error = y[i] - pred
                X[i] = np.array(X[i]).reshape(np.array(X).shape[0], )
                self.weights += learning_rate * error * X[i]
                self.bias += learning_rate * error
                pd.DataFrame(X).drop(i, inplace=True)
                total_loss += self.loss([y[i]], [pred], labels=[0, 1])

            print("Epochs: {0}, Loss: {1}".format(epoch, total_loss))

    def eval(self, X, y, metric=None):
        y_pred = self.predict(X)
        if metric is not None:
            return metric(y, y_pred)