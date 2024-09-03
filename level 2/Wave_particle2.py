import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
X, Y = np.meshgrid(x, y)

# Initial wave pattern
Z = np.sin(np.sqrt(X**2 + Y**2) * 3)

# Create the initial plot
wave_img = ax.imshow(Z, extent=(-10, 10, -10, 10), cmap='viridis', alpha=0.7)
particles, = ax.plot([], [], 'ro', markersize=8)

# Update function for the animation
def update(frame):
    # Update wave pattern
    wave_intensity = np.exp(-frame / 20.0)  # Wave decays over time
    Z = np.sin(np.sqrt(X**2 + Y**2) * 3 + frame / 5.0) * wave_intensity
    wave_img.set_array(Z)

    # Update particle-like points (photons)
    if frame > 50:
        num_particles = 20
        particle_x = np.random.uniform(-10, 10, num_particles)
        particle_y = np.random.uniform(-10, 10, num_particles)
        particles.set_data(particle_x, particle_y)
        particles.set_markersize(10 * (1 - wave_intensity))  # Size of particles changes with wave intensity

    return [wave_img, particles]

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Set axis limits and labels
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Wave-Particle Duality of Light")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")

# Show the animation
plt.show()
