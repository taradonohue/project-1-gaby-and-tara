import numpy as np
import math 
list1 = [10,12,14,16,18]
array1=np.array(list1)
def period(array) :
    n = len(array1)
    for i in range(n):
      T = (2* math.pi) * math.sqrt(array[i]/9.81)
      array[i] = T
      #np.append(array, T)
   #   return array 
    return array 
print(period(array1))