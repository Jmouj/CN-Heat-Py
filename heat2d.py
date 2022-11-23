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
#Finds the solution for the 2D heat equation.  
#f is the function defining the temperature at some point x,y. 
#nx = number of space steps, nt = number of time steps
#L = length, T = end time
#alpha = diffusivity
#Top, Bot, Left, Right = Boundary conditions
def heatpde2D(f,nx,nt,L,T,alpha,Top,Bot,Left,Right):
    #Keeps the space sqaure for simplicity.
    ny = nx
    
    #Define space and time step.
    deltat = T/nt
    deltax = L/nx
    
    
    #Define constants.
    alpha = 0.1
    r = alpha*deltat/deltax**2/2
    
    #Divides diffusion rate by 2 as the calculations are being run twice.
    r = r/2
    
    #Creates the heat array.
    u = np.zeros([nx,ny,nt])
    
    #Fills the array with f(x).
    for i in range(nx):
        for n in range(ny):
            u[i,n,:] = f(i,n)
    
    #Boundary conditions
    u[:,0,:] = Left
    u[:,-1,:] = Right
    u[0,:,:] = Top
    u[-1,:,:] = Bot
    
    #Create diag matrices.
    tempA = sp.diags([-r,1+2*r,-r], [-1,0,1], shape = (nx,nx))
    A = sp.csc_matrix(tempA)

    tempB = sp.diags([r,1-2*r,r], [-1,0,1], shape = (nx,nx))
    B = sp.csc_matrix(tempB)
    
    #Calculations. Alternates between horizontal and vertical calculations.
    for n in range(nt-1):
        if n % 2 == 0:
            for i in range(ny):
                #Fixes the ends
                fix = np.zeros(ny)
                fix[0] = r*2*u[i,0,n]
                fix[-1] = r*2*u[i,-1,n]
                
                #f to be multplied by A^-1
                f = B*u[i,0:ny,n] + fix
                
                #Solve
                u[i,0:ny,n+1] = sla.spsolve(A,f)
                
                #Reset boundary conditions.
                u[:,0,:] = 0
                u[:,-1,:] = 0
                u[0,:,:] = 0
                u[-1,:,:] = 0
        else:
            for i in range(nx):
                #Fixes the ends
                fix = np.zeros(nx)
                fix[0] = r*2*u[0,i,n]
                fix[-1] = r*2*u[-1,i,n]
                
                #f to be multplied by A^-1
                f = B*u[0:nx,i,n] + fix
                
                #Solve
                u[0:nx,i,n+1] = sla.spsolve(A,f)
                
                #Reset boundary conditions.
                u[:,0,:] = 0
                u[:,-1,:] = 0
                u[0,:,:] = 0
                u[-1,:,:] = 0
    
    #Returns the calculated heat diffusion at each time and space, u.    
    return u