from pgzero.actor import Actor


class Background:
    image = None
    x = None
    y = None
    bg1 = None
    bg2 = None
    scroll_speed = 1

    def __init__(self, x, y, image, x2, y2, image2):
        self.x = x
        self.y = y
        self.image = image
        self.image2 = image2
        self.bg1 = Actor(image)
        self.bg1.x = x
        self.bg1.y = y
        self.bg2 = Actor(image2)
        self.bg2.x = x2
        self.bg2.y = y2

    def draw(self):
        self.bg1.draw()
        self.bg2.draw()

    def update(self):
        if self.bg1.y > 1854:
            self.bg1.y = -2642
        if self.bg2.y > 1854:
            self.bg2.y = -2642
        self.bg1.y += 1
        self.bg2.y += 1


