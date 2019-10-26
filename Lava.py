import pygame

class Lava:
    # front end position of lava
    # know time
    led-number = -1
    position = [led-number, -1] # LED number and LED row
    previous-time = 0
    increment-time = 0
    
    # required a towerComm object to passed to it
    def __init__(self, commClass, time):
        self.comm = commClass
        self.time = time
        return
    
    def updatePosition(self):
        if (self.Time - previous-time > increment-time):
            increment-time *= .9
            previous-time = self.Time
            led-number += 1
        else:
            break
        
        return position
    