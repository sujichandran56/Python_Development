import turtle as t
import time
t.pensize(2)
t.bgcolor('gray')
t.speed(1)
colors = ['Red', 'black', 'white', 'orange', 'Blue', 'Green', 'yellow']
while True:
    for i in range(7):
        for Colors in colors:
            t.pencolor(Colors)
            t.circle(60)
            t.left(20)
time.sleep(2)

