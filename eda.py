import pandas as pd

df = pd.read_csv("House price ai.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print(df.describe())
