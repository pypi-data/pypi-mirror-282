import numpy as np
import pandas as pd


class Matrix:
    def __init__(self, data, index=None, columns=None):
        self.data = pd.DataFrame(data)
        self.data.columns = columns
        if index is None:
            self.index = index
        if index is not None:
            self.index = np.arange(0, len(data.keys))

    def head(self, num):
        return pd.DataFrame(self.data).iloc[:num, :]

    def tail(self, num):
        return pd.DataFrame(self.data)[num:, :]

    def delete(self, index, axis=0):
        self.data.drop(index, axis=axis, inplace=True)
        return self.data

    def fill_nan(self, value):
        self.data.replace({np.nan: value}, inplace=True)
        return self.data

    def change_col_name(self, new_col_names):
        self.data.columns = new_col_names
        return self.data
