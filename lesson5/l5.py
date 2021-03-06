from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
from pyglet.image import create

window=Window(background_image="img/beach_03.png")

class Player(Sprite):

    def on_create(self):
        self.image="img/cat.png"
        self.y=0
    def on_update(self, dt):
        if window.get_key(KeyCode.LEFT):
            self.scale_x=-1
            self.x-=10
        if window.get_key(KeyCode.RIGHT):
            self.scale_x=1
            self.x+=10

player = window.create_sprite(Player)

class Gem(Sprite):

    def on_create(self):
        self.image="img/gem_shiny01.png"
        self.goto_random_position()
        self.y=window.height
        self.scale=0.25

    def on_update(self, dt):
        self.y-=3
        if is_aabb_collision(self, player):
            self.delete()
        elif self.y<0:
            self.delete()



def my_custom_update():
    window.create_sprite(Gem)

Scheduler.update(my_custom_update, delay=0.1)
         















window.run()
