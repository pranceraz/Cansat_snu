import matplotlib.pyplot as plt 
from itertools import count
import csv,time,random
from matplotlib.animation import FuncAnimation

x= []
y= []
csv_file_path = "sample.csv"

   


index = count()
def animate(i):
        with open(csv_file_path,'r') as csvfile: 
                csv_reader = csv.reader(csvfile)      
                for row in csv_reader:
                        a=row[0]
                        y.append(float(a))
                        x.append(next(index)) 
                        print(y)

        plt.cla
        plt.plot(x,y)

ani = FuncAnimation(plt.gcf(),animate,interval= 1000)




plt.tight_layout()
plt.show()
