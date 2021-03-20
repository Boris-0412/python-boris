from pycat.base.color import Color
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Sprite, Window
from enum import Enum, auto

from pyglet.gl.gl import GL_RED

window = Window(background_image="Galaxy.png")
window.background_sprite.scale = 1.5

class PlayerState(Enum):
    WAITING_FOR_CLICK = auto()
    JUMPING = auto()
    RESETTING = auto()



class Player(Sprite):

    def on_create(self):
        self.image = "frank-a.png"
        self.reset()

    def reset(self):
        self.x = 300
        self.y = 300
        self.scale = 0.3
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = 0
        self.state = PlayerState.JUMPING

    def on_update(self, dt):
        if self.state == PlayerState.JUMPING:
            prev_y = self.y
            self.x += self.x_speed
            self.y += self.y_speed
            self.y_speed -= 0.75

            for p in platforms:
                
                if self.is_touching_sprite(p.hitbox):
                    top_y = p.hitbox.y + p.hitbox.height/2 + self.height/2
                    
                    if prev_y > top_y:
                        self.x_speed = 0
                        self.y_speed = 0
                        self.y = top_y
                        self.state = PlayerState.WAITING_FOR_CLICK

            if self.is_touching_window_edge():
                self.state = PlayerState.RESETTING
            if self.is_touching_sprite(enemy.hitbox):

                self.state = PlayerState.RESETTING
        elif self.state == PlayerState.RESETTING:
            
            self.scale *=0.9
            self.rotation += 10
            if self.rotation > 180:
                self.reset()
        

    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state == PlayerState.WAITING_FOR_CLICK:
            x_dist = mouse_event.position.x - self.x
            y_dist = mouse_event.position.y - self.y

            self.x_speed = x_dist*0.05
            self.y_speed = y_dist*0.05

            self.state = PlayerState.JUMPING
        

class Platform(Sprite):

    def on_create(self):
        self.image = "button3-a.png"
        self.scale = 0.75
        self.add_tag("platform")

    def add_hitbox(self):
        self.hitbox = window.create_sprite()
        self.hitbox.position = self.position
        self.hitbox.y += 35
        self.hitbox.width = self.width*0.65
        self.hitbox.height = 5
        self.hitbox.color = Color.RED
        self.hitbox.opacity = 0

platforms = [
    window.create_sprite(Platform,x=600,y=100),
    window.create_sprite(Platform,x=800,y=300),
    window.create_sprite(Platform,x=300,y=200)
 ]

for p in platforms:
    p.add_hitbox()

window.create_sprite(Player)

class Enemy(Sprite):

    def on_create(self):
        self.image = "dinosaur4-c.png"
        self.x = 1000
        self.y = 300

    def add_hitbox(self):
        self.hitbox = window.create_sprite()
        self.hitbox.position = self.position
        self.hitbox.width = self.width*0.5
        self.hitbox.height = 280
        self.hitbox.color = Color.RED
        self.hitbox.opacity = 0
        
        
        

enemy = window.create_sprite(Enemy)
enemy.add_hitbox()







window.run()












