import pgzrun
import random
from pgzero.clock import clock
from pgzero.loaders import sounds
from seventh.entity.Background import Background
from seventh.entity.Enemy import Enemy
from seventh.entity.Hero import Hero

WIDTH = 436
HEIGHT = 730
bg = Background(WIDTH / 2, -394, 'bg1', WIDTH / 2, -2642, 'bg2')
hero = Hero(WIDTH / 2, 700, 'hero')
enemys = []
score = 0
end = False
speed = 1


def init():
    global end
    global score
    global bullets
    global enemys
    global hero
    hero = Hero(WIDTH / 2, 700, 'hero')
    enemys = []
    score = 0
    end = False
    removeEnemy()
    createEnemys()


def draw():
    bg.draw()
    hero.draw()
    for enemy in enemys:
        enemy.draw()

    screen.draw.text('SCORE:' + str(score), (50, 50), fontsize=30, color='RED')
    if end:
        screen.draw.text('GAME OVER', (100, 300), fontsize=60, color='RED')
        screen.draw.text('click R to restart', (150, 350), fontsize=30, color='RED')


def update():
    global end
    if end:
        return
    end = hero.update(enemys)
    bg.update()
    for enemy in enemys:
        enemy.update()
    checkHitEnemys()


def on_mouse_move(pos, rel, buttons):
    if end:
        return
    hero.on_mouse_move(pos)


def on_key_down(key):
    if end and key == keys.R:
        init()
    if end:
        return
    hero.fire(key)


def createEnemys():
    global speed
    if end:
        return
    enemy = Enemy(random.randint(0, WIDTH), -10, 'enemy', speed, 1)
    if not score == 0 and score % 5 == 0:
        enemy = Enemy(random.randint(0, WIDTH), -10, 'enemy2', speed + 1, 5)
        if speed <= 5:
            speed += 1
        enemys.append(enemy)

    enemys.append(enemy)
    clock.schedule_unique(createEnemys, 1)


def removeEnemy():
    for enemy in enemys:
        if enemy.life <= 0:
            enemys.remove(enemy)
    clock.schedule_unique(removeEnemy, 0.05)


def checkHitEnemys():
    if end:
        return
    global score
    try:
        for bullet in hero.bullets:
            for enemy in enemys:
                if bullet.colliderect(enemy.actor):
                    enemy.life -= 1
                    if enemy.life <= 0:
                        enemy.actor.image = 'boom'
                    sounds.explode.play()
                    hero.bullets.remove(bullet)
                    score += 1
    except ValueError:
        return


init()
pgzrun.go()
