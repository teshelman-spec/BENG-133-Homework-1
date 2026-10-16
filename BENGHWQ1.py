# Q1: Taylor Approximation

#part a
import numpy as np
import matplotlib.pyplot as plt
#part b
t = np.linspace(0, 0.6, 601)

f = np.exp(-t)

p = 1 - t + (t**2 / 2)

error = np.abs(f - p)
max_error = np.max(error)

print(max_error)

plt.plot(t, error, label="Actual Error")
plt.axhline(y=0.036, linestyle="--", label="Error Bound B = 0.036")
plt.xlabel("t")
plt.ylabel("Actual Error")
plt.title("Taylor Polynomial Approximation Error")
plt.grid(True)
plt.legend()
plt.show()

#part d
h_values = np.array([0.3] + [10.0**(-i) for i in range(1, 17)])

x = 0.3
exact = -np.exp(-x)

print("Exact derivative:", exact)

forward = (np.exp(-(x + h_values)) - np.exp(-x)) / h_values
forward_error = np.abs(forward - exact)
print(forward)
print(forward_error)

centered = (np.exp(-(x + h_values)) - np.exp(-(x - h_values))) / (2 * h_values)
centered_error = np.abs(centered - exact)
print(centered)
print(centered_error)

plt.loglog(h_values, forward_error, "o-", label="Forward Difference")
plt.loglog(h_values, centered_error, "s-", label="Centered Difference")
plt.xlabel("Step size h")
plt.ylabel("Absolute Error")
plt.title("Forward vs. Centered Difference")
plt.legend()
plt.grid(True)
plt.show()
