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
    produced_rice = 0
    rice_x = [field[0] for field in rice.fields]
    rice_y = [field[1] for field in rice.fields]
    rice_field = rice.fields
    rice_coords_array = rice_field[:, 0:2]

    sparrow_x = [sparrow.position[0] for sparrow in sparrows]
    sparrow_y = [sparrow.position[1] for sparrow in sparrows]
    insect_x = [insect.position[0] for insect in insects]
    insect_y = [insect.position[1] for insect in insects]
    [bird.move(rice_coords_array) for bird in sparrows]
    [insect.move(rice_coords_array) for insect in insects]

    plt.cla()
    plt.scatter(sparrow_x, sparrow_y, c='black', marker='^', s=50)
    plt.scatter(insect_x, insect_y, marker="^", c="lightgreen", s=10)
    plt.scatter(rice_x, rice_y, c='g', s=500, zorder=-1, marker='s')
    plt.title(f'Time step = {frame}')

    for bird in sparrows:        # Birds eat
        true_rice = np.all(bird.position == rice_coords_array, axis=1)
        true_insect = np.all(bird.position == insects_coords_array, axis=1)

        if True in true_rice and True in true_insect:  # If bird at rice field and insect position
            r = np.random.rand()
            if r < 0.5:     # Bird eats rice
                rice_field_row = np.where(true_rice == True)[0][0]
                if rice_field[rice_field_row, -1] > 0:  # There is rice to eat
                    bird.food(True)
                    bird.move_random()
                    rice.rice_gets_eaten(rice_field_row)
                else:       # There is no rice but still an insect
                    bird.food(True)
                    bird.move_random()
                    # Should eat insect here and change insect to dead
            else:
                bird.food(True)
                bird.move_random()
                # Should eat insect here and change insect to dead

        elif True in true_rice and not True in true_insect:     # There is rice in position but not insect
            rice_field_row = np.where(true_rice == True)[0][0]
            if rice_field[rice_field_row, -1] > 0:  # There is rice to eat
                bird.food(True)
                bird.move_random()
                rice.rice_gets_eaten(rice_field_row)
            else:  # There is no rice
                bird.food(False)

        else:   # No rice or insect
            bird.food(False)
        if not bird.alive:
            sparrows.remove(bird)   # bird dies

    num_new_sparrows = np.ceil(len(sparrows) * 0.015).astype(int)
    new_sparrows = [Sparrow(lattice_size) for _ in range(num_new_sparrows)]
    for ns in new_sparrows:
        sparrows.append(ns)
    rice.grow_rice()


anim = animation.FuncAnimation(
    plt.figure(),  # The figure to animate
    update,  # The frame-generating function
    frames=100,  # The number of frames in the animation
    interval=100  # The interval between frames, in milliseconds
)

# Save the animation to a file
# anim.save("animation.gif", writer="imagemagick")
plt.show()
