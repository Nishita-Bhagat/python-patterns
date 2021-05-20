import turtle
#Creating a turtle object(pen)

pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    # Move the turtle to air
    pen.up()
    #Move the turtle to a given position
    pen.setpos(val,0)
    # Move the turtle to the ground
    pen.down()
    pen.right(180)

# Set the colors for drawing
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

turtle.bgcolor('sky blue')

# Setup the turtle features
pen.right(90)
pen.pensize(10)
pen.speed(0)

# Loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10*(i + 25), -10 * (i + 1))

pen.hideturtle()
turtle.done()
