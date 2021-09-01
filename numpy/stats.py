import numpy as np

x = np.arange(1,11)
print (x.size)
print (sum(x))
xmean = sum(x)/x.size
print (xmean)
print (np.mean(x))
print (np.var(x))
#axis 0 column wise
#axis 1 row wise
print (np.std(x))
print (np.median(x))
