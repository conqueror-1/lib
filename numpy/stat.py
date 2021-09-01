import numpy as np

def print_array (arr : np.array):

    row,col = arr.shape
    
    for r in range (row):
        for c in range (col):
            print (arr[r][c],end=" ")
        print()

ND = np.random.standard_normal((3,4))
UD = np.random.uniform(1,12,(3,4))

ri = np.random.randint(1,50,(2,2))

ze = np.zeros((3,4))
ones = np.ones((3,4))

filter_ND = np.logical_and(ri>30,ri<50)

print_array(filter_ND)
