import pandas as pd

province = pd.Series(["Chaing Mai", "Lampang", "Bangkok"])
population = pd.Series([100000, 200000, 300000])

pv = pd.DataFrame({ "Province": province, "Population": population })

pp = pv["Population"] / 1000

print(pp)

cc = pd.Series([50, 20, 30])
ee = pp + cc
print(ee)