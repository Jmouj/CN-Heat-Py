# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:50:09 2022

Project

@author: Jacob Moujalli
"""
"""
Import Functions
"""
from heat import heatpde
from analytical import example1,example2
import numpy as np
import math as math
import matplotlib.pyplot as plt
"""
Define Functions
"""
#First example function.
def f(x):
    return 0.5
#Second example function.
def f2(x):
    return np.cos(math.pi*x)
#Function to calculate the mean-squared error.
def mse(actual, predicted):
    actual = np.array(actual)
    predicted = np.array(predicted)
    differences = np.subtract(actual, predicted)
    squared_differences = np.square(differences)
    return squared_differences.mean()
"""
Main Script
"""
#Define Constants
nx = 50
nt = 1000
L = 1
T = 1
alpha = 0.5
Top = 0
Bot = 0

#Convergence for example 1
nt = np.linspace(100,1100,11)
deltat = T/nt
error1 = np.zeros(11)

#Iterates through the values of nt.
for i in range(11):
    xn,un = heatpde(f,nx,int(nt[i]),L,T,alpha,Top,Bot)
    xa,ua = example1(nx,int(nt[i]),L,T)
    error1[i] = np.sqrt(mse(ua,un))

#Log-Log plot for dt against error.
plt.loglog(deltat,error1)

#Convergence for example 2
error2 = np.zeros(11)

#Iterates through the values of nt.
for i in range(11):
    xn,un = heatpde(f2,nx,int(nt[i]),L,T,alpha,Top,Bot)
    xa,ua = example2(nx,int(nt[i]),L,T)
    error2[i] = np.sqrt(mse(ua,un))

#Log-Log plot for dt against error.
plt.loglog(deltat,error2)

#Add labels.
plt.legend(["Example 1 (f = 0.5)","Example 2 (f = cos(pi*x))"])
plt.xlabel('dt')
plt.ylabel('error')
plt.show()