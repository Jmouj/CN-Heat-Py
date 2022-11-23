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
import matplotlib.pyplot as plt
"""
Define Functions
"""
#Defines a step function.
def f(x):
    if x > 0.5:
        return 100
    else:
        return 50
#Defines an impulse function.
def f2(x):
    if 0.51 > x > 0.49:
        return 100
    else:
        return 0
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
Bot = 100

#Function 1 (Step function)
xn,un = heatpde(f,nx,nt,L,T,alpha,Top,Bot)

#Plot solutions at various times.
plt.plot(xn,un[:,0])
plt.plot(xn,un[:,500])
plt.xlabel('x')
plt.ylabel('u')
plt.legend(["t = 0","t = 0.5"])
plt.show()

#Function 2 (Impulse)
xn1,un1 = heatpde(f2,500,20000,L,T,alpha,0,0)

#Plot solutions at various times.
plt.plot(xn1,un1[:,0])
plt.plot(xn1,un1[:,20])
plt.plot(xn1,un1[:,30])
plt.plot(xn1,un1[:,50])
plt.plot(xn1,un1[:,100])
plt.xlabel('x')
plt.ylabel('u')
plt.legend(["t = 0","t = 0.02","t = 0.03","t = 0.05","t = 0.1"])
plt.show()