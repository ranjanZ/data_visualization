import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import style




X=[12,2,7,4,5]
Y=["X1","X2","X3","X4","X5"]
C=['r','k','b','m','y']


plt.pie(X,labels=Y,colors=C)
#plt.pie(X,labels=Y,colors=C,shadow=True,explode=[0,0.2,0,0,0],autopct='%1.1f%%")
plt.show()





