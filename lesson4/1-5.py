from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode

window = Window(background_image='forest_background.jpg')
#w=window.create_sprite()
#w.image='forest_background.jpg'
class MySprite(Sprite):

    def on_create(self):
        self.image='owl.png'
        self.x=100
        self.y=400
        self.health=50
    
    def on_update(self, dt):
        self.move_forward(8)
        if window.get_key_down(KeyCode.UP):
            self.rotation=90
        elif window.get_key_down(KeyCode.DOWN):
            self.rotation=270
        elif window.get_key_down(KeyCode.LEFT):
            self.rotation=180
        elif window.get_key_down(KeyCode.RIGHT):
            self.rotation=0
        if self.touching_any_sprite() or self.x>window.width:
           self.health-=1
           print(self.health)
        if self.health<0:
           print("You lose!")
           window.exit()

class Enemy(Sprite):

    def on_create(self):
        self.image='ork1.png'
        self.x=1000
        self.y=300
        self.scale=0.5
    def on_update(self, dt):
        self.point_toward_sprite(self)
    
self=window.create_sprite(Enemy)
        


s=window.create_sprite()
s.image='fireball.gif'
s.x=300
s.y=300
s1=window.create_sprite()
s1.image='fireball.gif'
s1.x=600
s1.y=500
s2=window.create_sprite()
s2.image='fireball.gif'
s2.x=1000
s2.y=100
s3=window.create_sprite()
s3.image='fireball.gif'
s3.x=600
s3.y=200
for x in range(0,window.width,100):
    b=window.create_sprite()
    b.image='pig.png'
    b.x=x
    b.y=700

window.create_sprite(MySprite)
window.run()



