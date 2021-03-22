import turtle

turtle.shape('turtle')
i = 0
n = 10
while i < n:
    turtle.forward(100)
    turtle.stamp()
    turtle.backward(100)
    turtle.left(360 / n)
    i += 1