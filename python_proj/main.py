import matplotlib.pyplot as plt
import numpy as np
import random

def main():  
    t = 0
    while t< 100 :
        X = random.sample(range(1, 100), 10)
        Y = random.sample(range(1, 100), 10)
        plt.hold(True)
        plt.scatter(X, Y)
        plt.show()
        plt.hold(False)




if __name__ == '__main__':
    main()