from random import *
import turtle
turtle.shape('turtle')
n = 1
while n <= 100:
    turtle.left(randint(0, 360))
    turtle.forward(randint(1, 50))
    n += 1