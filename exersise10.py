import turtle
turtle.shape('turtle')
i = 0
def round(i):
    while i < 360/10:
        turtle.forward(10)
        turtle.left(10)
        i += 1
k = 1
n = 7
while k < n:
    round(i)
    turtle.left(360/(n-1))
    k +=1