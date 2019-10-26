class Character:
    position = [0, 0] # angle and LED row
    color = [255, 255, 255]
    stepRatio = 96/23 # the ratio of motor steps to LED changes
    stepAngle = 0 # the angle of the stepper motor
    #4 steps counter clockwise = one LED to the right
    #23 LEDs and 96 steps counter clockwise = one revolution
    def __init__(self):
        return

    #move the character to the right one led
    def moveRight(self):
        if(self.position[0] < 299):
            self.position[0] += 1
            self.calcStepPosition()
        return

    #move the character to the left one led
    def moveLeft(self):
        if(self.position[0] > 0):
            self.position[0] += 1
            self.calcStepPosition()
        return

    #move the character up one row
    def moveUp(self):
        if(self.position[1] < 2):
            self.position[1] += 1
        return

    #move the character down one row
    def moveDown(self):
        if (self.position[1] > 0):
            self.position[1] -= 1
        return

    #calculate the posiiton of the stepper motor
    def calcStepPosition(self):
        stepAngle = self.position[0]*self.stepRatio
        LEDNum = self.position[0]
        return