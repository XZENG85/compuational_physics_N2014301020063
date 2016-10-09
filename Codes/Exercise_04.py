import pylab as pl
class uranium_decay:
    def __init__(self, number_of_nuclei_A1 = 100,\
    number_of_nuclei_B1 = 0,time_constant_1 = 2,\
    time_constant_2 = 1, time_of_duration = 10,\
    time_step1 = 0.1,time_step2 = 0.05,number_of_nuclei_A2 = 100,number_of_nuclei_B2 = 0):
        # unit of time is second
        self.n11_uranium = [number_of_nuclei_A1 ]
        self.n21_uranium = [number_of_nuclei_B1 ]
        self.n12_uranium = [number_of_nuclei_A2 ]
        self.n22_uranium = [number_of_nuclei_B2 ]
        self.t = [0]
        self.tau1 = time_constant_1
        self.tau2 = time_constant_2
        self.dt1 = time_step1
        self.dt2 = time_step2
        self.time = time_of_duration
        self.nsteps1 = int(time_of_duration // time_step1 + 1)
        self.nsteps2 = int(time_of_duration // time_step2 + 1)
        print("Initial number of nuclei A1 ->", number_of_nuclei_A1)
        print("Initial number of nuclei B1 ->", number_of_nuclei_B1)
        print("Initial number of nuclei A2 ->", number_of_nuclei_A2)
        print("Initial number of nuclei B2 ->", number_of_nuclei_B2)
        print("Time constant A ->", time_constant_1)
        print("Time constant B ->", time_constant_2)
        print("time step1 -> ", time_step1)
        print("time step2 -> ", time_step2)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps1):
            tmp11 = self.n11_uranium[i] - self.n11_uranium[i] /self.\
            tau1 * self.dt1+self.n21_uranium[i] / self.tau2 * self.dt1
            tmp21 = self.n21_uranium[i] - self.n21_uranium[i] /self.\
            tau2 *self.dt1+self.n11_uranium[i] / self.tau1 * self.dt1
            tmp12 = self.n12_uranium[i] - self.n12_uranium[i] /\
            self.tau1 * self.dt2+self.n22_uranium[i] /\
            self.tau2 * self.dt2
            tmp22 = self.n22_uranium[i] - self.n22_uranium[i] /\
            self.tau2 *self.dt2+self.n12_uranium[i] /\
            self.tau1 * self.dt2
            self.n11_uranium.append(tmp11)
            self.n21_uranium.append(tmp21)
            self.n12_uranium.append(tmp12)
            self.n22_uranium.append(tmp22)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n11_uranium)
        pl.plot(self.t, self.n21_uranium)
        pl.plot(self.t, self.n12_uranium)
        pl.plot(self.t, self.n22_uranium)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei ')
        pl.legend(['$N_A$','$N_B$'])
        pl.show()
    def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n11_uranium[i], file = myfile)
            print(self.t[i], self.n21_uranium[i], file = myfile)
            print(self.t[i], self.n12_uranium[i], file = myfile)
            print(self.t[i], self.n22_uranium[i], file = myfile)
        myfile.close()
a = uranium_decay()
a.calculate()
a.show_results()
a.store_results()
