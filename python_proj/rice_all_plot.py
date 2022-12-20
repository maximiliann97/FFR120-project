import numpy as np
import matplotlib.pyplot as plt

timesteps = 1000
nIterations = 20
time = np.reshape(np.arange(timesteps), [1, timesteps])

rice_no_kill = np.load('Data/rice_pop_SK=0.0IK=0.0, it = 100.npy')
rice_kill_spa = np.load('Data/rice_pop_SK=0.02IK=0.0, it = 100.npy')
rice_kill_in = np.load('Data/rice_pop_SK=0.0IK=0.03, it = 100.npy')
rice_kill_both = np.load('Data/rice_pop_SK=0.03IK=0.03, it = 100.npy')

rice_no_kill = rice_no_kill[0][:1000]
rice_kill_spa = rice_kill_spa[0][:1000]
rice_kill_in = rice_kill_in[0][:1000]
rice_kill_both = rice_kill_both[0][:1000]

rice_no_kill = np.reshape(rice_no_kill, (1, 1000))
rice_kill_spa = np.reshape(rice_kill_spa, (1, 1000))
rice_kill_in = np.reshape(rice_kill_in, (1, 1000))
rice_kill_both = np.reshape(rice_kill_both, (1, 1000))

plt.figure(figsize=(9, 8))
plt.plot(time[0], rice_no_kill[0])
plt.plot(time[0], rice_kill_spa[0])
plt.plot(time[0], rice_kill_in[0])
plt.plot(time[0], rice_kill_both[0])


plt.xlabel('t', fontsize=20)
plt.ylabel('Amount of rice', fontsize=20)
plt.tick_params(labelsize=20)
plt.legend([r'$\alpha=0$, $\beta=0$', r'$\alpha=0.02$, $\beta=0$', r'$\alpha=0$, $\beta=0.03$', r'$\alpha=0.03$, $\beta=0.03$'], fontsize=20)
plt.tight_layout()

plt.show()