import matplotlib.pyplot as plt
import numpy as np
from Sparrow import Sparrow
from Insects import Insects
from Rice import Rice
from tqdm import trange


def run_simulation():
    # Eco system parameters
    kill_rate_sparrows = 0.017
    kill_rate_insects = 0.03

    sparrow_growth_rate = 0.025
    sparrow_starvation_threshold = 3
    sparrow_age_limit = 75

    insect_growth_rate = 0.015
    insect_starvation_threshold = 3
    insect_age_limit = 75
    insect_emerge_prob = 0.2

    start_rice = 1000
    rice_growth_per_day = 50
    rice_vs_insect_prob = 0.1

    # Initialize
    nIterations = 100
    timesteps = 1400
    time = np.reshape(np.arange(timesteps), [1, timesteps])
    lattice_size = 100
    nSparrows = 200
    nInsects = 100

    sparrow_pop = np.zeros([1, timesteps])
    insect_pop = np.zeros([1, timesteps])
    rice_pop = np.zeros([1, timesteps])

    # Add populations at timestep 0
    sparrow_pop[0, 0] = nSparrows * nIterations
    insect_pop[0, 0] = nInsects * nIterations
    rice_pop[0, 0] = start_rice*5 * nIterations

    for it in trange(nIterations):
        sparrows = [Sparrow(lattice_size, sparrow_starvation_threshold, sparrow_age_limit) for _ in range(nSparrows)]
        insects = [Insects(lattice_size, insect_starvation_threshold, insect_age_limit) for _ in range(nInsects)]
        rice = Rice(lattice_size, start_rice, rice_growth_per_day)

        for t in trange(1, timesteps):
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

                        # If the random number is less than 0.1, feed the bird with rice
                        if r < rice_vs_insect_prob:

                            # Find the row in the rice field where the bird is
                            rice_field_row = np.where(true_rice == True)[0][0]

                            # If there is rice at that location, feed the bird and move it to a new location
                            if rice_field[rice_field_row, -1] > 0:
                                bird.food(True)
                                bird.move_random()
                                rice.rice_gets_eaten(rice_field_row, "sparrow")

                            # If there is no rice at the rice field eat insect
                            else:
                                try:
                                    # Find the row in the insects_coords_array where the bird is
                                    insect_row = np.where(true_insect == True)[0][0]

                                    # Remove insect from list
                                    if len(insects) > 0:
                                        insects.remove(insects[insect_row])
                                        bird.food(True)
                                        bird.move_random()
                                except IndexError:
                                    pass

                        # If the random number is not less than 0.5, feed the bird with an insect
                        else:

                            # Find the row in the insects_coords_array where the bird is
                            insect_row = np.where(true_insect == True)[0][0]

                            # Set the insect in that position to dead
                            if len(insects) > 0:
                                try:
                                    insects.remove(insects[insect_row])
                                    # Must update coordinates when an insect is removed from population
                                    insect_x = [insect.position[0] for insect in insects]
                                    insect_y = [insect.position[1] for insect in insects]
                                    bird.food(True)
                                    bird.move_random()
                                except IndexError:
                                    pass

                            else:
                                # Find the row in the rice field where the bird is
                                rice_field_row = np.where(true_rice == True)[0][0]

                                # If there is rice at that location, feed the bird and move it to a new location
                                if rice_field[rice_field_row, -1] > 0:
                                    bird.food(True)
                                    bird.move_random()
                                    rice.rice_gets_eaten(rice_field_row, "sparrow")

                    # If the bird is at the rice field but not at an insect position
                    elif np.any(true_rice) and not np.any(true_insect):
                        rice_field_row = np.where(true_rice == True)[0][0]

                        if rice_field[rice_field_row, -1] > 0:  # There is rice to eat
                            bird.food(True)
                            bird.move_random()
                            rice.rice_gets_eaten(rice_field_row, "sparrow")
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

                bird.aged()       # bird ages
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
                        rice.rice_gets_eaten(rice_field_row, "insect")
                        #insect.move_random()
                else:
                    insect.food(False)

                if insect.aged():
                    insects.remove(insect)

            # Pest control
            n_dead_sparrows = np.floor(kill_rate_sparrows * len(sparrows)).astype(int)
            del sparrows[0:n_dead_sparrows]

            n_dead_insects = np.floor(kill_rate_insects * len(insects)).astype(int)
            del insects[0:n_dead_insects]

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

            # Probability that insect reemerge
            if np.random.rand() < insect_emerge_prob:
                # for i in range(1, 2):
                insects.append(Insects(lattice_size, insect_starvation_threshold, insect_age_limit))
            # Grow rice
            amount_rice = np.sum(rice.fields[:, -1])
            rice.grow_rice()

            # Add populations to plot
            sparrow_pop[0, t] += len(sparrows)
            insect_pop[0, t] += len(insects)
            rice_pop[0, t] += amount_rice

    avg_sparrow_pop = sparrow_pop / nIterations
    avg_insect_pop = insect_pop / nIterations
    avg_rice_pop = rice_pop / nIterations

    rice_array = np.asarray(avg_rice_pop)
    sparrow_array = np.asarray(avg_sparrow_pop)
    insect_array = np.asarray(avg_insect_pop)

    np.save(f'rice_pop_SK={kill_rate_sparrows}IK={kill_rate_insects}, it = {nIterations}', rice_array)
    np.save(f'sparrow_pop_SK={kill_rate_sparrows}IK={kill_rate_insects}, it = {nIterations}', sparrow_array)
    np.save(f'insect_pop_SK={kill_rate_sparrows}IK={kill_rate_insects}, it = {nIterations}', insect_array)

    # Plots
    plt.subplot(1, 2, 1)
    plt.plot(time[0], avg_sparrow_pop[0])
    plt.plot(time[0], avg_insect_pop[0])
    plt.xlabel('t', fontsize=18)
    plt.ylabel('Population', fontsize=18)
    plt.tick_params(labelsize=18)
    plt.legend(['Sparrow population', 'Insect population'], fancybox=True, shadow=True, fontsize=20)
    #plt.title(f'Time evolution of populations of Sparrows and insects \n averaged over {nIterations} iterations', fontsize=18)
    plt.gca()

    plt.subplot(1, 2, 2)
    plt.plot(time[0], avg_rice_pop[0], c='green')
    plt.xlabel('t', fontsize=18)
    plt.ylabel('Amount of rice', fontsize=18)
    plt.tick_params(labelsize=18)
    #plt.title(f'Time evolution of amount of rice averaged\n over {nIterations} iterations', fontsize=18)
    plt.gca()