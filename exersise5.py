import turtle

turtle.shape('turtle')
i = 1
while i < 11:
    turtle.forward(30 * i)
    turtle.left(90)
    turtle.forward(30 * i)
    turtle.left(90)
    turtle.forward(30 * i)
    turtle.left(90)
    turtle.forward(30 * i)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-15 * i, -15 * i)
    turtle.pendown()
    i += 1