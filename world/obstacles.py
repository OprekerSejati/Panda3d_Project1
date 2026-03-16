import random
from panda3d.core import CardMaker

def create_obstacles(base, count):
    obstacles = []
    for _ in range(count):
        cm = CardMaker("obstacle")
        cm.setFrame(-1,1,-1,1)
        obs = base.render.attachNewNode(cm.generate())
        x = random.uniform(-15,15)
        y = random.uniform(-15,15)
        obs.setPos(x, y, 0.5)
        obs.setScale(1)
        obs.setColor(0,0,1,1)
        obstacles.append(obs)
    return obstacles