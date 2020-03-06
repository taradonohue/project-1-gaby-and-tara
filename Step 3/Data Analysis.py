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
    y_denominator = np.sqrt((y * 2) + ((z * 2)))
    x_numerator = x
    angle_x = np.atan2(x_numerator, y_denominator)
    np.degrees(angle_x)
    return np.degrees(angle_x)
def find_tilt_y(acc_x, acc_y, acc_z):
    x_denominator = np.sqrt((x * 2) + ((z * 2)))
    y_numerator = y
    angle_y = np.atan2(y_numerator, x_denominator)
    np.degrees(angle_y)
    return np.degrees(angle_y)
def find_tilt_z(acc_x,acc_y,acc_z):
    x_and_y_denominator = np.sqrt((y * 2) + ((x * 2)))
    z_numerator = z
    angle_z = np.atan2(z_numerator, x_and_y_denominator)
    np.degrees(angle_z)
    return np.degrees(angle_z)

list = (np.genfromtxt(fin, delimiter = ","))
x = list[0:1]
y = list[1]
z = list[2]
print(x)
#plt.plot()
#plt.title()
#plt.xlabel()
#plt.ylabel()
#plt.show()
