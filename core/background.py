from panda3d.core import CardMaker, PNMImage, TextureStage

class Background:
    """
    Ground plane using desert2048.png
    Full proporsional, cube and agents visible
    """

    def __init__(self, base, texture_path="assets/desert2048.png"):
        self.base = base

        # Load texture
        tex = base.loader.loadTexture(texture_path)
        if not tex:
            print(f"ERROR: {texture_path} not found!")

        # Get texture ratio
        img = PNMImage()
        tex.store(img)
        ratio = img.getXSize() / img.getYSize()

        # Plane size
        plane_height = 100   # world unit height
        plane_width = plane_height * ratio

        cm = CardMaker("ground")
        cm.setFrame(-plane_width/2, plane_width/2, -plane_height/2, plane_height/2)
        self.ground = base.render.attachNewNode(cm.generate())
        self.ground.setP(-90)  # horizontal
        self.ground.setZ(0)

        # Apply texture
        ts = TextureStage("ground")
        self.ground.setTexture(ts, tex)

        # Disable lighting to keep visible
        self.ground.setLightOff()
        self.ground.setDepthWrite(True)
        self.ground.setDepthTest(True)