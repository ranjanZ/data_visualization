import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import style




X1=[1,2,3,4,5]
Y1=[2,3,5,7,8]
X2=[1,2,3,4,5]
Y2=[2,3,5,7,8]

plt.bar(X1,Y1,color="r")
plt.bar(X2,Y2,color="b")




plt.title("BAR")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

