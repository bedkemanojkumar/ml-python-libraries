import pandas as pd

# Creating dataframes from series

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)


print(df)
# locate a row/rows
print(df.loc[0])
print(df.loc[[0,1]])

# Naming indices
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
dff = pd.DataFrame(data,index=["Day1","Day2","Day3"])
print(dff)
# Locating named indexes
print(dff.loc["Day2"])
