#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:17:44 2020

@author: gackermannlogan
"""

import os
import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig
path = "/Users/gackermannlogan/mu_code/data_capture/"
os.chdir(path)
print(os.getcwd())
fin = open("10inch-Trial.csv", "r")

x = np.array(array[960:1087,0])
y = np.array(array[960:1087,1])
z = np.array(array[960:1087,2])
time = np.array(array[960:1087,3])
x_axis = np.array(find_tilt_x(x,y,z))
y_axis = np.array(find_tilt_y(x,y,z))
z_axis = np.array(find_tilt_z(x,y,z))

filtered_x = sig.medfilt(x)
filtered_y = sig.medfilt(y)
filtered_z = sig.medfilt(z)
plt.plot(time, y)
plt.show()
plt.plot(time, x)
plt.show()
plt.plot(time, z)
plt.show()