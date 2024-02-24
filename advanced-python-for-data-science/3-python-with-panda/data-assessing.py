import pandas as pd

province = pd.Series(["Chaing Mai", "Lampang", "Bangkok"])
population = pd.Series([100000, 200000, 300000])

pv = pd.DataFrame({ "Province": province, "Population": population })

a = pv["Province"][2]
b = pv[1:3]

print(a)
print(b)