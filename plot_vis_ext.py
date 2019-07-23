import numpy as np
import matplotlib.pyplot as plt
from  matplotlib import style



style.use("ggplot")
X=[1,2,3,4,5]
Y=[2,3,5,7,8]



plt.plot(X,Y,label="line1",color="r",linewidth=5)
plt.grid(True,color="k")






plt.title("Time vs temp")
plt.xlabel("Time")
plt.ylabel("Temp")
plt.show()

