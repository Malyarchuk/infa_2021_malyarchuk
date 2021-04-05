import pygame
import os
from pygame.draw import *
from random import randint

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('arial', 30)

FPS = 30
time = 0
screen = pygame.display.set_mode((900, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


# Add more balls targets
def new_balls(balls_number):
    for i in range(balls_number):
        x = randint(100, 800)
        y = randint(100, 500)
        r = randint(30, 50)
        dx = randint(-8, 8)
        dy = randint(-8, 8)
        color = COLORS[randint(0, 5)]
        circle(screen, color, (x, y), r)
        balls.append((x, y, r, dx, dy, color))


# Add more triangle targets
def new_triangles(tr_number):
    for i in range(tr_number):
        x = randint(100, 800)
        y = randint(100, 500)
        r = randint(60, 100)
        dx = randint(-8, 8)
        dy = randint(-8, 8)
        color = COLORS[randint(0, 5)]
        polygon(screen, color, [(x, y), (x + r, y), (x + r / 2, y + r)])
        triangles.append((x, y, r, dx, dy, color))


# Moving of targets with every frame
def new_frame():
    # Moving of balls
    for i in range(number_of_balls):
        x, y, r, dx, dy, color = balls[i]
        (x, y) = (x + dx, y + dy)
        if x - r < 0 or x + r > 900:
            dx = -dx
        if y - r < 0 or y + r > 600:
            dy = -dy
        balls[i] = (x, y, r, dx, dy, color)
    for i in range(number_of_balls):
        circle(screen, balls[i][5], (balls[i][0], balls[i][1]), balls[i][2])

    # Moving of triangles
    for i in range(number_of_triangles):
        x, y, r, dx, dy, color = triangles[i]
        (x, y) = (x + dx, y + dy)
        if x - r < 0 or x + r > 900:
            dx = -dx
        if y - r < 0 or y + r > 600:
            dy = -dy
        triangles[i] = (x, y, r, dx, dy, color)
    for i in range(number_of_triangles):
        polygon(screen, triangles[i][5], [(triangles[i][0], triangles[i][1]),
                                          (triangles[i][0] + triangles[i][2], triangles[i][1]),
                                          (triangles[i][0] + triangles[i][2] / 2, triangles[i][1] + triangles[i][2])])


# Check if player hit any targets
def click(cur_event):
    # Check if player hit any ball
    for i in range(number_of_balls):
        if (cur_event.pos[0] - balls[i][0]) ** 2 + (cur_event.pos[1] - balls[i][1]) ** 2 < balls[i][2] ** 2:
            global hits
            hits += 1
            rect(screen, WHITE, (0, 0, 900, 600), width=100)
            balls.pop(i)
            new_balls(1)
            break

    for i in range(number_of_triangles):
        if 0 < cur_event.pos[0] - triangles[i][0] < triangles[i][2] and 0 < cur_event.pos[1] - triangles[i][1] < \
                triangles[i][2]:
            hits
            hits += 2
            rect(screen, WHITE, (0, 0, 900, 600), width=100)
            triangles.pop(i)
            new_triangles(1)
            break


def sort_col(i):
    return int(i[0])


# Make a results table
def results_table():
    # Read existing table
    output = open("output.txt", 'r+')
    file = output.readlines()
    # Add new result
    file.append(str(hits) + " " + input() + '\n')
    for i in range(len(file)):
        file[i] = file[i].split()
    file.sort(key=sort_col, reverse=True)

    # Rewrite results
    output.seek(0)
    for i in range(len(file)):
        output.write(str(file[i][0]) + " " + file[i][1] + "\n")
    output.close()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

hits = 0

balls = []
number_of_balls = 15
new_balls(number_of_balls)

triangles = []
number_of_triangles = 10
new_triangles(number_of_triangles)

while time < 30 * 20:
    clock.tick(FPS)
    time += 1

    text_surface = my_font.render(str(hits), False, WHITE)
    screen.blit(text_surface, (0, 0))

    text_surface = my_font.render(str(20 - time // 30), False, WHITE)
    screen.blit(text_surface, (600, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)

    new_frame()
    pygame.display.update()
    screen.fill(BLACK)

results_table()

pygame.quit()
