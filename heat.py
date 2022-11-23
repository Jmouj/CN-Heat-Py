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
import scipy.sparse as sp
import scipy.sparse.linalg as sla
"""
Define Functions
"""
#Finds the solution for the 1D heat equation.  
#f is the function defining the temperature at some point x. 
#nx = number of space steps, nt = number of time steps
#L = length, T = end time
#alpha = diffusivity
#Top, Bot = Boundary conditions
def heatpde(f,nx,nt,L,T,alpha,Top,Bot):
    #Calculate constants.
    deltat = T/nt
    deltax = L/nx
    r = alpha*deltat/deltax**2/2

    #Create space array.
    x = np.linspace(0,L, num = nx)
    
    #Creates heat array.
    u = np.zeros([nx,nt])
    
    #Fills the array with f(x).
    for i in range(nx):
        u[i,:] = f(x[i])
    
    #Set boundaries.
    u[0,:] = Top
    u[-1,:] = Bot

    #Create diag matrix
    tempA = sp.diags([-r,1+2*r,-r], [-1,0,1], shape = (nx,nx))
    A = sp.csc_matrix(tempA)

    tempB = sp.diags([r,1-2*r,r], [-1,0,1], shape = (nx,nx))
    B = sp.csc_matrix(tempB)

    #Loop through solution.
    for i in range(nt-1):
        #Define fix vector.
        fix = np.zeros(nx)
        fix[0] = r*2*u[0,i]
        fix[-1] = r*2*u[-1,i]
        
        #Finds the RHS
        f = (B*u[0:nx,i]) + fix
        
        #Finds the inverse of A and multiplies it by f. 
        u[0:nx,i+1] = sla.spsolve(A,f)
        
        #Redefines the boundary conditions.
        u[0,:] = Top
        u[-1,:] = Bot
    
    #Returns the solution.
    return x,u

