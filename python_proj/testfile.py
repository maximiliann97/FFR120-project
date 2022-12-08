import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice

lattice_size = 100
nSparrows = 100
nInsects = 50
sparrows = [Sparrow(lattice_size) for _ in range(nSparrows)]
insects = [Insects(lattice_size) for _ in range(nInsects)]
rice = Rice(lattice_size, 20)

def update(frame):
    rice_x = [field[0] for field in rice.fields]
    rice_y = [field[1] for field in rice.fields]
    rice_field = rice.fields
    rice_coords = rice_field[:, 0:2]
    produced_rice = 0

    sparrow_x = [sparrow.position[0] for sparrow in sparrows]
    sparrow_y = [sparrow.position[1] for sparrow in sparrows]
    insect_x = [insect.position[0] for insect in insects]
    insect_y = [insect.position[1] for insect in insects]
    [bird.move(rice_coords) for bird in sparrows]
    [insect.move(rice_coords) for insect in insects]

    plt.cla()
    plt.scatter(sparrow_x, sparrow_y, c='black', marker='^', s=50)
    plt.scatter(insect_x, insect_y, marker="^", c="lightgreen", s=10)
    plt.scatter(rice_x, rice_y, c='g', s=500, zorder=-1, marker='s')
    plt.title(f'Time step = {frame}')

    # for bird in sparrows:        # Birds eat
    #     true_array = np.all(bird.position == rice_coords, axis=1)
    #     if True in true_array:  # If bird at rice field
    #         rice_field_row = np.where(true_array == True)[0][0]
    #         if rice_field[rice_field_row, -1] > 0:
    #             bird.food(True)
    #             bird.move_random()
    #             rice.rice_gets_eaten(rice_field_row)
    #         else:
    #             bird.food(False)
    #     else:
    #         bird.food(False)
    #     if not bird.alive:
    #         sparrows.remove(bird)   # bird dies
    #
    #     # Animations
    # # Insects eat
    # produced_rice += sum(rice.fields[:, -1])
    # amount_rice = sum(rice.fields[:, -1])
    # rice.grow_rice()
    # n_birthed_birds = np.ceil(len(sparrows) * 0.015).astype(int)
    # sparrows += [Sparrow(lattice_size) for _ in range(n_birthed_birds)]
    # print(f'timestep = {t}, birthed birds = {n_birthed_birds}, nBirds = {len(sparrows)}\nrice={amount_rice}')

anim = animation.FuncAnimation(
    plt.figure(),  # The figure to animate
    update,  # The frame-generating function
    frames=100,  # The number of frames in the animation
    interval=100  # The interval between frames, in milliseconds
)

# Save the animation to a file
anim.save("animation.gif", writer="imagemagick")
