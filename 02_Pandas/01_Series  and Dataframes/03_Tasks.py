#Task 01
#Create a Series of 5 numbers
import pandas as pd
df = pd.Series([10,20,30,40,50])
print(df)
#Task 02
#DataFrame Creation
data={
    "Name":["Manoj","Shriniwas","Sonu"],
    "Age":[25,50,19],
    "Score":[56,89,90]
}
dff=pd.DataFrame(data)
print(dff)
#Task 3 — Selection
#Print only Age column
print(dff["Age"])
#Print first row
print(dff.loc[0])
#Print last 2 rows
print(dff.loc[[1,2]])

# Task04 Filtering
