Exercise_08:Poincare section and bifurcation diagram
========================================

标签： python
Student name: Zhang Boqi

Student number:2014301020063

---
![chaos butterfly][1]
**Abstract**
--------

 - In my last exercise, I write program to see what is chaos. Now we know that at small value of $F_D$,such as 0.5, it shows simple oscillatory motion,however, at big value of $F_D$ like 1.2 it shows chaotic motion.For our deeper research, in this exercise I will focus on Poincare section and bifurcation diagram, which are linked to problem 3.18 and 3.20, to see internal principle of routes to chaos.
 


----------

**Background**
----------

 - Equations for pendulum problems

From Euler—cromer method,we have

 $$\begin{cases}\omega_{i+1}=\omega_i-(\frac{g}{l}sin(\theta_i)-q\omega_i+F_Dsin(\Omega_Dt_i))\Delta{t}\\\\\theta_{i+1}=\theta_i+\omega_{i+1}\Delta{t}\\t_{i+1}=t_i+\Delta{t}\end{cases}$$ 

 - Poincare section
Poincare section is preferred When we need to plot and analyse the behavior of a dynamical system. To construct Poincare section, we plot points only when the phases of the driven force are fixed, to be more specific, we plot $\omega$ only at times that are in phase with the driving force. The time can be determined by $$\Omega_Dt=2n\pi$$
where n is an integer.


 - Bifurcation diagram helps to analyze the transition to chaos. It can show us lines for $\theta$ as a function of drive amplitude, which was constructed in the following manner. For each value of F_D we have calculated \theta as a function of time. After waiting for 300 driving periods so that the initial transients have decayed away, we plotted \theta at times that were in phase with the driving force as a function of F_D. Here we plotted points up to the 428th driving period. 
the Feigenbaum $\delta$ parameter can be calculate:
$$\delta_n=\frac{F_n-F_{n-1}}{F_{n+1}-F_n}$$

 


----------

**The Main body**
-------------

 -   Problem 3.20
Calculate the bifurcation diagrams for the pendulum in the vicinity of F_D=1.35 to 1.5. Make a magnified plot of the diagram (as compared to Figure 3.11) and obtain an estimate of the Feigenbaum $\delta$ parameter.

First of all, here are results for $\theta$ as a function of time for our pendulum for several different values of the drive amplitude.
![drive amplitude=1.2][2]
![different values of the drive amplitude][3]
[Click here to see the codes](https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Codes/Exercise_08_01.py)

From the running results, we can see that when drive amplitude is 1.2, the pendulum is at a chaotic state. However, when it refers to 1.35, we can see a regular plot(the sharp veriation is for that the angles is reset so as to keep it in range -$\pi$ to +$\pi$), also, we see that the period is the drive period. When it comes to 1.465, the period is four times the drive period.
When we see the two red figures on the right, it's amazing that the period go back to twice the drive period as we increase the drive amplitude.It seems that there exist a circle of period.

Now I use Bifurcation diagram to see more clear.
The range of $F_D$ is 1.35 to 1.5.
![][4]
[click here to see the code](https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Codes/Exercise_08_02.py) 

We can see that from 1.35 to 1.5, one value of drive amplitude linked to one, two or four value of $\theta$, which means the drive period, twice the drive period, four times the drive period. As the drive amplitude increase over 1.44, subsequently, the system run into a state of chaos, there isn't certain period. 

If the program get higher precision, we can read the value of driving force in the figure, as n approach to positive infinite, we can get $\delta$ =4.669.

 - Problem 3.21
First of all, change the value of driving frequency, we choose f=2/3,2/3+0.00001,2/3+0.00002
![change driving frequency][5]
we can find that the whole figure just move down.

Then we change the damping coefficient, we choose p=0.5,0.51,0.52
![change damping coefficient][6]
we can see that the whole figure just move towards the right, which means that the chaos is put off.




**References**
----------

 1. [Shan Tan's codes](http://www.jianshu.com/p/b141af43e303)
 2. [Yuqiao Wu's codes](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Chapter3---2/Exercise%209.md)


  [1]: https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Pictures/Exercise_08_01.jpg
  [2]: https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Pictures/Exercise_08_03.png
  [3]: https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Pictures/Exercise_08_02.png
  [4]: https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Pictures/Exercise_08_04.png
  [5]: https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Pictures/Exercise_08_05.png
  [6]: https://github.com/allenoel/compuational_physics_N2014301020063/blob/master/Pictures/Exercise_08_06.png