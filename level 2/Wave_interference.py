import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

Z1 = np.sin(np.sqrt((X-2)**2 + Y**2) * 3)
Z2 = np.sin(np.sqrt((X+2)**2 + Y**2) * 3)
Z = Z1 + Z2

plt.imshow(Z, extent=(-10, 10, -10, 10), cmap='plasma')
plt.colorbar()
plt.show()
