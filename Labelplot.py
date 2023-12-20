import matplotlib.pyplot as plt 
from itertools import count
import csv,time,random
from matplotlib.animation import FuncAnimation

x= []
y= []
csv_file_path = "sample.csv"


def animate(i):
        x_val = 1000
        with open(csv_file_path,'r') as csvfile: 
                csv_reader = csv.reader(csvfile)      
                for row in csv_reader:
                        a=row[0]
                        
                        y.append(a)
                        x.append(x_val)
                        x_val+=1

                        print(x)

        plt.cla
        plt.plot(x,y)
# gotta add vals to csv file to make it work longer 
# change x axis to UTC 
ani = FuncAnimation(plt.gcf(),animate,interval= 1000)




plt.tight_layout()
plt.show()
