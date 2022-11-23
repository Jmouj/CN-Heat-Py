# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:50:09 2022

Project

@author: Jacob Moujalli
"""
"""
Import Functions
"""
import numpy as np
import math as math
"""
Define Functions
"""
#Defines the analytical solution for the function f(x) = 0.5
def example1(nx,nt,L,T):
    #Creates solution array
    ua = np.zeros([nx,nt]) 
    
    #Defines the space and time vectors.
    t = np.linspace(0,T, num = nt)
    x = np.linspace(0,L, num = nx)
    
    #Iterates through the solution.
    for n in range(1,800):
        for i in range(nt-1):
            #Defines each component in the Fourier series
            e = math.exp(-0.5*((n*math.pi)**2)*t[i])
            s = np.sin(n*math.pi*x[:])
            o = -1*((-1)**n - 1)/(math.pi*n)
            
            #Sums the solution.
            ua[:,i] = ua[:,i] + e*s*o
    return x,ua

#Defines the analytical solution for the function f(x) = cos(pi*x)
def example2(nx,nt,L,T):
    #Creates solution array
    ua = np.zeros([nx,nt]) 
    
    #Defines the space and time vectors.
    t = np.linspace(0,T, num = nt)
    x = np.linspace(0,L, num = nx)
    
    #Iterates through the solution.
    for n in range(2,800):
        for i in range(nt):
            #Defines each component in the Fourier series
            e = math.exp(-0.5*((n*math.pi)**2)*t[i])
            s = np.sin(n*math.pi*x[:])
            o = (2*n*((-1)**n + 1))/(math.pi*(n+1)*(n-1))
            
            #Sums the solution.
            ua[:,i] = ua[:,i] + e*s*o
    return x,ua