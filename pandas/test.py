import pandas as pd

Age = pd.Series([10,20,30,40],index=["age1","age2","age3","age4"])
print(Age[0])

filtered_age = Age[Age>20]
print (filtered_age)
print(Age.values)
print(Age.index)

