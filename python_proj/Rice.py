import numpy as np

class Rice:
    def __init__(self, fields, N):
        self.center = np.array([N/2,N/2])
        self.upper_left = np.array([0,0])
        self.upper_right = np.array([0, N-1])
        self.lower_left = np.array([N-1,0])
        self.lower_right = np.array([N-1,N-1])
        

    def grow_rice(self):
        self.fields[:, -1] += 1         # Adds one rice grain per day

    def rice_gets_eaten(self, plant: int):
        # if animal == "Sparrow":
        self.fields[plant, -1] -= 2  # Rice gets eaten
        if self.fields[plant, -1] < 0:
            self.fields[plant, -1] = 0
