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

#Example 1: f = 0.5

#Numerical Solution
xn1,un1 = heatpde(f,nx,nt,L,T,0.5,0,0)

#Analytical Solution
xa1,ua1 = example1(nx,nt,L,T)

#Plot solutions
plt.plot(xn1,un1[:,0],linestyle = 'dotted')
plt.plot(xn1,un1[:,500],linestyle = 'dotted')

plt.plot(xa1,ua1[:,0])
plt.plot(xa1,ua1[:,500])
plt.xlabel('x')
plt.ylabel('u')
plt.legend(["Numerical t = 0","Numerical t = 0.5","Analytical t = 0","Analytical t = 0.5"])
plt.show()


#Example 2: f = cos(x)

#Numerical Solution
xn2,un2 = heatpde(f2,nx,nt,L,T,0.5,0,0)

#Analytical Solution
xa2,ua2 = example2(nx,nt,L,T)

#Plot Solutions
plt.plot(xn2,un2[:,0],linestyle = 'dotted')
plt.plot(xn2,un2[:,20],linestyle = 'dotted')

plt.plot(xa2,ua2[:,0])
plt.plot(xa2,ua2[:,20])
plt.xlabel('x')
plt.ylabel('u')
plt.legend(["Numerical t = 0","Numerical t = 0.02","Analytical t = 0","Analytical t = 0.02"])
plt.show()

#Error averaged over all points in time and space.
print('Error in example 1: ', np.sqrt(mse(ua1,un1)))
print('Error in example 2: ', np.sqrt(mse(ua2,un2)))