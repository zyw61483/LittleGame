from pgzero.actor import Actor
from pgzero.loaders import sounds
from pgzero.constants import keys


class Hero:
    image = None
    x = None
    y = None
    actor = None
    bullets = []

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.actor = Actor(image)
        self.actor.x = x
        self.actor.y = y

    def draw(self):
        self.actor.draw()
        for bullet in self.bullets:
            bullet.draw()

    def update(self, enemys):
        for bullet in self.bullets:
            bullet.y -= 6
            # 子弹从画面消失 从数组移除
            if bullet.y < 0:
                self.bullets.remove(bullet)
        return self.checkHeroDead(enemys)


    def on_mouse_move(self, pos):
        self.actor.x = pos[0]
        self.actor.y = pos[1]

    def fire(self, key):
        if key == keys.SPACE:
            bullet = Actor('bullet')
            bullet.x = self.actor.x
            bullet.y = self.actor.y - 100
            self.bullets.append(bullet)
            sounds.shoot.play()

    def checkHeroDead(self, enemys):
        for enemy in enemys:
            if enemy.actor.colliderect(self.actor):
                sounds.explode.play()
                self.actor.image = 'boom'
                return True
