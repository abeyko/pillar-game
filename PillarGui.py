import pygame
import sys
from pygame.locals import *

class Pane(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()
        
    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
        pygame.display.update()
        
    def addSecondRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (175, 275, 200, 100), 2)
        pygame.display.update()

    def addText(self):
        self.screen.blit(self.font.render('Start', True, (255,0,0)), (240, 110))
        pygame.display.update()
        
    def addSecondText(self):
        self.screen.blit(self.font.render('Reset', True, (255,0,0)), (240, 310))
        pygame.display.update()

class PillarGui:   
    white = (255,255,255)
    black = (0,0,0)

    running = True

    window = pygame.display.set_mode((600,400), 0, 32)

    Rect1 = pygame.draw.rect(window, (black), (175, 75, 200, 100), 2)
    Rect2 = pygame.draw.rect(window, (black), (175, 275, 200, 100), 2)
    def __init__():
        pane = Pane()
        
        pane.addRect()
        pane.addText()
        
        pane.addSecondRect()
        pane.addSecondText()
        
    def draw():        
        # Mouse position and button clicking.
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            # Check if the rect collided with the mouse pos
            # and if the left mouse button was pressed.
            if Rect1.collidepoint(pos) and pressed1:
                print("Starting up tower game")
                return 1
            # Check if the rect collided with the mouse pos
            # and if the left mouse button was pressed.
            elif Rect2.collidepoint(pos) and pressed1:
                print("Reseting tower game")
                return 2
            elif event.type == pygame.QUIT:
                running = False
        pygame.quit()
