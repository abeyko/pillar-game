import random

OFF = (0,0,0)
WALL_COLOR = (245,222,179)
position = [0,0]
class Wall:
    def __init__(self, comm):
        self.col = 0
        
        # height is 0 or 1
        height = random.getrandbits(1)
        # determine if starting from top or bottom
        bottom = bool(random.randint(1))
        
        #store which rows the wall is on
        if bottom:
            self.rows = list(range(height))
        else
            self.rows = list(2-range(height))
            
        self.comm = comm
    
    def drawWall(self, comm):
        for row in self.rows:
            if(row == 0):
                self.comm.lowerBandLight(self.col, WALL_COLOR)
            elif (row == 1):
                self.comm.middleBandLight(self.col, WALL_COLOR)
            else:
                self.comm.upperBandLight(self.col, WALL_COLOR)
        
        
    
    