#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy.abc import c,x,y,u,v,omega,rho,beta
from sympy import Matrix, im, re, symbols, sqrt, init_printing
init_printing()


# In[2]:


ep1,ep2=symbols("epsilon_1 epsilon_2")
e1=x*(1-x**2-y**2)-omega*y+ep1*u
e2=y*(1-x**2-y**2)+omega*x
e3=rho*v
e4=-rho*beta*u-c*v+ep2*x
X = Matrix([e1,e2,e3,e4])
F=X.jacobian([x,y,u,v])


# In[3]:


F


# In[5]:


jack=F.subs([(beta,1),(rho,1),(c,1),(omega,5)])
jack


# In[6]:


def check_stability(jack):
    k=0
    p=list(jack.eigenvals().keys())
    #print("**Real Part of Eigenvalues**")
    for i in p:
        #print(re(i.evalf()))
        if re(i.evalf())>=0:
            k=1
    #print("***************************")
    return k


# In[7]:


def jack_eval(epsilon1):
    epsilon2=8
    stable=[]
    unstable=[]
    a=(epsilon1*epsilon2+50 +sqrt((epsilon1**2)*(epsilon2**2)-100))/(2*epsilon1*epsilon2)
    b=(epsilon1*epsilon2+50 -sqrt((epsilon1**2)*(epsilon2**2)-100))/(2*epsilon1*epsilon2)
    
    
    #first trivial fixed point
    x1=0
    y1=0
    u1=0

    #second fixed point
    x2=(5*a)/(-25+a*a*epsilon1*epsilon2)
    y2=a
    u2=(5*a*epsilon2)/(-25+a*a*epsilon1*epsilon2)

    #third fixed point
    x3=(-5*a)/(-25+a*a*epsilon1*epsilon2)
    y3=-a
    u3=(5*a*epsilon2)/(-25+a*a*epsilon1*epsilon2)

    #fourth fixed point
    x4=(5*b)/(-25+b*b*epsilon1*epsilon2)
    y4=b
    u4=(5*b*epsilon2)/(-25+b*b*epsilon1*epsilon2)

    #fifth fixed point
    x5=(-5*b)/(-25+b*b*epsilon1*epsilon2)
    y5=-b
    u5=(5*b*epsilon2)/(-25+b*b*epsilon1*epsilon2)

    x1=float(x1)
    y1=float(y1)
    u1=float(u1)
    
    x2=float(x2)
    y2=float(y2)
    u2=float(u2)
    
    x3=float(x3)
    y3=float(y3)
    u3=float(u3)
    
    x4=float(x4)
    y4=float(y4)
    u4=float(u4)
    
    x5=float(x5)
    y5=float(y5)
    u5=float(u5)
    
    #print(x1,float(x2),float(x3),float(x4),float(x5))
    xi=[[x1,y1,u1],[x2,y2,u2],[x3,y3,u3],[x4,y4,u4],[x5,y5,u5]]
    #print("Set of Fixed Points: ",xi)
    i=1
    for point in xi:
        j=jack.subs([(x,point[0]),(y,point[1]),(u,point[2]),(ep2,epsilon2),(ep1,epsilon1)])
        #print(f"\nx({i}):")
        #print(point[0])
        if check_stability(j)==0:
            stable.append(point[0])
            print(point[0])
        else:
            unstable.append(point[0])
            
        i+=1
    return [stable,unstable]


# In[9]:


jack_eval(5)


# In[26]:


import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(16,7))
stable=[]
unstable=[]
for val in np.linspace(2,8,100):
    s_temp,u_temp=jack_eval(val)
    #s_temp=np.array(s_temp)
    #u_temp=np.array(u_temp)
    #print(s_temp,"\n ***",u_temp)
    stable.append(s_temp)
    unstable.append(u_temp)
    for point in u_temp:#plot unstable points
        plt.plot(val,point,'r.',markersize=0.5)#,label="Unstable Points")
        
    for point in s_temp:

        plt.plot(val,point,'b*',markersize=0.5)#,label="Stable Points")

#######################################################
plt.title("x vs $\epsilon_{1}$ with $\epsilon_{1}=8$")        
#plt.legend()
#plt.show()


# In[27]:


plt.savefig("phase.jpg",dpi=1000)


# In[ ]:




