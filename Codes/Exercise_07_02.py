import math
import pylab as pl
class pendulum:
    def __init__(self, omega_0 = 0, theta_1=0.2,theta_2=0.201, time_of_duration = 400, time_step = 0.04,g=9.8,length=9.8,q=1/2,F=0.5,D=2/3):
        # unit of time is second
        self.omega_1 = [omega_0]
        self.theta_1= [theta_1]
        self.omega_2 = [omega_0]
        self.theta_2= [theta_2]
        self.a=[math.log(abs(theta_2-theta_1))]
        self.t = [0]
        self.g=g
        self.length=length
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.q=q
        self.F=F
        self.D=D
    def calculate(self):
        for i in range(self.nsteps):
            self.omega_1.append(self.omega_1[i] -((self.g/self.length)*math.sin(self.theta_1[i])+self.q*self.omega_1[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.theta_1.append(self.theta_1[i] + self.omega_1[i+1]*self.dt)
            if self.theta_1[i+1]<-math.pi:
                self.theta_1[i+1]=self.theta_1[i+1]+2*math.pi
            if self.theta_1[i+1]>math.pi:
                self.theta_1[i+1]=self.theta_1[i+1]-2*math.pi
            else:
                pass
            self.omega_2.append(self.omega_2[i] -((self.g/self.length)*math.sin(self.theta_2[i])+self.q*self.omega_2[i]-self.F*math.sin(self.D*self.t[i]))*self.dt)
            self.theta_2.append(self.theta_2[i] + self.omega_2[i+1]*self.dt)
            if self.theta_2[i+1]<-math.pi:
                self.theta_2[i+1]=self.theta_2[i+1]+2*math.pi
            if self.theta_2[i+1]>math.pi:
                self.theta_2[i+1]=self.theta_2[i+1]-2*math.pi
            else:
                pass
            self.t.append(self.t[i] + self.dt)
            self.a.append(math.log(abs(self.theta_2[i+1]-self.theta_1[i+1])))
    def show_results(self):
        pl.plot(self.t, self.a)
        pl.xlabel('time ($s$)')
        pl.ylabel(' angle(radians)')
        pl.legend(loc='upper right',frameon = True)
        pl.grid(True)
        pl.show()
a = pendulum()
a.calculate()
a.show_results()
