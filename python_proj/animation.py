import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(7,7))


x,y = [], []
def animate(i):
    x.append(random.randint(2,100))
    y.append(random.randint(2,100))
    lastx = x.pop()
    lasty = y.pop()
    for i in range(100) :
        x.append(lastx+random.randint(1,3))
        y.append(lasty+random.randint(1,3))
        #plt.style.use("ggplot")    
        plt.scatter(x,y,c='g')

ani = FuncAnimation(fig, animate, interval=300)
plt.show()