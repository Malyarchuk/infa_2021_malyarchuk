import turtle

turtle.shape('turtle')
def draw_geom (n):
    i = 1
    while i <= n:
        turtle.forward(20 * n)
        a = 180 - (180 * (n - 2) / n)
        turtle.left(a)
        i += 1
k = 3
n = 10
while k <= n:
    draw_geom(k)
    turtle.penup()
    turtle.goto(-10 * (k - 2), -10 * (k - 2))
    turtle.pendown()
    k += 1

