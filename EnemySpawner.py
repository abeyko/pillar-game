import FallingRocks
import random

# This class is responsible for spawning enemies at random
class EnemySpawner:
    enemies = []
    timer = 0

    def __init__(self):
        self.spawnLava()
        return

    def spawnRocks(self):
        rock = FallingRocks.FallingRocks()
        self.enemies.append(rock)
        return

    def spawnLava(self):
        return

    def spawnBoulder(self):
        return

    def spawnWall(self):
        return

    def randomSpawn(self, timer):
        mob = random.randint(0, 2)
        time = timer-self.timer
        if(time > 4000):
            self.timer = timer
            if mob == 0:
                self.spawnRocks()
            elif mob == 1:
                self.spawnBoulder()
            else:
                self.spawnWall()
        return