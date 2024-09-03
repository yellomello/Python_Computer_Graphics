import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

# Initial wave-like pattern
Z = np.sin(np.sqrt(X**2 + Y**2) * 3)

# Create the initial plot
im = ax.imshow(Z, extent=(-10, 10, -10, 10), cmap='viridis', alpha=0.8)
points, = ax.plot([], [], 'wo', markersize=5)

# Update function for the animation
def update(frame):
    # Wave pattern (gradually sharpening into particles)
    wave_intensity = np.exp(-frame/20.0)  # Decay to simulate wave collapsing
    Z = np.sin(np.sqrt(X**2 + Y**2) * 3 + frame/5.0) * wave_intensity

    # Update wave pattern
    im.set_array(Z)

    # Particle-like points (emerging as wave decays)
    if frame > 50:
        num_particles = 10
        particle_x = np.random.uniform(-10, 10, num_particles)
        particle_y = np.random.uniform(-10, 10, num_particles)
        points.set_data(particle_x, particle_y)
        points.set_markersize(10 * (1 - wave_intensity))  # Increase particle size as wave collapses

    return [im, points]

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
