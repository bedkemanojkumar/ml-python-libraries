#  Create a series
import pandas as pd
s=pd.Series([10,20,30,40])
print(s)
# custom Index/Labels
sm = pd.Series([10,20,30], index=['a','b','c'])
print(sm)
# Access the data
print(s[0])
print(sm['b'])
# Key/Value objects as series
calories={'day1':420,'day2':390,'day3':450}
myvar=pd.Series(calories)
print(myvar)

