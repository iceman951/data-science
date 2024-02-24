import pandas as pd
a = pd.Series(["San Francisco", "San Jose", "Sacramento"])
b = pd.Series([852469, 1015785, 485199])

c = pd.DataFrame({ "City name": a, "Population": b })

print(c)