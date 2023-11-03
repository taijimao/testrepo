import pandas as pd
filepath = "C:/Users/Downloads/titanic.txt"
df = pd.read_csv(filepath)
df.head()
df.dtypes