# -*- coding: utf-8 -*-
"""

Script that uses odeint to integrate the differential equations of the rocket both before and
after it runs out of fuel, including drag into the equation.

"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def speedmass(y,t):          #the differential before fuel runs out 
    
    dy = [0,0,0]
    dy[0] = y[0]             #diff of speed
    dy[1] = y[1]             #diff of mass  
    dy[2] = y[2]             #diff of position
    dydt = [200*9.81*66.6/dy[1]-9.81-0.5*0.6*70*dy[0]*dy[0]/dy[1]*1.225*np.exp(-0.1385*dy[2]), -66.6, dy[0]] #differential equations
    
    return dydt
def speeddrag(y,t):          #model after we run out of fuel     
    
    dy = [0,0,0]
    dy[0] = y[0]             #speed
    dy[1] = y[1]             #mass
    dy[2] = y[2]             #position
    dydt = [-9.81-0.5*0.6*70*dy[0]*dy[0]/dy[1]*1.225*np.exp(-0.1385*dy[2]), 0, dy[0]] #differential equations
    
    return dydt
y=[0,5000,0]                 #initial speed (m/s), mass(kg), position (m) 
t=np.arange(0, 60, 1)        #time array for period w/ fuel
t1=np.arange(60, 300, 1)     #time without fuel
          
y=odeint(speedmass, y, t)    #integrate first part
y0=[2444,1000,50045]         #initial conditions for stage without fuel
y0=odeint(speeddrag, y0, t1) #intergate second part

y= np.vstack((y,y0))         #combine results from both parts into single arrays
t= np.hstack((t,t1))
plt.plot(t, y[:, 0], 'b', label='Speed')            #plot result
#plt.plot(t, y[:, 1], 'g', label='Mass')
#plt.plot(t, y[:, 2], 'r', label='Position')
plt.legend(loc='best')