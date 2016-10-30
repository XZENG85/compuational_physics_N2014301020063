import math
import pylab as pl
class pendulum:
    def __init__(self, omega_0 = 0, theta_0=0.2, time_of_duration = 5000, time_step = 0.04,g=9.8,length=9.8,q=1/2,F=1.2,D=2/3):
        # unit of time is second
        self.omega_0 = [omega_0]
        self.theta_0 = [theta_0]
        self.t = [0]
        self.g=g
        self.length=length
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.q=q
        self.F=F
        self.D=D
        self.omega_1=[0]
        self.theta_1=[0]
    def calculate(self):
        for i in range(self.nsteps):
            self.omega_0.append(self.omega_0[i]-((self.g/self.length)*math.sin(self.theta_0[i])+self.q*self.omega_0[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.theta_0.append(self.theta_0[i] + self.omega_0[i+1]*self.dt)
            if self.theta_0[i+1]<-math.pi:
                self.theta_0[i+1]=self.theta_0[i+1]+2*math.pi
            if self.theta_0[i+1]>math.pi:
                self.theta_0[i+1]=self.theta_0[i+1]-2*math.pi
            else:
                pass
            self.t.append(self.t[i] + self.dt)
        for i in range(self.nsteps):
            if (self.t[i]-math.pi/4)%(2*math.pi/self.D)<0.02:
                self.omega_1.append(self.omega_0[i])
                self.theta_1.append(self.theta_0[i])
    def show_results(self):
        pl.plot( self.theta_1,self.omega_1,'.')
        pl.xlabel('omega(radians/s)')
        pl.ylabel(' theta(radians)')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)
        pl.show()
a = pendulum()
a.calculate()
a.show_results()
