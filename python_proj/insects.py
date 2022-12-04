import numpy as np
import matplotlib.pyplot as plt

class insects:
    def __init__(self, N: int, age: int, hungry: bool):
        if isinstance(N, int):
            self.position = np.random.randint(1, N+1, 2)
        else:
            raise TypeError('Needs to take integer')

        self.hungry = hungry
        self.age = age
        self.alive = True
        self.days_without_food = 0


    def update_hungry(self, hungry):
        if isinstance(hungry, bool):
            self.hungry = hungry
        else:
            raise TypeError('Needs to be true or false')

    def update_state(self, alive):
        if isinstance(alive, bool):
            self.alive = alive
        else:
            raise TypeError('Needs to be true or false')



    def food(self, food):
        if food:
            self.update_hungry(False)
            self.days_without_food = 0
        else:
            self.update_hungry(True)
            self.days_without_food += 1
        if self.days_without_food == 5:
            self.alive = False




o = insects(2, 5, True)


o.food(False)
o.food(False)
o.food(False)
o.food(False)
o.food(False)
print(o.days_without_food)
print(o.alive)
