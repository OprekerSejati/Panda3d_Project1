from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
import time

class Stats:
    def __init__(self):
        self.collisions = 0
        self.start_time = time.time()
        self.text = OnscreenText(
            text="",
            pos=(-1.3, 0.9),
            scale=0.05,
            align=TextNode.ALeft,
            mayChange=True
        )

    def add_collision(self):
        self.collisions += 1

    def update(self, agent_count, fps):
        elapsed = int(time.time() - self.start_time)
        self.text.setText(f"""
Agents: {agent_count}
Collisions: {self.collisions}
FPS: {int(fps)}
Time: {elapsed}s
""")