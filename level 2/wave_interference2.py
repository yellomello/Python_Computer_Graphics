import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure, the axis, and the plot
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

# Initial wave interference pattern
Z1 = np.sin(np.sqrt((X-2)**2 + Y**2) * 3)
Z2 = np.sin(np.sqrt((X+2)**2 + Y**2) * 3)
Z = Z1 + Z2

# Create the initial plot
im = ax.imshow(Z, extent=(-10, 10, -10, 10), cmap='plasma')

# Update function for the animation
def update(frame):
    # Change the phase by modifying the frame count
    phase_shift = frame / 10.0
    Z1 = np.sin(np.sqrt((X-2)**2 + Y**2) * 3 + phase_shift)
    Z2 = np.sin(np.sqrt((X+2)**2 + Y**2) * 3 + phase_shift)
    Z = Z1 + Z2
    im.set_array(Z)
    return [im]

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
