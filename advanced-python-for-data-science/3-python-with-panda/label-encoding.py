import pandas as pd

data = pd.DataFrame(["poor", "fair", "good"])
print(data)

cleanup = { "poor": 1, "fair": 2, "good": 3 }
aa = data.replace(cleanup)
print(aa)