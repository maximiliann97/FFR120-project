import matplotlib.pyplot as plt
import numpy as np

timesteps = 1400
time = np.reshape(np.arange(timesteps), [1, timesteps])

avg_sparrow_pop = np.load('Data/sparrow_pop_SK=0.0IK=0.0, it = 100.npy')
avg_insect_pop = np.load('Data/insect_pop_SK=0.0IK=0.0, it = 100.npy')
avg_rice_pop = np.load('Data/rice_pop_SK=0.0IK=0.0, it = 100.npy')



# Plots
plt.figure(figsize=(9, 8))
plt.subplot(2, 1, 1)
plt.plot(time[0], avg_sparrow_pop[0])
plt.plot(time[0], avg_insect_pop[0])
plt.xlabel('t', fontsize=18)
plt.ylabel('Population', fontsize=18)
plt.tick_params(labelsize=18)
plt.legend(['Sparrow population', 'Insect population'], fancybox=True, shadow=True, fontsize=20)
plt.gca()

plt.subplot(2, 1, 2)
plt.plot(time[0], avg_rice_pop[0], c='green')
plt.xlabel('t', fontsize=18)
plt.ylabel('Amount of rice', fontsize=18)
plt.tick_params(labelsize=18)
plt.tight_layout()

plt.gca()
plt.show()