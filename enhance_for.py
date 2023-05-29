import turtle
import time
turtle.begin_fill()
for i in range(4):
    turtle.fd(100)
    turtle.rt(90)
turtle.fillcolor('yellow')
turtle.end_fill()
time.sleep(2)
turtle.penup()
turtle.rt(90)
turtle.fd(100)
turtle.rt(90)
turtle.pendown()
turtle.penup()
turtle.fd(100)
turtle.rt(90)
turtle.pendown()
n = 10
turtle.begin_fill()
while n <= 40:
    turtle.circle(n)
    n = n+10
turtle.fillcolor('orange')
turtle.end_fill()
time.sleep(2)