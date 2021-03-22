import turtle
turtle.shape('turtle')
i = 0
r = 1
def round(i, r):
    while i < 360/10:
        turtle.forward(10 * r**0.3)
        turtle.left(10)
        i += 1
n = 8
while r <= 8:
    round(i, r)
    turtle.left(180)
    round(i, r)
    r += 1