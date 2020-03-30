#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:47:32 2020

@author: gackermannlogan
"""
#Project 1 Step 5 
#Authors: Gaby Ackerman Logan and Tara Donodue 
#Hours spent: 2 total 
#Imports
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.signal as sig

#Varibales
l = [0.254, 0.305, 0.356, 0.406, 0.457]
pos = [0]
vel = [0]
acc = [0]
time = np.linspace(0, 10, 100000)

#Functions
def update_system(pos,vel,acc,time1,time2,l):
    dt = time2-time1
    new_acceleration = (-9.81 * math.sin(pos))/l
    new_velocity = vel + (new_acceleration * dt)
    new_position = pos + (new_velocity * dt)
    return new_acceleration, new_velocity, new_position

def print_system ():
    print("Time:     ", time)
    print("Position: ", pos)
    print("Velocity: ", vel)
    print("Acceleration ", acc, "\n")
    
def run_simulation(l, initialpos):
    i = 1
    pos = [initialpos]
    vel = [0]
    acc = [(-9.81 * math.sin(initialpos))/l]
    while i < len(time):
        new_acceleration, new_velocity,new_position = update_system(pos[i-1],vel[i-1],acc[i-1],time[i-1],time[i],l)
        pos.append(new_position)
        vel.append(new_velocity)
        acc.append(new_acceleration)
        i += 1
    return pos, vel, acc

def period(pos):
    filtered_pos = sig.medfilt(pos)
    peaks = sig.find_peaks(filtered_pos)[0]
    change = 0
    timeinput = time[peaks]
    for i in range(len(peaks)-1):
        difference_in_time = timeinput[i+1] - timeinput[i]
        change = change + difference_in_time
    period = change/(len(timeinput)-1)
    print(period)
    plt.plot(time, filtered_pos, 'r-', time[peaks], filtered_pos[peaks], 'b.')
    plt.title("Period")
    plt.xlabel("Time")
    plt.ylabel("Theta (degrees)")
    plt.show()

#Main Script
pos, vel, acc = run_simulation(0.305, np.pi/3)  
plt.plot(time, pos)
period(pos)