import pygame
import towerComm
import Character
import EnemySpawner
from time import sleep

BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
RED = pygame.Color('red')
GREEN = pygame.Color('green')
BLUE = pygame.Color('blue')

comm = towerComm.towerComm()
pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Volcano of Doom")
clock = pygame.time.Clock()
pygame.joystick.init()
Player = Character.Character(comm)
time = pygame.time.get_ticks()

spawner = EnemySpawner.EnemySpawner(comm, time)

def loop():
    done = False
    while done == False:
        time = pygame.time.get_ticks()
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

        #spawner.randomSpawn(time)
        for enemy in spawner.enemies:
            enemy.updatePosition(time)

        if (Player.HasWon == 1):
            print("Won")
            sleep(2)
            comm.sendAnything("Murica")
            sleep(2)
            done = True
        if (Player.HasLos == 1):
            comm.sendAnything("RED")
            sleep(2)
            done = True
        draw()
        clock.tick(7)


def draw():
    screen.fill(WHITE)
    return

loop()