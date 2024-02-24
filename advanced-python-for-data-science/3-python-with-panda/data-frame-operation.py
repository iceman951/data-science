import pandas as pd
import numpy as np
from numpy import nan as NA

cc = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
# print(cc.describe())

dd = cc.sort_index()
print(dd)

# set data
data = pd.DataFrame([1,6.5,NA])

# cleaning data
cleaned = data.dropna()
print(cleaned)

# fillna
filled = data.fillna(data.mean())
print(filled)

#statistic operation
a = data.min()
b = data.max()
c = data.sum()
d = data.mean()
e = data.median()
print(a)
print(b)
print(c)
print(d)
print(e)
