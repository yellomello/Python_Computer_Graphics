import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
n = 36
h = 0

for i in range(180):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    t.color(c)
    t.forward(i*2)
    t.right(60)
    t.forward(i*2)
    t.right(120)

turtle.done()
