import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.title("Stephen Wolfram's Rule 30 Visualization")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.penup()

# Rule 30 in binary form: 00011110 (this is [0, 0, 0, 1, 1, 1, 1, 0] in list form)
rule_30 = {
    (1, 1, 1): 0,
    (1, 1, 0): 0,
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0
}

# Grid settings
cell_size = 10
grid_width = 61  # Number of cells (should be an odd number)
iterations = 30  # Number of rows to generate

# Initialize the first row with a single cell in the middle
current_row = [0] * grid_width
current_row[grid_width // 2] = 1

def draw_row(row, y_pos):
    for i, cell in enumerate(row):
        t.goto((i - grid_width // 2) * cell_size, y_pos)
        if cell == 1:
            t.dot(cell_size, "white")

def generate_next_row(current_row):
    next_row = []
    for i in range(grid_width):
        left = current_row[i - 1] if i > 0 else 0
        center = current_row[i]
        right = current_row[i + 1] if i < grid_width - 1 else 0
        next_row.append(rule_30[(left, center, right)])
    return next_row

def main():
    y_pos = 0
    for _ in range(iterations):
        draw_row(current_row, y_pos)
        y_pos -= cell_size
        current_row[:] = generate_next_row(current_row)
    screen.update()

# Run the main loop
main()

turtle.done()
