import numpy as np

class Rice:
    def __init__(self, N, amount_rice, rice_growth):
        center = np.array([N//2, N//2, amount_rice])
        upper_left = np.array([0, 0, amount_rice])
        upper_right = np.array([0, N, amount_rice])
        lower_left = np.array([N, 0, amount_rice])
        lower_right = np.array([N, N, amount_rice])
        temp_list = [center, upper_left, upper_right, lower_left, lower_right]
        self.fields = np.zeros([len(temp_list), 3])
        for index, element in enumerate(temp_list):
            self.fields[index, :] = element
        self.rice_growth = rice_growth
    def grow_rice(self):
        self.fields[:, -1] += self.rice_growth

    def rice_gets_eaten(self, plant: int):
        # if animal == "Sparrow":
        self.fields[plant, -1] -= 2  # Rice gets eaten
        if self.fields[plant, -1] < 0:
            self.fields[plant, -1] = 0



