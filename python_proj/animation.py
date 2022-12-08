import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice
import numpy as np
fig = plt.figure(figsize=(7, 7))

lattice_size = 100
nSparrows = 100
nInsects = 50
sparrow = [Sparrow(lattice_size) for _ in range(nSparrows)]
insects = [Insects(lattice_size) for _ in range(nInsects)]
rice_field = Rice(lattice_size, 20).fields
x, y = [], []


# def animate(i):
for i in range(200):
    for bird in sparrow:
        plt.scatter(bird.position[0], bird.position[1], c='b',marker='^')
        bird.move(rice_field[:, 0:2])
    plt.scatter(rice_field[:, 0], rice_field[:, 1], c='g', s=500, zorder=-1, marker='s')
    plt.pause(0.01)
    plt.clf()



# ani = FuncAnimation(fig, animate, interval=100)


