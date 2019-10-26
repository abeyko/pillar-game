class Character:
    position = [0, 0] # LED number and LED row
    color = [255, 255, 255] # main color of the player
    color2 = [255, 255, 255] # second color that's used during animations
    stepRatio = 96/23 # the ratio of motor steps to LED changes
    stepAngle = 0 # the angle of the stepper motor
    lives = 3
    isInvincibleTicks = 0

    # 4 steps counter clockwise = one LED to the right
    # 23 LEDs and 96 steps clockwise = one revolution

    # required a towerComm object to passed to it
    def __init__(self, commClass):
        self.comm = commClass
        return

    def updatePosition(self, axis0, axis1):
        if(axis0 > 0.5):
            self.moveRight()
        if (axis0 < -0.5):
            self.moveLeft()
        if (axis1 < -0.5):
            self.moveUp()
        if (axis1 > 0.5):
            self.moveDown()
        print(self.position)
        return

    # move the character to the right one led
    def moveRight(self):
        # makes sure you cant move to an LED over 300
        if(self.position[0] < 299):
            self.updateTower((0, 0, 0))  # blank the previous LED
            self.calcStepPosition()
            self.position[0] += 1
            self.calcStepPosition()
            self.updateTower(self.color)
        return

    # move the character to the left one LED
    def moveLeft(self):
        # makes sure you cant move to an LED under 0
        if(self.position[0] > 0):
            self.updateTower((0, 0, 0))  # blank the previous LED
            self.calcStepPosition()
            self.position[0] -= 1
            self.calcStepPosition()
            self.updateTower(self.color)
        return

    # move the character up one row
    def moveUp(self):
        # makes sure you cant move to a row above 2
        if(self.position[1] < 2):
            self.updateTower((0, 0, 0))  # blank the previous LED
            self.position[1] += 1
            self.updateTower(self.color)
        return

    # move the character down one row
    def moveDown(self):
        # makes sure you cant move to a row under 0
        if (self.position[1] > 0):
            self.updateTower((0, 0, 0))  # blank the previous LED
            self.position[1] -= 1
            self.updateTower(self.color)

        return

    # calculate the position of the stepper motor
    def calcStepPosition(self):
        self.stepAngle = self.position[0]*self.stepRatio

        # makes sure the step angle doesn't surpass 0-96
        while(self.stepAngle > 96):
            self.stepAngle -= 96
        while (self.stepAngle < 0):
            self.stepAngle += 96
        return

    # updates the tower with the new character position information
    def updateTower(self, color):
        self.comm.GoTo(self.stepAngle)
        if(self.position[1] == 0):
            self.comm.lowerBandLight(self.position[0], color)
        elif (self.position[1] == 1):
            self.comm.middleBandLight(self.position[0], color)
        else:
            self.comm.upperBandLight(self.position[0], color)
        return

    #give it an array of all the enemies currently on the screen to detect collissions
    def hasCollided(self, enemies):

        #incriments the amount of invicibility the player has down by one
        if self.isInvincibleTicks > 0:
            self.isInvincibleTicks -= 1
            self.collissionAnimation()

        for i in range(0, len(enemies)):
            # checks to see if the player and the enemy collided
            if enemies[i].position[0] == self.position[0] and enemies[i].position[1] == self.position[1]:
                # checks to see if the player is currently invincible
                if self.isInvincibleTicks == 0:
                    self.lives -= 1
                    self.isInvincibleTicks = 15 # makes the player invincible for 15 frames
        return

    def collissionAnimation(self):
        if self.isInvincibleTicks % 2 == 0: # checks to see if it's even
            self.color = self.color2
        else:
            self.color = [0, 0, 0]
        return

