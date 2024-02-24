import numpy as np

def abc(a, b):
    if a > b:
        return a - b
    else:
        return a + b

aa = np.vectorize(abc)
print(aa([1,2,3,4], 2))