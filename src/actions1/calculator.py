# A simple calculator with addition and multiplication functions
import numpy as np

def add(a, b):
    """Returns the sum of a and b"""
    return a + b

def multiply(a, b):
    """Returns the product of a and b"""
    return a * b

def make_matrix(m:list):
    return np.array(m)

if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 6, 5], [1, 2, 3]]
    print(make_matrix(mat))
