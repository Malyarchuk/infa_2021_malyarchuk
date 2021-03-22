import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 600))

'''backgroung'''
rect(screen, (13, 144, 45), (0, 300, 900, 900))
rect(screen, (44, 185, 245), (0, 0, 900, 300))

'''big house'''
rect(screen, (132, 84, 4), (100, 350, 200, 150))
rect(screen, (0, 0, 0), (100, 350, 200, 150), 1)

polygon(screen, (233, 44, 86), [(100, 350), (300, 350), (200, 250), (100, 350)])
polygon(screen, (0, 0, 0), [(100, 350), (300, 350), (200, 250), (100, 350)], 1)

rect(screen, (72, 177, 204), (165, 390, 70, 60))

'''small house'''
rect(screen, (132, 84, 4), (500, 350, 150, 100))
rect(screen, (0, 0, 0), (500, 350, 150, 100), 1)

polygon(screen, (233, 44, 86), [(500, 350), (650, 350), (575, 280), (500, 350)])
polygon(screen, (0, 0, 0), [(500, 350), (650, 350), (575, 280), (500, 350)], 1)

rect(screen, (72, 177, 204), (549, 380, 55, 45))

'''big tree'''
rect(screen, (0, 0, 0), (400, 385, 15, 100))

circle(screen, (10, 122, 15), (425, 385), 30)
circle(screen, (0, 0, 0), (425, 385), 30, 1)

circle(screen, (10, 122, 15), (420, 360), 30)
circle(screen, (0, 0, 0), (420, 360), 30, 1)

circle(screen, (10, 122, 15), (390, 385), 30)
circle(screen, (0, 0, 0), (390, 385), 30, 1)

circle(screen, (10, 122, 15), (410, 400), 30)
circle(screen, (0, 0, 0), (410, 400), 30, 1)

circle(screen, (10, 122, 15), (390, 360), 30)
circle(screen, (0, 0, 0), (390, 360), 30, 1)

'''small tree'''
rect(screen, (0, 0, 0), (800, 385, 10, 80))

circle(screen, (10, 122, 15), (825, 385), 20)
circle(screen, (0, 0, 0), (825, 385), 20, 1)

circle(screen, (10, 122, 15), (820, 360), 20)
circle(screen, (0, 0, 0), (820, 360), 20, 1)

circle(screen, (10, 122, 15), (790, 385), 20)
circle(screen, (0, 0, 0), (790, 385), 20, 1)

circle(screen, (10, 122, 15), (810, 400), 20)
circle(screen, (0, 0, 0), (810, 400), 20, 1)

circle(screen, (10, 122, 15), (790, 360), 20)
circle(screen, (0, 0, 0), (790, 360), 20, 1)

'''sun'''
circle(screen, (254, 200, 35), (100, 100), 40)
circle(screen, (0, 0, 0), (100, 100), 40, 1)

'''cloud1'''
circle(screen, (255, 255, 255), (300, 100), 30)
circle(screen, (0, 0, 0), (300, 100), 30, 1)

circle(screen, (255, 255, 255), (320, 100), 30)
circle(screen, (0, 0, 0), (320, 100), 30, 1)

circle(screen, (255, 255, 255), (340, 100), 30)
circle(screen, (0, 0, 0), (340, 100), 30, 1)

circle(screen, (255, 255, 255), (360, 100), 30)
circle(screen, (0, 0, 0), (360, 100), 30, 1)

circle(screen, (255, 255, 255), (315, 80), 30)
circle(screen, (0, 0, 0), (315, 80), 30, 1)

circle(screen, (255, 255, 255), (350, 80), 30)
circle(screen, (0, 0, 0), (350, 80), 30, 1)

'''cloud2'''
circle(screen, (255, 255, 255), (700, 120), 30)
circle(screen, (0, 0, 0), (700, 120), 30, 1)

circle(screen, (255, 255, 255), (720, 120), 30)
circle(screen, (0, 0, 0), (720, 120), 30, 1)

circle(screen, (255, 255, 255), (740, 120), 30)
circle(screen, (0, 0, 0), (740, 120), 30, 1)

circle(screen, (255, 255, 255), (760, 120), 30)
circle(screen, (0, 0, 0), (760, 120), 30, 1)

circle(screen, (255, 255, 255), (715, 100), 30)
circle(screen, (0, 0, 0), (715, 100), 30, 1)

circle(screen, (255, 255, 255), (750, 100), 30)
circle(screen, (0, 0, 0), (750, 100), 30, 1)

'''cloud3'''
circle(screen, (255, 255, 255), (500, 140), 20)
circle(screen, (0, 0, 0), (500, 140), 20, 1)

circle(screen, (255, 255, 255), (520, 140), 20)
circle(screen, (0, 0, 0), (520, 140), 20, 1)

circle(screen, (255, 255, 255), (540, 140), 20)
circle(screen, (0, 0, 0), (540, 140), 20, 1)

circle(screen, (255, 255, 255), (560, 140), 20)
circle(screen, (0, 0, 0), (560, 140), 20, 1)

circle(screen, (255, 255, 255), (520, 120), 20)
circle(screen, (0, 0, 0), (520, 120), 20, 1)

circle(screen, (255, 255, 255), (545, 120), 20)
circle(screen, (0, 0, 0), (545, 120), 20, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()