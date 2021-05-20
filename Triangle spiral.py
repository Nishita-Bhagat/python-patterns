import turtle
turtle.speed(0)
turtle.pensize(2)
turtle.bgcolor('purple')
turtle.pencolor('white')

def shape(angle, side, limit):
    reversedirection = 200
    turtle.forward(side)
    if side%(reversedirection*2) == 0:
        angle+=2
    elif side%reversedirection == 0:
        angle-=2
        turtle.right(angle)
        side = side+2
        if side<limit:
            shape(angle, side, limit)
angle = 119
side = 0
limit = 600
shape(angle, side, limit)
turtle.done()