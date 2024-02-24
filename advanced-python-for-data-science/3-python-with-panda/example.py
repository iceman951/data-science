import pandas as pd
import numpy as np

# step 1
name = pd.Series(["Sarawut Ramjan", "Jirapon Sunkpho", "Kom Campiranon", "Pan Pongpanarat", "Chayakrit A."])
position = pd.Series(["Lecturer", "Lecturer", "Lecturer", "Lecturer", "Lecturer"])
income = pd.Series([1100, 2000, 1000, 1000, 1000])

income = income + 50

# step 2
data = pd.DataFrame({ "Name": name, "Position": position, "Income": income })
data = data.sort_values(by="Income")
print(data)

# step 3
min = data["Income"].min()
max = data["Income"].max()
print(min)
print(max)

# step 4
colors = pd.Series(["red", "red", "yellow", "green", "blue", "pink"])
new = pd.get_dummies(colors)
print(new)