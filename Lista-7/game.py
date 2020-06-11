import sys, pygame
from note import Note
pygame.init()

size = width, height = 960, 540
speed = [0, 1]
background = 120, 22, 10
screen = pygame.display.set_mode(size)




while 1:
    screen.fill(background)
    pygame.display.flip()