import turtle

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
colors = ['#4B0082', '#8A2BE2', '#9400D3', '#9932CC', '#BA55D3', '#800080']

for i in range(72):
    t.color(colors[i % 6])
    t.circle(150)
    t.left(5)

turtle.done()
