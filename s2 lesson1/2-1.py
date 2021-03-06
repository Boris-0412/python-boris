from pycat.core import Window, Sprite, KeyCode, Label
from pycat.scheduler import Scheduler
from random import randint

from pyglet.window.key import W


window =Window(enforce_window_limits=False,background_image="background.png",width=900,height=504)

 
class Score(Label):
    def on_create(self):
        self.score = 0


    def on_update(self, dt: float):
        self.text = "Score :" + str(int(self.score))


score = window.create_label(Score)

     
class LittleBird(Sprite):

    def on_create(self):
        self.image = "bird.gif"
        self.y = window.center.y
        self.x = 100
        self.scale = 0.25                          
  
    def on_update(self, dt):
        self.y -= 2.5     
        if window.is_key_down(KeyCode.SPACE):
            self.y += 40

        if self.is_touching_window_edge():
            window.close()   


class Pipes(Sprite):

    def on_create(self):
        self.image = "pipe.png"
        self.x = window.width + self.width/2
        self.scale = 0.5
        

    def on_update(self, dt):
        self.x -= 10
        if self.x  < -self.width/2:
            self.delete()
            score.score += 0.5

        if self.is_touching_sprite(player):
            window.close()



def create_pipes():
    bot_pipe = window.create_sprite(Pipes)
    top_pipe = window.create_sprite(Pipes)
    top_pipe.rotation = 180
    top_pipe.y = window.height
    y_offset = randint(-100, 100)
    bot_pipe.y += y_offset
    top_pipe.y += y_offset
    gap_offset = randint(-30, 10)
    bot_pipe.y -= gap_offset
    top_pipe.y += gap_offset                 



Scheduler.update(create_pipes,1)

player = window.create_sprite(LittleBird)
window.run()
                          