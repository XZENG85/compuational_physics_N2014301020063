from __future__ import division
import math
import pylab as pl
import numpy
# define a function that given amplitude of force, gives angle,avelo and t
def change_amp(F):   
    # define some constants
    q = 0.5
    l = 9.8
    g = 9.8
    f = 2/3
    dt = math.pi/100
    theta0 = 0.2
    omega0 = 0
    angle = [theta0]
    avelo = [omega0]
    t = [0]
    an=[]
    # move the pendulum
    while t[-1] <= 1200*math.pi:
        avelo_new = avelo[-1] - ((g/l)*math.sin(angle[-1]) + q*avelo[-1] - F*math.sin(f*t[-1]))*dt
        avelo.append(avelo_new)
        angle_new = angle[-1] + avelo[-1]*dt
        while angle_new > math.pi:
            angle_new -= 2*math.pi
        while angle_new < -math.pi:
            angle_new += 2*math.pi
        angle.append(angle_new)
        if t[-1]>=900*math.pi:
            if t[-1]%(3*math.pi)<=dt:
                an.append(angle_new)
        t_new = t[-1] + dt
        t.append(t_new)
    return an
fd1=list(numpy.linspace(1.35,1.5,100))
fd=[]
th=[]
for i in fd1:
    points=change_amp(i)
    for j in points:
        fd.append(i)
        th.append(j)
pl.scatter(fd,th,s=10)
pl.grid(True)
pl.xlim(1.35,1.48)
pl.ylim(0,3)
pl.title('Bifurcation diagram')
pl.xlabel('FD')
pl.ylabel('theta(radians)')
pl.show()
