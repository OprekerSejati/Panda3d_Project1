from direct.showbase.ShowBase import ShowBase
from panda3d.core import Vec3, AmbientLight, OrthographicLens

from core.background import Background
from ui.stats import Stats
from agents.agent import Agent
from world.obstacles import create_obstacles

import random

class Simulation(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Stats UI
        self.stats = Stats()

        # Background desert
        self.background = Background(self, "assets/desert2048.png")

        # Disable default camera mouse control
        self.disableMouse()

        # Orthographic camera → desert plane proporsional
        lens = OrthographicLens()
        lens.setFilmSize(50, 50)  # adjust to cover whole plane
        lens.setNearFar(-100, 1000)
        self.cam.node().setLens(lens)

        # Camera top-down
        self.camera.setPos(0, -50, 50)
        self.camera.lookAt(0, 0, 0)

        # Ambient light
        light = AmbientLight("ambient")
        light.setColor((1,1,1,1))
        light_np = self.render.attachNewNode(light)
        self.render.setLight(light_np)

        # Player cube
        self.player = self.loader.loadModel("models/box")
        self.player.reparentTo(self.render)
        self.player.setScale(1)
        self.player.setPos(0, 0, 0.5)

        # Keyboard input
        self.keys = {"w": False, "a": False, "s": False, "d": False}
        for key in self.keys:
            self.accept(key, self.set_key, [key, True])
            self.accept(key + "-up", self.set_key, [key, False])

        # Obstacles
        self.obstacles = create_obstacles(self, 8)

        # Agents
        self.agents = []
        self.spawn_agents(200)

        # Main loop
        self.taskMgr.add(self.update, "update")

    def set_key(self, key, value):
        self.keys[key] = value

    def spawn_agents(self, count):
        for _ in range(count):
            x = random.uniform(-20, 20)
            y = random.uniform(-20, 20)
            agent = Agent(self, x, y)
            self.agents.append(agent)

    def move_player(self):
        speed = 0.4
        move = Vec3(0, 0, 0)
        if self.keys["w"]: move.y += speed
        if self.keys["s"]: move.y -= speed
        if self.keys["a"]: move.x -= speed
        if self.keys["d"]: move.x += speed
        self.player.setPos(self.player.getPos() + move)

    def update(self, task):
        self.move_player()

        fps = globalClock.getAverageFrameRate()
        self.stats.update(len(self.agents), fps)

        for agent in self.agents:
            agent.update(self.player, self.obstacles)

        return task.cont