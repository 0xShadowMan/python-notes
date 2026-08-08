import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral with Turtle")

# Create turtle
t = turtle.Turtle()
t.speed(0)  # fastest speed
turtle.colormode(255)  # allow RGB colors

# Draw a spiral
hue = 0
for i in range(200):
    color = colorsys.hsv_to_rgb(hue, 1, 1)  # convert HSV to RGB
    r = int(color[0]*255)
    g = int(color[1]*255)
    b = int(color[2]*255)
    t.pencolor(r, g, b)
    t.forward(i * 2)
    t.right(59)  # angle for spiral
    hue += 0.01

# Hide turtle and finish
t.hideturtle()
turtle.done()
