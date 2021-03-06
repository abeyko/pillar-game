import FallingRocks
import Lava
import random

# This class is responsible for spawning enemies at random
class EnemySpawner:

    def __init__(self, comm, time):
        self.comm = comm
        self.time = time
        self.enemies = []
        self.spawnLava()
        return

    def spawnRocks(self):
        rock = FallingRocks.FallingRocks(self.comm, self.time)
        self.enemies.append(rock)
        return

    def spawnLava(self):
        lava = Lava.Lava(self.comm, self.time)
        self.enemies.append(lava)
        return

    def spawnBoulder(self):
        return

    def spawnWall(self):
        return

    def randomSpawn(self, timer):
        mob = random.randint(0, 2)
        time = timer-self.time
        if(time > 5000):
            self.timer = timer
            if mob == 0:
                self.spawnRocks()
            elif mob == 1:
                self.spawnBoulder()
            else:
                self.spawnWall()
        return