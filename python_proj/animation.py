import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Sparrow import Sparrow
from insects import insects
#import Sparrow
import insects
import numpy as np

fig = plt.figure(figsize=(7,7))

lattice_size = 100
nSparrows = 30
sparrow = [Sparrow(lattice_size) for _ in range(nSparrows)]
Insects = []
x,y = [], []

def animate(i):
    #sparrow.append(Sparrow(lattice_size))
    #Insects.append(insects(lattice_size))
    x.append(random.randint(2,lattice_size))
    y.append(random.randint(2,lattice_size))
    lastx = x.pop()
    lasty = y.pop()
    for i in range(100) :
        x.append(lastx+random.randint(1,3))
        y.append(lasty+random.randint(1,3))
        #plt.style.use("ggplot")    
        plt.scatter(x,y,c='g')
    #plt.scatter(sparrow.position,c='b')
    #plt.scatter(Insects.position,c='r')
#test code to include obj
sparrow.append(Sparrow(lattice_size))
#Insects.append(insects(lattice_size))
ani = FuncAnimation(fig, animate, interval=300)
plt.show()