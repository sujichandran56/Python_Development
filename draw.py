# graphical window opened inbuild keyword from v3 instead of import turtle as t using t
import turtle
# time module is used to wait the graphics widow using sleep keyword
import time
# getscreen is used to open the graphic window
turtle.getscreen()
# shape is used to draw cursor shape default in arrow   optional
#turtle.shape('square')
# shape size not must width, height, size
#turtle.shapesize(5,5,5)
# arrow color
turtle.fillcolor('yellow')
turtle.begin_fill()
# move the cursor draw line
turtle.forward(100)
# just cursor move the position
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
# this keyword is used to open time in window
time.sleep(5)
