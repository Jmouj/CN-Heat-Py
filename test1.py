# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:50:09 2022

Project

@author: Jacob Moujalli
"""
"""
Import Functions
"""
from heat2d import heatpde2D
import matplotlib.pyplot as plt
"""
Define Functions
"""
#Function defines the starting temperature at any given point.
def f(x,y):
    return 100
"""
Main Script
"""
#Constants:
#Number of space steps.
nx = 40

#Number of time steps.
nt = 200

#Time (Defines deltat)
T = 0.5

#Length (Defines deltax and deltay).
L = 1

#Diffusion rate.
alpha = 0.2

#Boundary Conditions.
Top = 0
Bot = 0
Left = 0
Right = 0

#Call the function. Solves the 2D heat equation with Crank-Nicolson.
u = heatpde2D(f,nx,nt,L,T,alpha,Top,Bot,Left,Right)

#2D Plot at some time.
plt.imshow( u[:,:,70] , cmap = 'coolwarm' , interpolation = 'nearest' )
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.imshow( u[:,:,199] , cmap = 'coolwarm' , interpolation = 'nearest' )
plt.xlabel('x')
plt.ylabel('y')
plt.show()

