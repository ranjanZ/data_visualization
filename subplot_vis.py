import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import style



#np.arange(0,10,0.1)
X1=[1,2,3,4,5]
Y1=[2,3,5,7,8]

plt.subplot(211)
plt.plot(X1,Y1)


plt.subplot(212)
plt.plot(X1,Y1)


plt.title("Time vs temp")
plt.xlabel("Time")
plt.ylabel("Temp")

plt.show()


