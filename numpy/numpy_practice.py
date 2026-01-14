import numpy as np
import pandas as pd
X= np.array([[20,30,40],[40,50,60],[89,98,20]])
print(X)

df = pd.DataFrame(
    X,
    columns=['R','G','B']
)
print(df)

