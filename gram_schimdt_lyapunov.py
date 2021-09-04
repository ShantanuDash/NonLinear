import numpy as np 
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
p     = 10.0
r     = 28.0
b     = -8.0/3.0

# define equation
def evaluate(t,var):
    x,y,z=var
    return [p*(y-x),-x*z + r*x - y,x*y - b*z]

sol = solve_ivp(evaluate, [0, 20], [0.1,0.1,0.1],dense_output=False)

t = np.linspace(0, 15, 100000)
z = sol.sol(t)
xx=z[0]
yy=z[1]
zz=z[2]

# fig = plt.figure(figsize=(10,7))
# ax=plt.axes(projection="3d")
# plt.style.use('dark_background')

# plt.plot(xx, yy, zz,'-',color='white',lw=0.8)

# # set limits
# # ax.set_xlim(-20,25)
# # ax.set_ylim(-25,20)
# # ax.set_zlim(0,50)

# # remove ticks
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])

# # make pane's have the same colors as background
# ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
# ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
# ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))

# ax.set_xlabel("X Axis")
# ax.set_ylabel("Y Axis")
# ax.set_zlabel("Z Axis")
# ax.set_title("Lorenz Attractor");
# ax.view_init(30, 120)

r1 = np.zeros(100000-1)
r2 = np.zeros(100000-1)
r3 = np.zeros(100000-1)
dt=15.0/100000
for i in range(100000-1):
  r1[i]=(np.log(abs((xx[i]-xx[i+1])/dt)))
  lambdas=(np.mean(result))
print(lambdas)





