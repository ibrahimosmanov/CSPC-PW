import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

data = np.loadtxt('freefall.csv', delimiter=',', skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

mean_accel = np.mean(a)
print(f"Mean Acceleration: {mean_accel:.4f} m/s^2")

std_accel = np.std(a)
print(f"Acceleration Standard Deviation: {std_accel:.4f}")

recovered_v = integrate.cumulative_trapezoid(a, t, initial=0) + v[0]
recovered_y = integrate.cumulative_trapezoid(recovered_v, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - recovered_y))
print(f"Largest difference in position: {max_diff:.4f} metres")

fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
axs[0].plot(t, y, label='Position (y)', color='blue')
axs[0].set_ylabel('Position (m)')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(t, v, label='Velocity (v)', color='orange')
axs[1].set_ylabel('Velocity (v - m/s)')
axs[1].legend()
axs[1].grid(True)

axs[2].plot(t, a, label='Acceleration (a)', color='green', alpha=0.6)
axs[2].axhline(y=-9.81, color='red', linestyle='--', label='Theory (-9.81)')
axs[2].set_ylabel('Acceleration (m/s^2)')
axs[2].set_xlabel('Time (s)')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('motion.png')
print("motion.png yaradıldı!")
