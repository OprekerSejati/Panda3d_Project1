from panda3d.core import Vec3


def seek(agent, target):

    direction = target.getPos() - agent.getPos()

    if direction.length() > 0:
        direction.normalize()

    return direction


def avoid(agent, obstacles):

    force = Vec3(0, 0, 0)

    for obs in obstacles:

        dist = (agent.getPos() - obs.getPos()).length()

        if dist < 6:

            away = agent.getPos() - obs.getPos()

            if away.length() > 0:
                away.normalize()

            force += away * 2

    return force