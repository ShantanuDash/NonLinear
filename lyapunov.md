#### Steps performed to obtain the following results:
- The numerical solution for the given system was calculated for a given set of initial values $x,y,u,v$
- Another numerical solution was found by incrementing the intial values by a small amount $d_{0}=1 \times 10^{-5}$ ie $x+d_{0},y+d_{0},u+d_{0},v+d_{0} $
- In the first plot the distance between the solution points $x,y$ was calculated, at each point in time, for all the solution points ie $d=\sqrt{(x_{1}-x_{2})^2+(y_{1}-y_{2})^2}$
- In the next plot we plot, $log_{e}(d/d_{0})$
- I've also done a linear regression and it has been plotted.
- Theoretically if the regression gives $ax+b$ then a is the lyapunov constant.
