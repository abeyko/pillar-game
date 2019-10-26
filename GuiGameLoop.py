import pygame
import towerComm
import Character
import EnemySpawner
import PillarGui

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
gui = PillarGui.PillarGui()

spawner = EnemySpawner.EnemySpawner()

def loop():
    status = draw()
    done = False
    run_game = False
    reset = True
    while done == False:
        if reset:
            comm.sendAnything("AllOff")
            clock = pygame.time.Clock()
            Player = Character.Character(comm)
            reset = False

        if run_game:
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

            spawner.randomSpawn(time)

            if (Player.HasWon == 1):
                print("Won")
                comm.sendAnything("Murica")
                time.sleep(2)
                done = True
            if (Player.HasLos == 1):
                comm.sendAnything("RED")
                time.sleep(2)
                done = True
                
        status = draw()

        # start
        if(status == 1):
            run_game = True
        elif(status == 2):
            reset = True

        clock.tick(5)


def draw():
    gui.draw()
    screen.fill(WHITE)
    return

loop()