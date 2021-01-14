#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:59:25 2020

@author: flo
"""

from pylab import *
import numpy as np





mu, sigma = 0, 2 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

p = np.random.poisson(1.0,1)

x = []
t = []
t.append(0)
x.append(0)
time = 0
for i in arange(0,2000):
    tau = np.random.exponential(1.0,1)
    time = time + tau[0]
    t.append(time)
    pos = i*0
    x.append(pos)
    
plot(t,x)
#t = array(t, dtype='float')
#x = array(x, dtype='float')
#m,b = np.polyfit(t, x, 1)

tt = arange(0,t[-1],1)

#plot(t,m*t+b)

#line = m*t + b

#dx = x-line
#plot(t,dx)

from scipy.interpolate import interp1d

f2 = interp1d(t, x, kind='previous', axis = 0)

xxx = f2(tt)
xs = xxx + np.random.normal(mu, 5, len(xxx))
plot(tt,xs)

e = []
d = []
l = len(xs)
v=1
for j in arange(0,l):
    p = 0
    for i in arange(0,l-j):
        p = p + (((xs[j+i]-xs[i]-v*j)**2)/(l-j+1))
     #   print(p)
    d.append(p)
    e.append((xs[j]-0*j)**2)
    
#from scipy import signal

#dx = signal.detrend(x)
#plot(t,dx)