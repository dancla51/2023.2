import Lab1
import numpy as np

if __name__ == '__main__':
    # Test power on 2x2
    r = Lab1.power(np.matrix([[2, -1], [-1, 2]]))
    print(r)

    # Test power on 3x3
    r = Lab1.power(np.matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]]))
    print(r)
