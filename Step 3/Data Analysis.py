#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 13:15:49 2020

@author: gackermannlogan
"""
import os
import numpy as np 
import matplotlib.pyplot as plt
path = "/Users/gackermannlogan/mu_code/data_capture/"
os.chdir(path)
print(os.getcwd())
fin = open("10inch-Trial.csv", "r")

def find_tilt_x(acc_x, acc_y, acc_z):
    y_denominator = np.sqrt((y ** 2) + (z ** 2))
    x_numerator = x
    angle_x = np.arctan(x_numerator / y_denominator)
    np.degrees(angle_x)
    return np.degrees(angle_x)
def find_tilt_y(acc_x, acc_y, acc_z):
    x_denominator = np.sqrt((x ** 2) + (z ** 2))
    y_numerator = y
    angle_y = np.arctan(y_numerator / x_denominator)
    np.degrees(angle_y)
    return np.degrees(angle_y)
def find_tilt_z(acc_x,acc_y,acc_z):
    x_and_y_denominator = np.sqrt((y ** 2) + (x ** 2))
    z_numerator = z
    angle_z = np.arctan(z_numerator / x_and_y_denominator)
    np.degrees(angle_z)
    return np.degrees(angle_z)

array = (np.genfromtxt(fin, delimiter = ","))
x = np.array(array[:,0])
y = np.array(array[:,1])
z = np.array(array[:,2])
x_axis = np.array(find_tilt_x(x,y,z))
y_axis = np.array(find_tilt_y(x,y,z))
z_axis = np.array(find_tilt_z(x,y,z))
plt.plot(x,y,z)
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()
