import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, length, thickness):
    if length < 10:
        return
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)

    plt.plot([x, x_end], [y, y_end], color='brown', linewidth=thickness)
    
    draw_tree(x_end, y_end, angle + np.pi/6, length * 0.7, thickness * 0.7)
    draw_tree(x_end, y_end, angle - np.pi/6, length * 0.7, thickness * 0.7)

plt.figure(figsize=(10, 10))
draw_tree(0, -100, np.pi/2, 100, 10)
plt.xlim(-200, 200)
plt.ylim(-200, 200)
plt.axis('off')
plt.show()
