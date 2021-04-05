"""main
This program uses a virtual environment
"""

# Numpy is not there
import numpy as np


def greet_me(name):
    """
    Function that says hello
    """
    print(f'Hello, {name}')

greet_me('world')

print(np.arange(0, 1, 0.1))
