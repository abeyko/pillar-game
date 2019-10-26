import pygame
import time
import serial
import towerComm
import Character

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')

comm = towerComm.towerComm()
pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Tower of Doom")
clock = pygame.time.Clock()
pygame.joystick.init()
Player = Character.Character(comm)

def loop():
    done = False
    while done == False:
        for event in pygame.event.get():  # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                done = True  # Flag that we are done so we exit this loop.
            elif event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        axis0 = joystick.get_axis(0)
        axis1 = joystick.get_axis(1)
        Player.updatePosition(axis0, axis1)
        draw()
        clock.tick(5)

def draw():
    screen.fill(WHITE)
    return

loop()