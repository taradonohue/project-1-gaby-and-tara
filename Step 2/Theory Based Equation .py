import numpy as np
import matplotlib.pyplot as plt
list1 = [10.0,12.0,14.0,16.0,18.0]
array1=np.array(list1)
def period(array) :
    n = len(array1)
    for i in range(n):
      T = (2* np.pi) * np.sqrt(array[i]/9.81)
      array[i] = T
    return array 
print(period(array1))

x = list1
y = array1
plt.scatter(x, y,)
plt.title('Estimated Period of Pendulum')
plt.xlabel('Length (in)')
plt.ylabel('Period (s)')
plt.show()