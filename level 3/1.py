import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Conway's Game of Life")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# Grid settings
grid_size = 20
cell_size = 10

# Create a grid with random initial states (alive or dead)
def create_grid():
    return [[random.choice([0, 1]) for _ in range(grid_size)] for _ in range(grid_size)]

# Draw the grid
def draw_grid(grid):
    t.clear()
    for y in range(grid_size):
        for x in range(grid_size):
            t.goto(x * cell_size - grid_size * cell_size // 2, y * cell_size - grid_size * cell_size // 2)
            if grid[y][x] == 1:
                t.dot(cell_size, "white")
            else:
                t.dot(cell_size, "black")
    screen.update()

# Count alive neighbors
def count_alive_neighbors(grid, x, y):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size:
            count += grid[ny][nx]
    return count

# Apply the rules of the Game of Life
def evolve(grid):
    new_grid = [[0] * grid_size for _ in range(grid_size)]
    for y in range(grid_size):
        for x in range(grid_size):
            alive_neighbors = count_alive_neighbors(grid, x, y)
            if grid[y][x] == 1:  # Alive cell
                if alive_neighbors in [2, 3]:
                    new_grid[y][x] = 1
                else:
                    new_grid[y][x] = 0
            else:  # Dead cell
                if alive_neighbors == 3:
                    new_grid[y][x] = 1
    return new_grid

# Main loop
def main():
    grid = create_grid()
    while True:
        draw_grid(grid)
        grid = evolve(grid)
        turtle.update()
        turtle.delay(100)

# Run the main loop
main()

turtle.done()
