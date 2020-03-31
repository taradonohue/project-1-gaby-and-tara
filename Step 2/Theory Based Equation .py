import numpy as np
import matplotlib.pyplot as plt
list1 = [0.254,0.305,0.356,0.406,0.457]
array1=np.array(list1)
def period(array) :
#This function takes an array of lengths as a parameter. It finds the theoretical period times based on the given lengths,
#and it has no return value.
    n = len(array1)
    for i in range(n):
      T = (2* np.pi) * np.sqrt(array[i]/9.81)
      array[i] = T
    return array 
print(period(array1))


#This graphs the theoretical periods versus length so the relationship between them can be found.
x = list1
y = array1
plt.scatter(x, y,)
plt.title('Estimated Period of Pendulum')
plt.xlabel('Length (m)')
plt.ylabel('Period (s)')
plt.show()
