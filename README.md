# Economics-Meets-ML
# defining 5 arms using gaussian classes
import random
import math
import numpy as np
import matplotlib.pyplot as plt
class Arm:
    def __init__(self,average,standard_deviation):
        self.average = average
        self.sd=standard_deviation
        self.nt=0 #number of pulls of a particular arm
        self.rt = 0 # average till then


    def pull_arm(self,t=1):
        self.nt +=1
        self.deltat = math.sqrt(8*(math.log(t))/self.nt)
        self.pull = random.gauss(self.average,self.sd)
        self.rt= (self.pull)/self.nt        
        return self.pull
# def ucb(self):
    #     self.ucb = self.rt+self.deltat
    #     return self.ucb




horizons = np.linspace(1000,100000,10) # [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, ..., 10000]
total_regrets = []

for horizon in horizons:
    arm1 = Arm(0.2,0.01)
    arm2 = Arm(0.3,0.01)
    arm3 = Arm(0.6,0.01)
    pull1 = arm1.pull_arm()
    pull2 = arm2.pull_arm()
    pull3 = arm3.pull_arm()
    t = 3 # total number of pulls of all arms
    T= horizon
    i=0
    arm1.ucb = arm1.deltat+ arm1.rt
    arm2.ucb = arm1.deltat + arm2.rt
    arm3.ucb = arm3.deltat + arm3.rt
    regret = 0
    p=1
    periods=floor;np.floor
    while (i<T):
        
        
        if max(arm1.ucb,arm2.ucb,arm3.ucb)==arm1.ucb:
            t +=1
            reward = arm1.pull_arm(t)
            arm1.ucb = arm1.deltat + arm1.rt
            arm2.ucb = arm1.deltat + arm2.rt
            arm3.ucb = arm3.deltat + arm3.rt
            print(f"we played arm 1 and arm1ucb= {arm1.ucb} arm2ucb = {arm2.ucb} arm3ucb = {arm3.ucb}")
            i+=1

        if max(arm1.ucb,arm2.ucb,arm3.ucb)==arm2.ucb:
            t +=1
            reward = arm2.pull_arm(t)
            arm2.ucb = arm2.deltat + arm2.rt
            arm2.ucb = arm1.deltat + arm2.rt
            arm3.ucb = arm3.deltat + arm3.rt
            print(f"we played arm 2 and arm1ucb= {arm1.ucb} arm2ucb = {arm2.ucb} arm3ucb = {arm3.ucb}")
            i+=1

        if max(arm1.ucb,arm2.ucb,arm3.ucb)==arm3.ucb:
            t +=1
            reward = arm3.pull_arm(t)
            arm3.ucb = arm3.deltat + arm3.rt
            arm2.ucb = arm1.deltat + arm2.rt
            arm3.ucb = arm3.deltat + arm3.rt
            print(f"we played arm 3 and arm1ucb= {arm1.ucb} arm2ucb = {arm2.ucb} arm3ucb = {arm3.ucb}")
            i+=1
            
        regret += max(arm1.average,arm2.average,arm3.average) - reward
    total_regrets.append(regret)
        


plt.plot(horizons,total_regrets)
plt.xlabel("Horizon")
plt.ylabel("Total Regret")
plt.show()

