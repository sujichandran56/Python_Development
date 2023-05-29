import turtle as t
import time
t.bgcolor('black')
t.speed(0)
colors=['red','dark red']
for numbers in range(400):
    t.fd(numbers+1)
    t.right(89)
    t.pencolor(colors[numbers%2])
time.sleep(2)







time.sleep(2)