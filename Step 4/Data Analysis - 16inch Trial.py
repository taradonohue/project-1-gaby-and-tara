#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:47:03 2020

@author: gackermannlogan
"""
#Project 1 Step 4 
#Authors: Gaby Ackerman Logan and Tara Donodue 
#Hours spent: 6 total 
#Imports
import os
import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as sig
path = "/Users/gackermannlogan/mu_code/data_capture/"
os.chdir(path)
print(os.getcwd())
fin = open("16inch-Trial.csv", "r")
#Functions
def find_tilt_x(acc_x, acc_y, acc_z):
#This function takes 3 parameters of the acceleration in the x, y, and z directions. 
#This function calculatesthe angle on the x-axis in degrees
#it returns the the calculated angle
    y_denominator = np.sqrt((y ** 2) + (z ** 2))
    x_numerator = x
    angle_x = np.arctan(x_numerator / y_denominator)
    np.degrees(angle_x)
    return np.degrees(angle_x)

def find_tilt_y(acc_x, acc_y, acc_z):
#This function takes 3 parameters of the acceleration in the x, y, and z directions. 
#This function calculatesthe angle on the y-axis in degrees
#it returns the the calculated angle
    x_denominator = np.sqrt((x ** 2) + (z ** 2))
    y_numerator = y
    angle_y = np.arctan(y_numerator / x_denominator)
    np.degrees(angle_y)
    return np.degrees(angle_y)

def find_tilt_z(acc_x,acc_y,acc_z):
#This function takes 3 parameters of the acceleration in the x, y, and z directions. 
#This function calculatesthe angle on the z-axis in degrees
#it returns the the calculated angle
    x_and_y_denominator = np.sqrt((y ** 2) + (x ** 2))
    z_numerator = z
    angle_z = np.arctan(z_numerator / x_and_y_denominator)
    np.degrees(angle_z)
    return np.degrees(angle_z)

def find_period():
#This function takes no parameters 
#This function calculatesthe period using the calculated angles and specific time interval
#It prints the period calculated and the graph showing the maximas used in the calculation
    filtered_y = sig.medfilt(y_axis)
    peaks = sig.find_peaks(filtered_y)[0]
    indextoremove = [0,2,3,4,5,7,8,10,11,12,14,16,18,19,20]
    newpeaks = np.delete(peaks, indextoremove)
    time = np.array(array[900:1096,3])
    change = 0
    timeinput = time[newpeaks]
    for i in range(6):
        difference_in_time = timeinput[i+1] - timeinput[i]
        change = change + difference_in_time
    period = change/(len(timeinput)-1)
    print(period)
    plt.plot(time, filtered_y, 'r-', time[newpeaks], filtered_y[newpeaks], 'b.')
    plt.title("Period")
    plt.xlabel("Time")
    plt.ylabel("Theta (degrees)")
    plt.show()
    
#Main Script 
#The time interval is set and the acceleration, theta and period graphs are graphed
array = (np.genfromtxt(fin, delimiter = ","))
x = np.array(array[900:1096,0])
y = np.array(array[900:1096,1])
z = np.array(array[900:1096,2])
time = np.array(array[900:1096,3])
x_axis = np.array(find_tilt_x(x,y,z))
y_axis = np.array(find_tilt_y(x,y,z))
z_axis = np.array(find_tilt_z(x,y,z))

plt.plot(time, z_axis)
plt.title("Theta v. Time")
plt.xlabel("Time")
plt.ylabel("Theta")
plt.show()


plt.plot(time, x)
plt.plot(time, y)
plt.plot(time, z)
plt.legend("x" "y" "z")
plt.title("Acceleration v. Time")
plt.xlabel("Time")
plt.ylabel("Acceleration")
plt.show()

find_period()
