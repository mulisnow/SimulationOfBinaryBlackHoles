import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data/Weyl4_mode_20.dat', skiprows=2)
time = data[:, 0]
re32, im32 = data[:, 1], data[:, 2]
re64, im64 = data[:, 3], data[:, 4]

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(time, re32, label='r=32 (Re)', color='blue', alpha=0.7)
plt.plot(time, re64, label='r=64 (Re)', color='red', alpha=0.7)
plt.title('Gravitational Wave Mode (l=2, m=0) - Real Part')
plt.xlabel('Time')
plt.ylabel('Integral Value')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, np.abs(im32), label='r=32 (|Im|)', color='blue', linestyle='--', alpha=0.7)
plt.plot(time, np.abs(im64), label='r=64 (|Im|)', color='red', linestyle='--', alpha=0.7)
plt.yscale('log')
plt.title('Absolute Value of Imaginary Part (Log Scale)')
plt.xlabel('Time')
plt.ylabel('|Integral Value|')
plt.legend()
plt.grid(True)
plt.gcf().text(
    0.95, 0.02,
    'simulation by Hu MingZhang',
    ha='right',
    va='bottom',
    fontsize=10,
    color='black', transform=plt.gcf().transFigure
)
plt.tight_layout()

plt.savefig('signal pattern/Weyl4_mode_20.png')
