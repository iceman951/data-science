import pandas as pd
import numpy as np
from numpy import nan as NA

data = pd.DataFrame([1,6.5,NA])
cleaned = data.dropna()
print(cleaned)