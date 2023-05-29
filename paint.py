from turtle import *
import turtle
t=Turtle()
s=Screen()
s.title("MS Paint")
t.pencolor('cyan')
t.speed(-1)
def paint(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(paint)

def erase(x,y):
    t.clear()

def main():
    s.listen()
    t.ondrag(paint)
    s.onscreenclick(erase)
    done()

main()


