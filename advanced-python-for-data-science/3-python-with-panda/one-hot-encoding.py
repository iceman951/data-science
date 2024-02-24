import pandas as pd

df = pd.DataFrame({'country': ['China', 'India', 'USA', 'Indonesia', 'Brazil']})
print(df)
aa = pd.get_dummies(df, prefix=['country'])
print(aa)