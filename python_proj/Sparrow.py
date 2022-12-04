import numpy as np


class Sparrow:
    def __init__(self, N: int, age: int, hungry: bool, alive: bool):
        if isinstance(N, int):
            self.position = np.random.randint(1, N+1)
        else:
            raise TypeError('Needs to take integer')
        
        self.age = age
        self.hungry = hungry
        self.alive = alive
        self.days_without_food = 0
        
    def update_hungry(self, hungry):
        if isinstance(hungry, bool):
            self.hungry = hungry
        else:
            raise TypeError('Needs to take boolean')
        
    def update_alive(self, alive):
        if isinstance(alive, bool):
            self.alive = alive
        else:
            raise TypeError('Needs to take boolean')
        
        
    def move(self, direction, grid):
        return 0

    def age(self, day):
        self.age += day

    def food(self, food):
        if food:
            self.update_hungry(False)
            self.days_without_food = 0
        else:
            self.update_hungry(True)
            self.days_without_food += 1

