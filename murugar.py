from sketchpy import canvas
import turtle
obj =  canvas.sketch_from_svg('C:\\Automation\\New folder\\Murugar.svg',scale=10)
t=turtle.Turtle()
t.penup()
t.goto(-100,-290)
t.pendown()
t.pencolor('red')
#t.write("OM SARAVANA BHAVA", align="center", font=("Arial",50,"bold"))
obj.draw()
# t.hideturtle()
t.done()
