#### Steps performed to obtain the following results:
- The numerical solution for the given system was calculated for a given set of initial values $`x,y,u,v`$
- Another numerical solution was found by incrementing the intial values by a small amount $`d_{0}=1 \times 10^{-5}$ ie $x+d_{0},y+d_{0},u+d_{0},v+d_{0} `$
- In the first plot the distance between the solution points $`x,y`$ was calculated, at each point in time, for all the solution points ie $`d=\sqrt{(x_{1}-x_{2})^2+(y_{1}-y_{2})^2}`$
- In the next plot we plot, $`log_{e}(d/d_{0})`$
- I've also done a linear regression and it has been plotted.
- Theoretically if the regression gives $ax+b$ then a is the lyapunov constant.
![lyapunov-4 0](https://user-images.githubusercontent.com/29148711/123992355-2e295480-d9e9-11eb-9833-08af001c28a4.png)
![lyapunov-3 466666666666667](https://user-images.githubusercontent.com/29148711/123992384-32557200-d9e9-11eb-8bb7-d878b696996e.png)
![lyapunov-2 9333333333333336](https://user-images.githubusercontent.com/29148711/123992405-371a2600-d9e9-11eb-994f-2e9b81756633.png)
![lyapunov-2 4](https://user-images.githubusercontent.com/29148711/123992465-4305e800-d9e9-11eb-99be-b47d723ac445.png)
![lyapunov-1 8666666666666667](https://user-images.githubusercontent.com/29148711/123992475-46996f00-d9e9-11eb-9d52-ef3636f06494.png)
![lyapunov-1 3333333333333335](https://user-images.githubusercontent.com/29148711/123992484-48fbc900-d9e9-11eb-8bbb-a136449b99c0.png)
![lyapunov-0 7999999999999998](https://user-images.githubusercontent.com/29148711/123992517-5022d700-d9e9-11eb-9931-d56b3eed8200.png)
![lyapunov-0 2666666666666666](https://user-images.githubusercontent.com/29148711/123992533-531dc780-d9e9-11eb-91a3-66d4c1947171.png)
![lyapunov0 2666666666666666](https://user-images.githubusercontent.com/29148711/123992587-5fa22000-d9e9-11eb-82c7-c02c444a53a5.png)
![lyapunov0 7999999999999998](https://user-images.githubusercontent.com/29148711/123992629-6a5cb500-d9e9-11eb-873d-79f0926d8f14.png)
![lyapunov1 333333333333333](https://user-images.githubusercontent.com/29148711/123992677-73e61d00-d9e9-11eb-906a-4cf37c3f5bfc.png)
![lyapunov1 8666666666666663](https://user-images.githubusercontent.com/29148711/123992833-9415dc00-d9e9-11eb-8da8-0292a3ca920f.png)
![lyapunov2 4000000000000004](https://user-images.githubusercontent.com/29148711/123992877-9c6e1700-d9e9-11eb-955b-300bc09aeb57.png)
![lyapunov2 9333333333333336](https://user-images.githubusercontent.com/29148711/123992914-a3952500-d9e9-11eb-8e24-d544a41c7fee.png)
![lyapunov3 466666666666667](https://user-images.githubusercontent.com/29148711/123993269-eb1bb100-d9e9-11eb-8aa4-75cc708f158b.png)
![lyapunov4 0](https://user-images.githubusercontent.com/29148711/123993307-f1119200-d9e9-11eb-992a-000698525339.png)
