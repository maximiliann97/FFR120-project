import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice


def update_scatterplot(sparrow_positions, rice_field, ax):
    """
    Function to update the scatter plot at each frame of the animation.

    Parameters
    ----------
    sparrow_positions : list
        List of tuples containing the (x, y) positions of the sparrows at a given timestep
    rice_field : numpy.ndarray
        Array containing the positions of the rice plants in the lattice
    ax : matplotlib.axes.Axes
        The axes object where the scatter plot will be drawn
    """
    ax.cla()  # Clear the existing plot
    for position in sparrow_positions:
        ax.scatter(position[0], position[1], c='b', marker='^')
    # Plot the rice plants in the lattice
    ax.scatter(rice_field[:, 0], rice_field[:, 1], c='g', marker='o')


def main():
    timesteps = 1000
    lattice_size = 100
    nSparrows = 100
    nInsects = 50
    sparrows = [Sparrow(lattice_size) for _ in range(nSparrows)]
    insects = [Insects(lattice_size) for _ in range(nInsects)]
    rice = Rice(lattice_size, 20)
    rice_field = rice.fields
    rice_coords = rice_field[:, 0:2]
    produced_rice = 0

    # Initialize the figure and axes object
    fig, ax = plt.subplots()

    # Initialize a list to store the positions of the sparrows at each timestep
    sparrow_positions = []

    # Loop through the timesteps
    for t in range(timesteps):
        for bird in sparrows:        # Birds move
            bird.move(rice_coords)
        # for insect in insects:
        #     insect.move(rice_field[:, 0:2])
        for bird in sparrows:        # Birds eat
            true_array = np.all(bird.position == rice_coords, axis=1)
            if True in true_array:  # If bird at rice field
                rice_field_row = np.where(true_array == True)[0][0]
                if rice_field[rice_field_row, -1] > 0:
                    bird.food(True)
                    bird.move_random()
                    rice.rice_gets_eaten(rice_field_row)
                else:
                    bird.food(False)
            else:
                bird.food(False)
            if not bird.alive:
                sparrows.remove(bird)   # bird dies

            # Store the positions of the sparrows at this timestep
            sparrow_positions.append([(sparrow.position[0], sparrow.position[1]) for sparrow in sparrows])

        # Insects eat
        produced_rice += sum(rice.fields[:, -1])
        amount_rice = sum(rice.fields[:, -1])
        rice.grow_rice()
        n_birthed_birds = np.ceil(len(sparrows) * 0.015).astype(int)
        sparrows += [Sparrow(lattice_size) for _ in range(n_birthed_birds)]
        print(f'timestep = {t}, birthed birds = {n_birthed_birds}, nBirds = {len(sparrows)}\nrice={amount_rice}')

    # Use FuncAnimation to generate the gif
    ani = animation.FuncAnimation(fig, update_scatterplot, frames=sparrow_positions, fargs=(ax, rice_field),
                                  interval=100)
    ani.save("your_gif.gif", writer="imagemagick")

if __name__ == '__main__':
    main()



