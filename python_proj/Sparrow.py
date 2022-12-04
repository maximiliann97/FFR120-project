import numpy as np


class Sparrow:
    def __init__(self, grid: int, age: int, hungry: bool, alive: bool):
        if isinstance(grid, int):
            self.position = np.random.randint(1, grid+1)
        else:
            raise TypeError('Needs to take integer')
        
        self.age = age
        self.hungry = hungry
        self.alive = alive
        
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
        
        
    def move(self):


    def age(self):
