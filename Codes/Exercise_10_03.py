import numpy as np
import matplotlib.pyplot as plt
import math
def orbits(x0,vy10,a,tt):
    au=149597870700.0
    yr=31558150.0
    G=6.67*10**(-11)
    Ms=1.989*10**(30)
    K=G*Ms
    x1=[]
    y1=[]
    vx1=[]
    vy1=[]
    vx1.append(0)
    vy1.append(vy10)
    x1.append(x0)
    y1.append(0)
    t=[]
    t.append(0)
    tau=0.00001
    t1=[]
    the=[]
    x2=[]
    y2=[]
    for i in range(tt):
        x1.append(x1[-1]+vx1[-1]*tau)
        y1.append(y1[-1]+vy1[-1]*tau)
        r1=math.sqrt((x1[-1])**2+(y1[-1])**2)
        vx1.append(vx1[-1]-4*math.pi**2*(x1[-1])*(1/r1**3+a/r1**5)*tau)
        vy1.append(vy1[-1]-4*math.pi**2*(y1[-1])*(1/r1**3+a/r1**5)*tau)
        t.append(t[-1]+tau)
        if abs(r1-x0)<0.000000005:
            t1.append(t[-1])
            the.append(math.atan(y1[-1]/x1[-1]))
            x2.append(x1[-1])
            y2.append(y1[-1])
    return x1,y1,x2,y2
x,y,t,tte=orbits(0.47,8.2,0.01,100000)
plt.plot(x,y)
for i in range(len(t)):
    plt.plot([0,t[i]],[0,tte[i]],color='black')
plt.title('the precession of mercury a=0.01')
plt.xlabel('X(AU)')
plt.ylabel('Y(AU)')
plt.show()
