import numpy as np
import matplotlib.pyplot as plt

timesteps = 1000
nIterations = 20
time = np.reshape(np.arange(timesteps), [1, timesteps])

rice_no_kill = np.load('rice_pop_SK=0.0IK=0.0.npy')
rice_kill_spa = np.load('rice_pop_SK=0.02IK=0.0.npy')
rice_kill_in = np.load('rice_pop_SK=0.0IK=0.03.npy')
rice_kill_both = np.load('rice_pop_SK=0.03IK=0.03.npy')

plt.plot(time[0], rice_no_kill[0])
plt.plot(time[0], rice_kill_spa[0])
plt.plot(time[0], rice_kill_in[0])
plt.plot(time[0], rice_kill_both[0])

plt.xlabel('t', fontsize=14)
plt.ylabel('Amount of rice', fontsize=14)
plt.tick_params(labelsize=14)
plt.legend(['No intervention', '2% Killing rate of sparrows', '3% Killing rate of insects', '3% Killing rate of both populations'])

plt.title(f'Time evolution of amount of rice for different strategies\n averaged over {nIterations} iterations', fontsize=16)
plt.show()