from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
from pycat.label import Label
import random
window=Window(background_image="underwater_04.png")

score_label=Label("aliens in spaceship=0")
window.add_label(score_label)
score_label.x=550
score_label.y=600

class Spaceship(Sprite):

    def on_create(self):
        self.image="saucer.png"
        self.y=500
        self.scale=0.3
        self.score=0
        self.add_tag("spaceship")

    def on_update(self, dt):
        self.move_forward(8)
        if self.touching_window_edge():
            self.rotation+= 180

spaceship=window.create_sprite(Spaceship)

class Aliens(Sprite):

    def on_create(self):
        self.image=random.choice(['1.png','2.png','3.png','4.png','5.png'])
        self.goto_random_position()
        self.y=50
        self.scale=0.3
        self.is_moving=False

    def on_update(self, dt):
        if self.is_moving:
            self.y+=20
        if self.touching_any_sprite_with_tag("spaceship"):
            spaceship.score+=1
            print(spaceship.score)
            score_label.text="aliens in spaceship="+ str(spaceship.score)
            self.delete()

        if self.touching_window_edge():
            self.delete()
    def on_left_click(self):
        self.is_moving=True



def my_custom_update():
    window.create_sprite(Aliens)


Scheduler.update(my_custom_update, delay=1)


















window.run()









