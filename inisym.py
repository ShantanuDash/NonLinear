#!/usr/bin/env python
# coding: utf-8


import numpy as np
from sympy.abc import c,x,y,u,v,omega,rho,beta
from sympy import symbols

ep1,ep2=symbols("epsilon_1 epsilon_2")
e1=x*(1-x**2-y**2)-omega*y+ep1*u
e2=y*(1-x**2-y**2)+omega*x
e3=rho*v
e4=-rho*beta*u-c*v+ep2*x

# define equation
def evaluate(X,Y,U,V,epsilon1=6,epsilon2=8,b=1,p=1,C=1,w=5):
    ''' input format: X,Y,U,V,epsilon1=6,epsilon2=8,b=1,p=1,C=1,w=5'''
    x_dot = e1.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
    y_dot = e2.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
    u_dot = e3.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
    v_dot = e4.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])

    return x_dot.evalf(), y_dot.evalf(), u_dot.evalf(), v_dot.evalf()


def compute(x0,y0,u0,v0,t0,epsilon1=6,epsilon2=8,b=1,p=1,C=1,w=5,steps=1000,delta_t=0.01):
	''' 
	input format: x0,y0,u0,v0,t0,epsilon1=6,epsilon2=8,b=1,p=1,C=1,w=5,steps=1000,delta_t=0.01
	usage : x1,y1,u1,v1,t1=compute(0.1,0,0,0,t0,p=2,steps=2000)	
	'''
	steps=int(steps)
	# initialize solutions arrays (+1 for initial conditions)
	xx = np.empty((steps + 1))
	yy = np.empty((steps + 1))
	uu = np.empty((steps + 1))
	vv = np.empty((steps + 1))
	tt = np.empty((steps+1))
	# fill in initial conditions
	xx[0], yy[0], uu[0], vv[0] = (x0,y0,u0,v0)
	tt[0] = t0
	# solve equation system
	
	for i in range(steps):
		# Calculate derivatives
		x_dot, y_dot, u_dot, v_dot = evaluate(xx[i], yy[i], uu[i], vv[i],epsilon1,epsilon2,b,p,C,w)

		tt[i+1] = tt[i] + delta_t

		xx[i + 1] = xx[i] + (x_dot * delta_t)
		yy[i + 1] = yy[i] + (y_dot * delta_t)
		uu[i + 1] = uu[i] + (u_dot * delta_t)
		vv[i + 1] = vv[i] + (v_dot * delta_t)
	return xx,yy,uu,vv,tt

#xaxis=np.linspace(-4,4,)
for P in range(-4,5):
	n=2e3
	n=int(n)
	dt=0.01
	x1,y1,u1,v1,t1=compute(0.1,0,0,0,0.0,p=P,steps=n,delta_t=dt)
	summation1=0.0
	summation2=0.0
	k=0
	for i in range(1,n+1):
		k=k+1
		summation1=summation1+ np.log(np.abs((x1[i]-x1[i-1])/dt))
		summation2=summation2+ np.log(np.abs((y1[i]-y1[i-1])/dt))

	lamda=[]
	lamda.append(summation1/k)
	lamda.append(summation1/k)
	print(f"lamda1_p_{P}=", lamda[0])
	print(f"lamda2_p_{P}=", lamda[1])

	np.savetxt(f'x_{P}.txt', (x1))
	np.savetxt(f'y_{P}.txt', (y1))


	
