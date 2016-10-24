import math
import numpy
import pylab as pl
class cannon_shell:
    def __init__(self, x_0, y_0, initial_velocity, theta_0, \
                 time_step, total_time,target_altitude,wind_speed):
        self.theta = theta_0
        self.v = [initial_velocity]
        self.x = [x_0]
        self.y = [y_0]
        self.v_x = [math.cos(theta_0 * math.pi / 180) * initial_velocity-\
        wind_speed]
        self.v_y = [math.sin(theta_0 * math.pi / 180) * initial_velocity]
        self.g = 9.8
        self.dt = time_step
        self.time = total_time
        self.a= 6.5*pow(10.0,-3)
        self.alpha = 2.5
        self.T_0 = 300
        self.Bm = 4.0*pow(10.0,-5)
        self.target_altitude = target_altitude
    def calculate(self):
        for i in range(self.time):
             self.v_x.append(self.v_x[-1]-self.Bm*\
             pow(1-(self.a/self.T_0)*self.y[-1],self.alpha)*self.v_x[-1]*self.v[-1]*self.dt)
             self.x.append(self.x[-1] + self.dt * self.v_x[-1])
             self.v_y.append(self.v_y[-1]-self.Bm*\
             pow(1-(self.a/self.T_0)*self.y[-1],self.alpha)*self.v_y[-1]*self.v[-1]*\
             self.dt - self.g * self.dt)
             self.y.append(self.y[-1] + self.dt * self.v_y[-1])
             if len(self.y)>2 and self.y[-1]<200 and self.y[-2]>=200:
                 break
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.title('Trajectory of cannon shell', fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.text(self.x[50], self.y[50],\
        str(self.v)+'m/s',fontdict = font) 
for j in numpy.linspace(100, 900, 9):
    a = cannon_shell(0 , 0, j, 45, 0.1,2000,300,8)
    a.calculate()
    a.show_results()    
