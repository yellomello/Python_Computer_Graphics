import turtle

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
colors = ['#ff0000', '#00ff00', '#0000ff', '#ff00ff', '#00ffff', '#ffff00']

for x in range(360):
    t.color(colors[x % 6])
    t.circle(x)
    t.left(59)

turtle.done()
