#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:28:35 2020

@author: gackermannlogan
"""

import os
import numpy as np 
import matplotlib.pyplot as plt
path = "/Users/gackermannlogan/mu_code/data_capture/"
os.chdir(path)
print(os.getcwd())
fin = open("12inch-Trial.csv", "r")

array = (np.genfromtxt(fin, delimiter = ","))
x = np.array(array[708:998,0])
y = np.array(array[708:998,1])
z = np.array(array[708:998,2])
time = np.array(array[708:998,3])

plt.plot(time, x)
plt.plot(time, y)
plt.plot(time, z)
plt.legend("x" "y" "z")
plt.title("Acceleration v. Time")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.show()