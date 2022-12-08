import random
import matplotlib.pyplot as plt
import numpy as np

from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice

def main():

    timesteps = 200
    lattice_size = 100
    nSparrows = 100
    nInsects = 50
    sparrow = [Sparrow(lattice_size) for _ in range(nSparrows)]
    insects = [Insects(lattice_size) for _ in range(nInsects)]
    rice = Rice(lattice_size, 20)
    rice_field = rice.fields
    rice_coords = rice_field[:, 0:2]

    for t in range(timesteps):
        for bird in sparrow:
            bird.move(rice_field[:, 0:2])
            true_array = np.all(bird.position == rice_coords, axis=1)
            if True in true_array:
                rice.rice_gets_eaten(bird.position)






if __name__ == '__main__':
    main()