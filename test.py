import numpy as np
import math
x = [9,7,4,6]
y = [5,4,2,3]
xsum = np.sum(x)
ysum = np.sum(y)
Sxx = np.dot(x, x) - (xsum**2)/len(x)
Syy = np.dot(y, y) - (ysum**2)/len(y)
Sxy = np.dot(x,y) - (xsum * ysum)/len(x)
Cxy = Sxy/(len(x)-1)
rxy = Sxy/math.sqrt(Sxx*Syy)
print("偏差積和は"+str(Sxy))
print("共分散"+str(Cxy))
print("相関係数"+str(rxy))