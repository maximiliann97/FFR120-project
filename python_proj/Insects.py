import numpy as np
import matplotlib.pyplot as plt


class Insects:
    def __init__(self, N: int):
        if isinstance(N, int):
            self.position = np.random.randint(1, N+1, 2)
        else:
            raise TypeError('Needs to take integer')
        self.age = 0
        self.hungry = False
        self.alive = True
        self.old = False
        self.days_without_food = 0
        self.lattice_size = N

    def update_hungry(self, hungry):
        if isinstance(hungry, bool):
            self.hungry = hungry
        else:
            raise TypeError('Needs to be true or false')

    def update_alive(self, alive):
        if isinstance(alive, bool):
            self.alive = alive
        else:
            raise TypeError('Needs to be true or false')

    def move(self, rice_field_coords):
        distance, rice_field_index = self.calc_distance(rice_field_coords)
        distance_limit = 25  # if below this sparrow move to closest rice field, else move randomly
        if distance < distance_limit:
            self.position = rice_field_coords[rice_field_index, :][0][0]
        else:
            directions = ['up', 'down', 'left', 'right']
            r = np.random.randint(0, 4)
            direction = directions[r]
            if direction == 'up' and self.position[1] > 1:
                self.position[1] -= 1
            if direction == 'down' and self.position[1] < self.lattice_size-1:
                self.position[1] += 1
            if direction == 'right' and self.position[0] < self.lattice_size-1:
                self.position[0] += 1
            if direction == 'left' and self.position[0] > 1:
                self.position[0] -= 1

    def aged(self):
        self.age += 1
        if self.age > 30:
            self.old = True
        return self.old

    def food(self, food):
        if food:
            self.update_hungry(False)
            self.days_without_food = 0
        else:
            self.update_hungry(True)
            self.days_without_food += 1
        if self.days_without_food > 4:
            self.alive = False

    def calc_distance(self, rice_field_coords):
        nFields = len(rice_field_coords)
        position = np.tile(self.position, (nFields, 1))
        distances = np.linalg.norm(position - rice_field_coords, axis=1)
        min_distance = np.min(distances)
        index_min_rice_field = np.where(distances == min_distance)
        return min_distance, index_min_rice_field



