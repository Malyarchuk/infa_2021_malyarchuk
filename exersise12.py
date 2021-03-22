import turtle
turtle.shape('turtle')
i = 0
def round(i):
    while i < 180/10:
        turtle.forward(10)
        turtle.left(10)
        i += 1
round(i)
s = 0
def roundsmall(s):

    while s < 180/10:
        turtle.forward(2)
        turtle.left(10)
        s += 1
roundsmall(s)
n = 8
while s <= n:
    while i <= n:
    round(0)
    roundsmall(0)
    i += 1
s +=1
