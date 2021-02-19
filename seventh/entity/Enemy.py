from pgzero.actor import Actor


class Enemy:
    x = None
    y = None
    actor = None
    image = None
    speed = None
    life = None

    def __init__(self, x, y, image, speed, life):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.actor = Actor(image)
        self.actor.x = x
        self.actor.y = y
        self.life = life

    def draw(self):
        self.actor.draw()

    def update(self):
        self.actor.y += self.speed
