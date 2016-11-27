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
            the.append(math.acos(x1[-1]/r1))
            x2.append(x1[-1])
            y2.append(y1[-1])
    return x1,y1,t1,the
def fit(x,y):
  if len(x)!=len(y):
    return 0,0
  else:
    xx=0
    yy=0
    xy=0
    x22=0
    for i in range(len(x)):
        xx=xx+x[i]
        yy=yy+y[i]
        xy=xy+x[i]*y[i]
        x22=x22+x[i]**2
    xx=xx/len(x)
    yy=yy/len(x)
    xy=xy/len(x)
    x22=x22/len(x)
    ta=(xx*yy-len(x)*xy)/(xx**2-len(x)*x22)
    tb=(xx*xy-x22*yy)/(xx**2-len(x)*x22)
    return ta,tb

tr=[]
tu=0.00000001
for k in range(4):
    tr.append(0.79798535+tu*k)
v=[]
tc=[]
for j in tr:
    vc=8.2/math.sqrt(0.794/1.206)
    v.append(math.sqrt((1-j)/(1+j))*vc)
ax1=plt.subplot(221)
ax2=plt.subplot(222)
ax3=plt.subplot(223)
ax4=plt.subplot(224)
plt.sca(ax1)
x,y,t,tte=orbits(0.47,v[0],0.0008,1000000)
plt.plot(x,y)
for k in range(len(t)):
    plt.plot([0,t[k]],[0,tte[k],], color ='red')
plt.xlabel('x/yr')
plt.ylabel('y/yr')
plt.title('the precession with different eccentricity 0.7979852')
plt.sca(ax2)
x,y,t,tte=orbits(0.47,v[1],0.0008,1000000)
plt.plot(x,y)
for k in range(len(t)):
    plt.plot([0,t[k]],[0,tte[k],], color ='red')
plt.xlabel('x/yr')
plt.ylabel('y/yr')
plt.title('the precession with different eccentricity 0.79798525')
plt.sca(ax3)
x,y,t,tte=orbits(0.47,v[2],0.0008,1000000)
plt.plot(x,y)
for k in range(len(t)):
    plt.plot([0,t[k]],[0,tte[k],], color ='red')
plt.xlabel('x/yr')
plt.ylabel('y/yr')
plt.title('the precession with different eccentricity 0.79798530')
plt.sca(ax4)
x,y,t,tte=orbits(0.47,v[3],0.0008,1000000)
plt.plot(x,y)
for k in range(len(t)):
    plt.plot([0,t[k]],[0,tte[k],], color ='red')
plt.xlabel('x/yr')
plt.ylabel('y/yr')
plt.title('the precession with different eccentricity 0.79798535')
plt.show()
