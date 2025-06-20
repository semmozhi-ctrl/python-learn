
import matplotlib.pyplot as plt
import numpy as np

x = np.array([3, 8, 1, 10])
y = np.array([6, 2, 7, 11])

plt.plot(x,marker='o',color='blue',linestyle='--',linewidth=2,markersize=10)
plt.plot(y,marker='s',color='red',linestyle='-',linewidth=2,markersize=10)
plt.xlabel( "food")
plt.ylabel( "water")
plt.grid(color='black',linestyle='-',linewidth=0.5)
plt.title('food vs water')
plt.legend(['food','water'],loc='upper left')
plt.bar(x,y)
plt.scatter(x,y)



x = np.random.normal(170, 10, 250)

plt.hist(x)


plt.show()