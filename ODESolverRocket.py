# -*- coding: utf-8 -*-
"""

Script that uses odeint to integrate the differential equations of the rocket both before and
after it runs out of fuel, including drag (w/ air density), gravity, change in mass into the equation, and then plots them.

"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def speedmass(y,t):          #the differential equations for the model before fuel runs out 
    
    dy = [0,0,0]             #create array to store temp values in, easier to work with data this way
    dy[0] = y[0]             #differential of speed 
    dy[1] = y[1]             #differential of mass  
    dy[2] = y[2]             #differential of position
    dydt = [200*9.81*66.6/dy[1]-9.81-0.5*0.6*70*dy[0]*np.abs(dy[0])/dy[1]*1.225*np.exp(-0.1385*dy[2]), -66.6, dy[0]] #differential equations for model w/ fuel,  incorporates air drag (w/ air density), gravity, changing mass, thrust (const), for formulas' origins see report
    
    return dydt              #return differential equation
def speeddrag(y,t):          #differential equations for model after we run out of fuel     
    
    dy = [0,0,0]             #create array to store temp values in, easier to work with data this way
    dy[0] = y[0]             #differential of speed
    dy[1] = y[1]             #differential of mass
    dy[2] = y[2]             #differential of position
    dydt = [-9.81-0.5*0.6*70*dy[0]*dy[0]/dy[1]*1.225*np.exp(-0.1385*dy[2]), 0, dy[0]] #differential equations for model without fuel, incorporates air drag (w/ air density), gravity
    
    return dydt              #return differential equation
y=[0,5000,0]                 #initial speed (m/s), mass(kg), position (m), this is for the first stage, w/ fuel
t=np.arange(0, 60, 1)        #time array for period w/ fuel
t1=np.arange(60, 600, 1)     #timearray for period without fuel, we create 2 separate arrays to integrate separately
          
y=odeint(speedmass, y, t)    #integrate first part (w/ fuel)
y0=[2444,1000,50045]         #initial conditions for stage without fuel (taken from runthrough of first stage)
y0=odeint(speeddrag, y0, t1) #integrate second part (without fuel)

y= np.vstack((y,y0))         #combine results from both parts into single arrays for speed, mass, position so we can plot both stages on one graph
t= np.hstack((t,t1))         #combine two time arrays so we can plot both stages on one graph
#plt.plot(t, y[:, 0], 'b', label='Speed')            #plot speed
#plt.plot(t, y[:, 1], 'g', label='Mass')             #plot mass
plt.plot(t, y[:, 2], 'r', label='Position')          #plot position
plt.xlabel('t (s)')                                  #put axis titles on graph
plt.ylabel('Height (m)')
plt.legend(loc='best')