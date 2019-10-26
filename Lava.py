from random import randint

class Lava:
    # front end position of lava
    # know time
    led_number = -1
    position = [led_number, -1] # LED number and LED row
    previous_time = 0
    increment_time = 5000
    
    # required a towerComm object to passed to it
    def __init__(self, commClass, time):
        self.comm = commClass
        self.time = time
        return
    
    def updatePosition(self, timer):
        if (timer - self.previous_time > self.increment_time):
            self.increment_time *= .9
            self.previous_time = timer
            self.led_number += 1

        self.draw()
        return

    def draw(self):
        color = [randint(249, 255), randint(54, 154), randint(14, 34)]
        self.comm.lowerBandLight(self.position[0], color)
        color = [randint(249, 255), randint(54, 154), randint(14, 34)]
        self.comm.middleBandLight(self.position[0], color)
        color = [randint(249, 255), randint(54, 154), randint(14, 34)]
        self.comm.upperBandLight(self.position[0], color)

        return
    