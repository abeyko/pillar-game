import random
from time import sleep

class FallingRocks:
    position = [0, 2]
    color = [154, 146, 96]
    previous_time = 0
    def __init__(self, comm, timer):
        self.position [0] = random.randint(276, 299)
        self.comm = comm
        self.timer = timer
        return

    def updatePosition(self, timer):
        sleep(0.1)
        if (timer - self.previous_time > 0.5):
            self.previous_time = timer
            self.drawRock([0, 0, 0])
            if self.position[1] == 0:
                self.moveDown()
                self.position[1] = 2
                self.drawRock(self.color)
            else:
                self.position[1] -= 1
                self.drawRock(self.color)
        return

    def moveDown(self):
        if self.position[0] < 23:
            self.position[0] = 0
        else:
            self.position[0] -= 23
        return

    def drawRock(self, color):
        if self.position[1] == 0:
            self.comm.lowerBandLight(self.position[0], color)
        elif self.position[1] == 1:
            self.comm.middleBandLight(self.position[0], color)
        else:
            self.comm.upperBandLight(self.position[0], color)
        return