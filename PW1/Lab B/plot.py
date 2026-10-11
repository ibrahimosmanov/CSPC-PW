import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1)
t = data[:, 0]
observed = data[:, 1]

LAMBDA = 0.3
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 4))

ax1.scatter(t, observed, color='black', label='Observed')
ax1.set_title('Observed Data')
ax1.set_xlabel('Time')
ax1.set_ylabel('Count')
ax1.legend()

ax2.plot(t, analytical, color='red', label='Analytical')
ax2.set_title('Analytical Law')
ax2.set_xlabel('Time')
ax2.legend()

plt.savefig('figure.png')
print("Figure saved successfully as figure.png")
