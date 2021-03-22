import pygame
from pygame.draw import circle
from pygame.draw import rect
from random import randint
import math
pygame.init()

FPS = 1
screen = pygame.display.set_mode((900, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls_pos = []
square_pos = []
n = 0


def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    return [x, y, r, color, dx, dy]


def new_figure():
    global a, b, c, d
    a = randint(100, 700)
    b = randint(100, 500)
    c = randint(20, 100)
    d = randint(20, 100)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (a, b, c, d))
    da = randint(-10, 10)
    db = randint(-50, 50)
    return [a, b, c, d, color, da, db]


for i in range(10):
    balls_pos.append(new_ball())

for i in range(2):
    square_pos.append(new_figure())


def click(event):
    print(x, y, r)


def click(event):
    print(a, b, c, d)


def count_ball(func_click, balls_pos):
    global n
    for i in range(len(balls_pos)):
        if math.sqrt((func_click[0] - balls_pos[i][0]) ** 2 + (func_click[1] - balls_pos[i][1]) ** 2) <= balls_pos[i][2]:
            del balls_pos[i]
            balls_pos.append(new_ball())
            n += 1


def count_figure(func_click, figure_pos):
    global n
    for i in range(len(figure_pos)):
        if 0 < (func_click[0] - figure_pos[i][0]) < figure_pos[i][2]:
            if 0 < (func_click[1] - figure_pos[i][1]) < figure_pos[i][2]:
                del figure_pos[i]
                figure_pos.append(new_figure())
                n += 2


pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                count_ball(click(event), balls_pos)
                count_figure(click(event), figure_pos)
                print(n)
            if event.type == pygame.QUIT:
                finished = True
        pygame.display.update()
        screen.fill(BLACK)
pygame.quit()