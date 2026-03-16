from panda3d.core import Vec3
import math

# dummy steering functions
def seek(agent_model, target_model):
    dir = target_model.getPos() - agent_model.getPos()
    return dir

def avoid(agent_model, obstacles):
    # simple placeholder, no real collision avoidance yet
    return Vec3(0,0,0)

class Agent:
    def __init__(self, base, x, y):
        self.game = base
        self.model = base.loader.loadModel("models/box")
        self.model.reparentTo(base.render)
        self.model.setPos(x, y, 0.5)
        self.model.setScale(0.5)
        self.model.setColor(1,0,0,1)

    def update(self, player, obstacles):
        move = seek(self.model, player) + avoid(self.model, obstacles)
        if move.length() > 0:
            move.normalize()
        self.model.setPos(self.model.getPos() + move*0.2)
        if move.length() > 0:
            angle = math.degrees(math.atan2(move.x, move.y))
            self.model.setH(angle)