# Q2: Convergence and Stopping Criteria

import numpy as np
import matplotlib.pyplot as plt

#part a
C = 1 / (1 - 0.99)
tau = 0.01 / C

print("C =", C)
print("tau =", tau)

#part b
q_values = [0.5, -0.5, 0.99, 1.01]
k_values = np.arange(0, 31)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)

for q in q_values:
    x = [0]
    for k in range(30):
        x.append(q * x[-1] + (1 - q))

    plt.plot(k_values, x, label=f"q = {q}")

plt.axhline(y=1, color="black", linestyle="--", label="Target = 1")
plt.xlabel("k")
plt.ylabel("x_k")
plt.title("Sequences for Different Values of q")
plt.legend()
plt.grid(True)

def run_rule(threshold):
    x = 0
    for k in range(1, 1001):
        x_new = 0.99 * x + (1 - 0.99)
        delta = abs(x_new - x)
        x = x_new

        if delta < threshold:
            return k, x, abs(x - 1), True

    return 1000, x, abs(x - 1), False


k1, x1, e1, met1 = run_rule(0.01)
k2, x2, e2, met2 = run_rule(tau)

print("\nRule 1: Delta_k < 0.01")
if met1:
    print("Stopping index k =", k1)
else:
    print("Criterion not met")
print("Final value =", x1)
print("Error =", e1)

print("\nRule 2: Delta_k < tau")
if met2:
    print("Stopping index k =", k2)
else:
    print("Criterion not met")
print("Final value =", x2)
print("Error =", e2)

# Generate error sequence
end_k = max(k1, k2)
x = 0
errors = [abs(x - 1)]

for k in range(1, end_k + 1):
    x = 0.99 * x + (1 - 0.99)
    errors.append(abs(x - 1))

# Plot error sequence and stopping points
plt.subplot(1, 2, 2)

plt.plot(range(end_k + 1), errors, label="Error e_k")
plt.axhline(y=0.01, color="red", linestyle="--",
            label="Target error = 0.01")

if met1:
    plt.scatter(k1, e1, color="orange", zorder=3,
                label="Rule 1 stopping point")

if met2:
    plt.scatter(k2, e2, color="green", zorder=3,
                label="Rule 2 stopping point")

plt.xlabel("k")
plt.ylabel("Error e_k")
plt.title("Error for q = 0.99")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()