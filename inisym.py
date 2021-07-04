#!/usr/bin/env python
# coding: utf-8


import numpy as np
#from sympy.abc import c,x,y,u,v,omega,rho,beta
#from sympy import symbols
p = 16.0
r = 45.92
b = 4.0

# define equation
def evaluate(x,y,z):
   
    x_dot = p*(y-x)
    y_dot = -x*z + r*x - y
    z_dot = x*y - b*z

    return x_dot, y_dot, z_dot


def compute(x0,y0,z0,t0,steps=1000,delta_t=0.01):
	
	steps=int(steps)
	# initialize solutions arrays (+1 for initial conditions)
	xx = np.empty((steps + 1))
	yy = np.empty((steps + 1))
	zz = np.empty((steps + 1))
	
	tt = np.empty((steps+1))
	# fill in initial conditions
	xx[0], yy[0],zz[0]= (x0,y0,z0)
	tt[0] = t0
	# solve equation system
	
	for i in range(steps):
		# Calculate derivatives
		x_dot, y_dot, z_dot= evaluate(xx[i], yy[i], zz[i])

		tt[i+1] = tt[i] + delta_t

		xx[i + 1] = xx[i] + (x_dot * delta_t)
		yy[i + 1] = yy[i] + (y_dot * delta_t)
		zz[i + 1] = zz[i] + (z_dot * delta_t)
		
	return xx,yy,zz,tt


n=2e7
n=int(n)
dt=0.001
x1,y1,z1,t1=compute(1.0,1.0,1.0,0,steps=n,delta_t=dt)
summation1=0.0
summation2=0.0
summation3=0.0
k=0
for i in range(1,n+1):
	k=k+1
	summation1=summation1+ np.log(np.abs((x1[i]-x1[i-1])/dt))
	summation2=summation2+ np.log(np.abs((y1[i]-y1[i-1])/dt))
	summation3=summation3+ np.log(np.abs((z1[i]-z1[i-1])/dt))
lamda=[]
lamda.append(summation1/k)
lamda.append(summation2/k)
lamda.append(summation3/k)
print("lamdax=", lamda[0])
print("lamday=", lamda[1])
print("lamdaz=", lamda[2])

np.savetxt('x.txt', (x1))
np.savetxt('y.txt', (y1))
np.savetxt('z.txt', (z1))


	
