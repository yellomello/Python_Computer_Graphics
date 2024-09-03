import turtle

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
colors = ['#FF1493', '#FFD700', '#00FA9A', '#1E90FF', '#FF4500']

for i in range(36):
    for color in colors:
        t.color(color)
        t.circle(100)
        t.right(10)

turtle.done()
