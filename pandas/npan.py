import pandas as pd
import numpy as np

DF = np.array ([[1,2,3],[4,5,6],[7,8,9]])
data_set = pd.DataFrame(DF,index = [1,2,3],columns=['age','grade','no'])
data_set["yes"] = [9,6,7]
# print (data_set)
#tracking loc and iloc

# print (data_set.loc[1])
# print (data_set.iloc[0][0])
# print (data_set["yes"][2])
# print (data_set["yes"][:])
print (data_set.iloc[:,2])
data_set=data_set.drop("yes",axis=1)
data_set =data_set.replace({1:100,6:5})
print (data_set.head())
data_set = data_set.sort_values('age',ascending=True)
data_set = data_set.sort_index(axis=0,ascending=True)
print (data_set.head())
