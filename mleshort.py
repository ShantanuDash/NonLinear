#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import c,x,y,u,v,omega,rho,beta
from sympy import Matrix, im, re, symbols, sqrt, init_printing
init_printing()


# In[2]:


ep1,ep2=symbols("epsilon_1 epsilon_2")
e1=x*(1-x**2-y**2)-omega*y+ep1*u
e2=y*(1-x**2-y**2)+omega*x
e3=rho*v
e4=-rho*beta*u-c*v+ep2*x



def compute(x0,y0,u0,v0,t0,pee=1,steps=1000,delta_t=0.01):
    # define equation
    def evaluate(X,Y,U,V,epsilon1=6,epsilon2=8,b=1,p=pee,C=1,w=5):
        x_dot = e1.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
        y_dot = e2.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
        u_dot = e3.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])
        v_dot = e4.subs([(x,X),(y,Y),(u,U),(v,V),(beta,b),(rho,p),(c,C),(omega,w),(ep1,epsilon1),(ep2,epsilon2)])

        return x_dot.evalf(), y_dot.evalf(), u_dot.evalf(), v_dot.evalf()

        # basic parameters
    #delta_t = 0.01 
    #steps = 1000

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
        x_dot, y_dot, u_dot, v_dot = evaluate(xx[i], yy[i], uu[i], vv[i])

        tt[i+1] = tt[i] + delta_t

        xx[i + 1] = xx[i] + (x_dot * delta_t)
        yy[i + 1] = yy[i] + (y_dot * delta_t)
        uu[i + 1] = uu[i] + (u_dot * delta_t)
        vv[i + 1] = vv[i] + (v_dot * delta_t)
    return xx,yy,uu,vv,tt
xaxis=np.linspace(-4,4,16)
mle=[]
for p in xaxis:
	d0=1e-5
	steps=2000
	#p=1
	t0=0
	x1,y1,u1,v1,t1=compute(0.1,0,0,0,t0,p,steps)
	x2,y2,u2,v2,t2=compute(0.1+d0,0+d0,0+d0,0+d0,t0,p,steps)


	# In[ ]:


	d1=[]
	for i in range(steps+1):
		d1.append(np.sqrt((x1[i]-x2[i])**2+(y1[i]-y2[i])**2))


	# In[ ]:


	plt.figure(figsize=(16,16))

	plt.subplot(2, 1, 1)
	plt.plot(t1,d1,'ro',label="d",markersize=0.8)
	plt.title(f"d(distance between (x,y) and (x+d0,y+d0))  VS Time , p={p}, d0={d0}")
	plt.xlabel("Time")
	plt.ylabel("d")
	plt.legend()
	#plt.show()

	plt.subplot(2,1,2)

	logd=[np.log(d/d0) for d in d1]
	till=steps
	model=np.polyfit(t1[:till],logd[:till],1)
	predict=np.poly1d(model)

	plt.plot(t1,logd,'b.',label="$log_{e}(d1/d0)$",markersize=0.8)
	plt.plot(t1[:till],predict(t1[:till]),'r--',label=f"{model[0]}*x+{model[1]}")
	plt.title("$log_{e}(d/d0)$ VS Time ," + f" p={p}, d0={d0}")
	plt.xlabel("Time")
	plt.ylabel("$log_{e}(d/d0)$")
	plt.legend()
	plt.savefig(f"lyapunov{p}.png",dpi=800)
	mle.append(model[0])

np.savetxt('out.txt', (xaxis, mle))

# In[ ]:



# In[ ]:



