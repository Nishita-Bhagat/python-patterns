from turtle import *
import time

speed(0)
setup(800, 500)

penup()
goto(-400, -250)
pendown()

color("red")
begin_fill()
forward(800)
left(90)
forward(250)
left(90)
forward(800)
end_fill()
time.sleep(10)