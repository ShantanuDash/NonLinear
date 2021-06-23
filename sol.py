#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import c,x,y,u,v,omega,rho,beta
from sympy import Matrix, im, re, symbols, sqrt, init_printing
#init_printing()


# In[2]:


ep1,ep2=symbols("epsilon_1 epsilon_2")
e1=x*(1-x**2-y**2)-omega*y+ep1*u
e2=y*(1-x**2-y**2)+omega*x
e3=rho*v
e4=-rho*beta*u-c*v+ep2*x


# define equation
def evaluate(X,Y,U,V,epsilon1,epsilon2,b=1,p=1,C=1,w=5):
    x_dot = e1.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
    y_dot = e2.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
    u_dot = e3.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
    v_dot = e4.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
        
    return x_dot.evalf(), y_dot.evalf(), u_dot.evalf(), v_dot.evalf()
    
    # basic parameters
delta_t = 0.0001 
steps = 50000

# initialize solutions arrays (+1 for initial conditions)
xx = np.empty((steps + 1))
yy = np.empty((steps + 1))
uu = np.empty((steps + 1))
vv = np.empty((steps + 1))
tt = np.empty((steps+1))
# fill in initial conditions
xx[0], yy[0], uu[0], vv[0] = (0.1, 0.1, 0.1, 0.1)
tt[0] = 0.0
# solve equation system

for i in range(steps):
    # Calculate derivatives
    x_dot, y_dot, u_dot, v_dot = evaluate(xx[i], yy[i], uu[i], vv[i],4,2)
    
    tt[i+1] = tt[i] + delta_t
    
    xx[i + 1] = xx[i] + (x_dot * delta_t)
    yy[i + 1] = yy[i] + (y_dot * delta_t)
    uu[i + 1] = uu[i] + (u_dot * delta_t)
    vv[i + 1] = vv[i] + (v_dot * delta_t)


# In[ ]:


#plt.style.use('dark_background')
plt.figure(figsize=(16,7))

plt.subplot(1, 2, 1)
plt.title("x,u vs t")
plt.xlim((min(tt),max(tt))) 
plt.ylim((min(xx),max(xx)))

plt.plot(tt, xx,'k.')
plt.plot(tt, uu,"r.") #,color='white',markersize=0.5)
plt.xlabel("Time, t")
plt.ylabel("x,u")

plt.subplot(1, 2, 2)
plt.title("y,v vs t")
plt.xlim((min(tt),max(tt))) 
plt.ylim((min(yy),max(yy)))

plt.plot(tt, yy,'k.')
plt.plot(tt, vv,"r.") #,color='white',markersize=0.5)
plt.xlabel("Time, t")
plt.ylabel("y,v")
plt.savefig("out.jpg",dpi=1200)

