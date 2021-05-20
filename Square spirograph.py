import turtle
turtle.speed(0)
turtle.bgcolor('black')
turtle.pensize(4)

def square():
    for i in range(4):
        turtle.forward(200)
        turtle.left(90)

for x in range(5):
    for colors in ['red', 'green', 'yellow', 'blue', 'grey', 'pink']:
        turtle.color(colors)
        turtle.left(12)
        square()

turtle.done()