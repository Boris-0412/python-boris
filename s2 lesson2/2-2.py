from pycat.core import Sprite, Window

window = Window(background_image="Galaxy.png")

window.background_sprite.scale = 1.5

class Player(Sprite):

    def on_create(self):
        self.image = "frank-a.png"
        self.x = 300
        self.y = 300
        self.scale = 0.3

window.create_sprite(Player)

class Platform(Sprite):

    def on_create(self):
        self.image = "button3-a.png"
        self.scale = 0.75
        
window.create_sprite(Platform,x=600,y=100)
window.create_sprite(Platform,x=700,y=300)
window.create_sprite(Platform,x=300,y=200)

class Enemy(Sprite):

    def on_create(self):
        self.image = "dinosaur4-c.png"
        self.x = 1000
        self.y = 300
        

window.create_sprite(Enemy)







window.run()












