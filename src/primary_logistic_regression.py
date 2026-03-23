import numpy as np
lmda = 0.1
def linear_kernel(x: np.array, z: np.array):
    shape_a = x.shape
    shape_b = z.shape
    if shape_a[0] == shape_b[0] or shape_a[1] == shape_b[1]:
        return x.T @ z
    if shape_a[0] == shape_b[1] or shape_a[1] == shape_b[0]:
        return x @ z

def norm(x: np.array):
    return sum(x ** 2)

def gaussian_method_kernel(x: np.array, z: np.array):
    return np.exp(-lmda * norm(x - z))

A = [1,2,3]
B = [3,2,1]
