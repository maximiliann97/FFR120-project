import random
import matplotlib.pyplot as plt
import numpy as np

from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice


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
    for t in range(timesteps):
        for bird in sparrows:        # Birds move
            bird.move(rice_coords)
            plt.scatter(bird.position[0], bird.position[1], c='b', marker='^')
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

            # Animations

        plt.scatter(rice_field[:, 0], rice_field[:, 1], c='g', s=500, zorder=-1, marker='s')
        plt.pause(1)
        plt.clf()

        # Insects eat
        produced_rice += sum(rice.fields[:, -1])
        amount_rice = sum(rice.fields[:, -1])
        rice.grow_rice()
        n_birthed_birds = np.ceil(len(sparrows) * 0.015).astype(int)
        sparrows += [Sparrow(lattice_size) for _ in range(n_birthed_birds)]
        print(f'timestep = {t}, birthed birds = {n_birthed_birds}, nBirds = {len(sparrows)}\nrice={amount_rice}')


if __name__ == '__main__':
    main()
