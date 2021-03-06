from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Sprite, Window
from enum import Enum, auto

window = Window(background_image="Galaxy.png")
window.background_sprite.scale = 1.5

class PlayerState(Enum):
    WAITING_FOR_CLICK = auto()
    JUMPING = auto()
    RESETTING = auto()



class Player(Sprite):

    def on_create(self):
        self.image = "frank-a.png"
        self.x = 300
        self.y = 300
        self.scale = 0.3
        self.x_speed = 0
        self.y_speed = 0
        self.state = PlayerState.WAITING_FOR_CLICK

    def on_update(self, dt):
        if self.state == PlayerState.JUMPING:
            self.x += self.x_speed
            self.y += self.y_speed
            self.y_speed -= 0.75
            if self.is_touching_any_sprite_with_tag("platform"):
                self.x_speed = 0
                self.y_speed = 0
                self.state = PlayerState.WAITING_FOR_CLICK

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state == PlayerState.WAITING_FOR_CLICK:
            x_dist = mouse_event.position.x - self.x
            y_dist = mouse_event.position.y - self.y

            self.x_speed = x_dist*0.05
            self.y_speed = y_dist*0.05

            self.state = PlayerState.JUMPING



window.create_sprite(Player)

class Platform(Sprite):

    def on_create(self):
        self.image = "button3-a.png"
        self.scale = 0.75
        self.add_tag("platform")
        
window.create_sprite(Platform,x=600,y=100)
window.create_sprite(Platform,x=800,y=300)
window.create_sprite(Platform,x=300,y=200)

class Enemy(Sprite):

    def on_create(self):
        self.image = "dinosaur4-c.png"
        self.x = 1000
        self.y = 300
        

window.create_sprite(Enemy)







window.run()












