from pycat.core import Sprite, Window
import random


class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = 5

    def on_update(self, dt):
        self.move_forward(5)
        if self.touching_window_edge():
            self.rotation+=180


class ExplosionParticle(Sprite):

    def on_create(self):
        self.scale = 3
        self.time=0
        

    def on_update(self, dt):
        self.time+=dt
        self.opacity *=0.95
        self.move_forward(3)
        if self.touching_window_edge() or self.time > 2:
            self.delete()
            


class CreateButton(Sprite):

    def on_left_click(self):
        for _ in range(10):
            window.create_sprite(Particle)

class ExplodeButton(Sprite):

    def on_left_click(self):
        
        for p in window.get_sprites_with_tag('particle'):
            for r in range(0,360,30):
                q=window.create_sprite(ExplosionParticle)
                q.position=p.position
                q.rotation=r
            p.delete()
        

        

        
window = Window()


bb=window.create_sprite(CreateButton, x=100, y=100, scale=75)
bb.color=[0,0,255]
rb=window.create_sprite(ExplodeButton, x=100, y=200, scale=75)
rb.color=[255,0,0]

window.run()