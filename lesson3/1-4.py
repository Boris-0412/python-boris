from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode

w=Window()

class MySprite(Sprite):
    def on_create(self):
        self.image="tiger.png"
        self.x=0
        self.y=100
        

    def on_update(self,dt):
        if self.window.get_key(KeyCode.D):
            self.x+=10
        if self.window.get_key(KeyCode.A):
            self.x-=10
        if self.window.get_key(KeyCode.W):
            self.y+=10 
        if self.window.get_key(KeyCode.S):
            self.y-=10       
        
class Me(Sprite):
    def on_create(self):
        self.image="owl.gif"
        self.x=0
        self.y=300
        
        

    def on_update(self,dt):
        if self.window.get_key(KeyCode.J):
            self.x+=10
        if self.window.get_key(KeyCode.G):
            self.x-=10
        if self.window.get_key(KeyCode.Y):
            self.y+=11  
        if self.window.get_key(KeyCode.H):
            self.y-=11     
        
class Hi(Sprite):
    def on_create(self):
        self.image="pig.png"
        self.x=0
        self.y=500
        


    def on_update(self,dt):
        if self.window.get_key(KeyCode.RIGHT):
            self.x+=12
        if self.window.get_key(KeyCode.LEFT):
            self.x-=12
        if self.window.get_key(KeyCode.UP):
            self.y+=12   
        if self.window.get_key(KeyCode.DOWN):
            self.y-=12               
       
w.create_sprite(Hi)
w.create_sprite(Me)
w.create_sprite(MySprite)

#if self.x>1000:
    #print("pig win!")


w.run()