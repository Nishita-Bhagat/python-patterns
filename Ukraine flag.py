import turtle
from turtle import *
import time

speed(0)
setup(800,500)
bgcolor("yellow")

penup()
goto(-400, 250)
pendown()

color("royalblue")
begin_fill()
forward(800)
right(90)
forward(250)
right(90)
forward(800)
end_fill()

time.sleep(10)