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
#This function takes 6 parameters: position, velocity, acceleration, time1, time2 and length
#This function calculates the new acceleration, velocity and position based on 
#the previous or "old" values 
#It returns the new acceleration, velocity and acceleration
    dt = time2-time1
    new_acceleration = (-9.81 * math.sin(pos))/l
    new_velocity = vel + (new_acceleration * dt)
    new_position = pos + (new_velocity * dt)
    return new_acceleration, new_velocity, new_position

def print_system():
#This function takes no parameters, has no returns and prints the time,position
# velocity and acceleration
    print("Time:     ", time)
    print("Position: ", pos)
    print("Velocity: ", vel)
    print("Acceleration ", acc, "\n")
    
def run_simulation(l, initialpos):
#This function takes 2 parameters: length and initial position 
#it uses the update_system function to calculated and then append the new accelerations,
#velocities and positions
#It returns the new positions, velocity and acceleration
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
#This function takes one parameter: the position 
#this function calculates the period and plots it on a graph 
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
#here the simulation is carried out for the 5 lengths 
#print("10 inch Trial")
plt.subplot(5,1,1)
pos, vel, acc = run_simulation(0.254, np.pi/3)  
plt.plot(time, pos)
period(pos)

#print("12 inch Trial")
plt.subplot(5,1,2)
pos, vel, acc = run_simulation(0.305, np.pi/3)  
plt.plot(time, pos)
period(pos)

#print("14 inch Trial")
plt.subplot(5,1,3)
pos, vel, acc = run_simulation(0.356, np.pi/3)  
plt.plot(time, pos)
period(pos)

#print("16 inch Trial")
plt.subplot(5,1,4)
pos, vel, acc = run_simulation(0.406, np.pi/3)  
plt.plot(time, pos)
period(pos)

#print("18 inch Trial")
plt.subplot(5,1,5)
pos, vel, acc = run_simulation(0.457, np.pi/3)  
plt.plot(time, pos)
period(pos)
