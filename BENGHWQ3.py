# Q3: Linear Systems

import numpy as np
import matplotlib.pyplot as plt

#part b
A = np.array([[0, 1, 1],
              [1, 1, 0],
              [1, 0, 1]])

b = np.array([1, 1, 3])
b_hat = np.array([1, 1, 2])

x = np.linalg.solve(A, b)
x_hat = np.linalg.solve(A, b_hat)

r = A @ x - b
r_hat = A @ x_hat - b_hat

print("Original target")
print("Solution:", x)
print("Residual vector:", r)

print("\nModified target")
print("Solution:", x_hat)
print("Residual vector:", r_hat)

print("\nFeasibility")
print("Original target feasible:", np.all(x >= 0))
print("Modified target feasible:", np.all(x_hat >= 0))