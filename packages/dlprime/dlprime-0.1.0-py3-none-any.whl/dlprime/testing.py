import numpy as np

from dl import Perceptron
from activation import sigmoid
from sklearn.metrics import log_loss, r2_score
from data import Matrix
import pandas as pd

X = [[-2, 1, 3, 0], [4, 3, 0, -2], [2, 1, 1, -2], [-3, 3, 3, 2]]
y = [0, 1, 1, 0]

pct = Perceptron(activation_func=sigmoid, loss=log_loss)

print(pct.fit(X, y, learning_rate=0.1, epochs=100))
print(pct.eval(X, y, metric=r2_score))

dictionary = {1: [1, 2, 3, np.NAN], 2: [2, 3, 4, 5], 3: [3, 4, 5, 6]}
mat = Matrix(dictionary, columns=[1, 2, 3])
print(mat.fill_nan(2))
mat.delete(1, axis=1)
mat.change_col_name(["a", "b"])
print(mat.data)