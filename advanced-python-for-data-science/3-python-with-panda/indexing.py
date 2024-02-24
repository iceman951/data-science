import pandas as pd

cc = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
print(cc.describe())

f = cc["median_income"]
print(f)