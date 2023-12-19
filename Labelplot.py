import matplotlib.pyplot as plt 
from itertools import count
import csv,time,random
from matplotlib.animation import FuncAnimation

x= []
y= []

#with open('hw_200.csv','r') as csvfile: 
#lines = csv.reader(csvfile, delimiter=',') 
    
index = count()

def animate(i):
    
        x.append(next(index)) 
        y.append(float(random.randint(0,5))) 
        plt.cla
        plt.plot(x,y)

ani = FuncAnimation(plt.gcf(),animate,interval= 1000)




plt.tight_layout()
plt.show()