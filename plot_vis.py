import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import style




X=[1,2,3,4,5]
Y=[2,3,5,7,8]
plt.plot(X,Y,label="line1")

Y1=[5,7,9,65,23]


plt.plot(X,Y1,color="k",label="line2")



plt.title("Time vs temp")
plt.xlabel("Time")
plt.ylabel("Temp")

plt.show()
