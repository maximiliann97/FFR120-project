import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(15,15))


x,y = [], []
def animate(i):
    x.append(random.randint(2,20))
    y.append(random.randint(2,20))
    #plt.style.use("ggplot")    
    plt.scatter(x,y,c='g')

ani = FuncAnimation(fig, animate, interval=300)
plt.show()