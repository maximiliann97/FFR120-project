import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice
from tqdm import trange


def run_simulation():
    # Eco system parameters
    kill_rate = 0.01

    sparrow_growth_rate = 0.015
    sparrow_starvation_threshold = 3
    sparrow_age_limit = 75

    insect_growth_rate = 0.015
    insect_starvation_threshold = 4
    insect_age_limit = 75


    start_rice = 200
    rice_growth_per_day = 50

    # Initialize
    timesteps = 500
    time = np.linspace(0, timesteps, timesteps+1)
    lattice_size = 100
    nSparrows = 100
    nInsects = 110
    sparrows = [Sparrow(lattice_size, sparrow_starvation_threshold, sparrow_age_limit) for _ in range(nSparrows)]
    insects = [Insects(lattice_size, insect_starvation_threshold, insect_age_limit) for _ in range(nInsects)]
    rice = Rice(lattice_size, start_rice, rice_growth_per_day)

    sparrow_pop = []
    insect_pop = []
    rice_pop = []

    # Add populations at timestep 0
    sparrow_pop.append(len(sparrows))
    insect_pop.append(len(insects))
    rice_pop.append(np.sum(rice.fields[:, -1]))


    for t in trange(timesteps):
        rice_field = rice.fields
        rice_coords_array = rice_field[:, 0:2]

        insect_x = [insect.position[0] for insect in insects]
        insect_y = [insect.position[1] for insect in insects]
        [bird.move(rice_coords_array) for bird in sparrows]
        [insect.move(rice_coords_array) for insect in insects]

        # Sparrow eat loop
        for bird in sparrows:
            if bird.hungry:
                insects_coords_array = np.array([[x, y] for x, y in zip(insect_x, insect_y)])
                true_rice = np.all(bird.position == rice_coords_array, axis=1)
                true_insect = np.all(bird.position == insects_coords_array, axis=1)
                # if the bird is at the rice field and at an insect position
                if np.any(true_rice) and np.any(true_insect):

                    # Generate a random number
                    r = np.random.rand()

                    # If the random number is less than 0.5, feed the bird with rice
                    if r < 0.5:

                        # Find the row in the rice field where the bird is
                        rice_field_row = np.where(true_rice == True)[0][0]

                        # If there is rice at that location, feed the bird and move it to a new location
                        if rice_field[rice_field_row, -1] > 0:
                            bird.food(True)
                            bird.move_random()
                            rice.rice_gets_eaten(rice_field_row)

                        # If there is no rice at the rice field eat insect
                        else:
                            # Find the row in the insects_coords_array where the bird is
                            insect_row = np.where(true_insect == True)[0][0]

                            # Remove insect from list
                            if len(insects) > 0:
                                insects.remove(insects[insect_row])
                                bird.food(True)
                                bird.move_random()

                    # If the random number is not less than 0.5, feed the bird with an insect
                    else:

                        # Find the row in the insects_coords_array where the bird is
                        insect_row = np.where(true_insect == True)[0][0]

                        # Set the insect in that position to dead
                        if len(insects) > 0:
                            insects.remove(insects[insect_row])
                            # Must update coordinates when an insect is removed from population
                            insect_x = [insect.position[0] for insect in insects]
                            insect_y = [insect.position[1] for insect in insects]
                            bird.food(True)
                            bird.move_random()

                        else:
                            # Find the row in the rice field where the bird is
                            rice_field_row = np.where(true_rice == True)[0][0]

                            # If there is rice at that location, feed the bird and move it to a new location
                            if rice_field[rice_field_row, -1] > 0:
                                bird.food(True)
                                bird.move_random()
                                rice.rice_gets_eaten(rice_field_row)

                # If the bird is at the rice field but not at an insect position
                elif np.any(true_rice) and not np.any(true_insect):
                    rice_field_row = np.where(true_rice == True)[0][0]

                    if rice_field[rice_field_row, -1] > 0:  # There is rice to eat
                        bird.food(True)
                        bird.move_random()
                        rice.rice_gets_eaten(rice_field_row)
                    else:  # There is no rice
                        bird.food(False)

                # If the bird is not at a rice field but in an insect position
                elif not np.any(true_rice) and np.any(true_insect):
                    # Find the row in the insects_coords_array where the bird is
                    insect_row = np.where(true_insect == True)[0][0]
                    """
                    print(f'insect index = {insect_row}, length of insects list = {len(insects)}')
                    """
                    # Set the insect in that position to dead
                    if len(insects) > 0:
                        insects.remove(insects[insect_row])
                        # Must update coordinates when an insect is removed from population
                        insect_x = [insect.position[0] for insect in insects]
                        insect_y = [insect.position[1] for insect in insects]
                        bird.food(True)
                        bird.move_random()
                # No rice or insect
                else:
                    bird.food(False)

            # Remove birds that died from population
            if not bird.alive:
                sparrows.remove(bird)   # bird dies

        # Insects eat loop
        for insect in insects:
            true_rice = np.all(insect.position == rice_coords_array, axis=1)
            if np.any(true_rice):
                rice_field_row = np.where(true_rice == True)[0][0]
                if rice_field[rice_field_row, -1] > 0:
                    insect.food(True)
                    rice.rice_gets_eaten(rice_field_row)
            else:
                insect.food(False)

            if insect.aged():
                insects.remove(insect)


        """
        # Pest control
        n_dead_sparrows = np.ceil(kill_rate * len(sparrows)).astype(int)
        """

        # Birth new sparrows
        num_new_sparrows = np.ceil(len(sparrows) * sparrow_growth_rate).astype(int)
        new_sparrows = [Sparrow(lattice_size, sparrow_starvation_threshold, sparrow_age_limit) for _ in range(num_new_sparrows)]

        for ns in new_sparrows:
            sparrows.append(ns)

        # Birth new insects
        num_new_insects = np.ceil(len(insects) * insect_growth_rate).astype(int)
        new_insects = [Insects(lattice_size, insect_starvation_threshold, insect_age_limit) for _ in range(num_new_insects)]
        for ni in new_insects:
            insects.append(ni)
        amount_rice = np.sum(rice.fields[:, -1])
        rice.grow_rice()

        # Add populations to plot
        sparrow_pop.append(len(sparrows))
        insect_pop.append(len(insects))
        rice_pop.append(amount_rice)

    # Plots
    plt.plot(time, sparrow_pop)
    plt.plot(time, insect_pop)
    plt.plot(time, rice_pop)
    plt.xlabel('t')
    plt.ylabel('Population')
    plt.legend(['Sparrow population', 'Insect population', 'Amount of rice'])
    plt.title(f'Time evolution of populations of Sparrows, insects and rice \n with killing rate of sparrows = {kill_rate}')
    plt.gca()
    plt.show()