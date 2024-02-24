import pandas as pd

data = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")
print(data.describe())