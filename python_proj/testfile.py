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

    sparrows_coords_array = np.array([[x, y] for x, y in zip(sparrow_x, sparrow_y)])
    insects_coords_array = np.array([[x, y] for x, y in zip(insect_x, insect_y)])

    # Loop through each sparrow
    for bird in sparrows:
        # Check if the bird is at the rice field or at an insect position
        if np.any(np.all(bird.position == rice_coords_array, axis=1)) and np.any(np.all(bird.position == insects_coords_array, axis=1)):

            # Generate a random number
            r = np.random.rand()

            # If the random number is less than 0.5, feed the bird with rice
            if r < 0.5:

                # Find the row in the rice field where the bird is
                rice_field_row = np.where(np.all(bird.position == rice_coords_array, axis=1))[0][0]

                # If there is rice at that location, feed the bird and move it to a new location
                if rice_field[rice_field_row, -1] > 0:
                    bird.food(True)
                    bird.move_random()
                    rice.rice_gets_eaten(rice_field_row)

                # If the random number is not less than 0.5, feed the bird with an insect
                else:
                    # Find the row in the insects_coords_array where the bird is
                    insect_row = np.where(np.all(bird.position == insects_coords_array, axis=1))[0][0]

                    # Set the insect in that position to dead
                    insects[insect_row].alive = False
                    insects.remove(insects[insect_row])
                    print(len(insects))
                    bird.food(True)
                    bird.move_random()
            else:
                bird.food(True)
                bird.move_random()
                # Should eat insect here and change insect to dead

        # If the bird is at the rice field but not at an insect position
        elif np.any(np.all(bird.position == rice_coords_array, axis=1)) and not np.any(
            np.all(bird.position == insects_coords_array, axis=1)):
            rice_field_row = np.where(np.all(bird.position == rice_coords_array, axis=1))[0][0]

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
