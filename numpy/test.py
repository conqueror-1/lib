import numpy as np

def print_array (arr : np.array):

    row,col = arr.shape
    
    for r in range (row):
        for c in range (col):
            print (arr[r][c],end=" ")
        print()


x = np.array([[1,2],[4,6]])
y = np.array([[1,2],[4,6]])
z = np.array([[1,2,3],[4,6,7]])

# print (x.ndim)
# print (x.size / x.ndim)

mmp = x @ y
mmp2 = x.dot(y)
mmp3 = np.multiply(x,y)

print_array(mmp2)
# print_array(mmp3)
# print_array(mmp)

print (x.shape)
tot_sum = np.sum(x)
print (tot_sum)

