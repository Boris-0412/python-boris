from pycat.core import Window, Sprite, KeyCode, Scheduler, Label
window=Window(background_image='Stars.png')
window.background_sprite.scale_to_width(window.width)
time=0
time_label = Label()
time_label.y = 100
dead_player = 0
window.add_label(time_label)

class GameManager(Sprite):
    def on_create(self):
        self.is_visible=False
        self.timer=0

    def on_update(self, dt):
        self.timer+=dt
        
game_manager=window.create_sprite(GameManager)


class TimeLabel(Label):
    def on_create(self):
        self.font_size = 100
        
        self.y = 400
        self.x = 600

    def on_update(self, dt: float):
        if game_manager.timer < 2:
            self.text = "Get Ready"
        elif game_manager.timer < 3:
            self.text = "3"
        elif game_manager.timer < 4:
            self.text = "2"
        elif game_manager.timer < 5:
            self.text = "1"
        elif game_manager.timer < 6:
            self.is_visible = False
        
countdown_label = window.create_label(TimeLabel)

        
class WinLabel(Label):
    def on_create(self):
        self.is_visible=False    
        self.text="You Win!"
        self.x=600
        self.y=400
        self.font_size=100
    def on_update(self, dt: float):
        if game_manager.timer > 180:
            if game_manager.timer < 186:
                self.is_visible=True    

win_label = window.create_label(WinLabel)

class LoseLabel(Label):
    def on_create(self):
        self.is_visible = False
        self.text="You Lose!"
        self.x=600
        self.y=400
        self.timer=0
        self.font_size=100
    def on_update(self, dt: float):
        if dead_player == 2:
            self.timer+=dt
            if self.timer < 6:
                self.is_visible=True
            else:
                window.close()


lose_label = window.create_label(LoseLabel)



class Player(Sprite):
    def on_create(self):
        self.image='Frank.png' 
        self.scale=0.2
        self.x_speed=10
        self.x=400
        self.y=265
        self.y_speed=0
        self.is_on_block=False
        self.add_tag('p1')
        
    def on_update(self, dt):
        if game_manager.timer > 5:
            self.y+=self.y_speed
            p2 = window.get_sprites_with_tag('p2')
            if window.get_key(KeyCode.LEFT):
                self.x-=self.x_speed
                if len(p2) > 0 and self.touching_sprite(p2[0]):
                    p2[0].x=self.x-self.width/2-p2[0].width/2
            if window.get_key(KeyCode.RIGHT):
                self.x+=self.x_speed
                if len(p2) > 0 and self.touching_sprite(p2[0]):
                    p2[0].x=self.x+self.width/+p2[0].width/2
            if self.touching_any_sprite_with_tag('block'):
                self.is_on_block=True
                while self.touching_any_sprite_with_tag('block'):
                    self.y+=0.5
                self.y_speed=0
            if  window.get_key_down(KeyCode.UP) and self.is_on_block:
                self.is_on_block=False
                self.y_speed=8
            else:
                self.y_speed-=0.5
            
            global time
            time+=dt
            time_label.text = str(int(time))
            if time >180:
                if game_manager.timer < 186:  
                    print("Congratulations!You are so great!!!")
                else:
                    window.close()
            if self.touching_window_edge():
                global dead_player
                dead_player+=1
                self.delete()
            if dead_player == 2:
                print("You lose!!!HaHaHa!")
 

 

class StartBlock(Sprite):
    def on_create(self):
        self.image='block.png'
        self.x=400
        self.y=200
        self.width=200
        self.height=50
        self.add_tag('block')

    def on_update(self, dt):
        if game_manager.timer > 5:
            if self.touching_window_edge():
                self.delete()
            self.y+=3



class Block(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.y=0
        self.image='block.png'
        self.width=200
        self.height=50
        self.add_tag('block')
    def on_update(self, dt):
        if game_manager.timer > 5:
            self.y+=3
            if self.touching_window_edge():
                self.delete()

def spawn_blocks():
    if game_manager.timer > 5:
        window.create_sprite(Block)
        window.create_sprite(Block)

Scheduler.update(spawn_blocks,delay=1)

class SecondPlayer(Sprite):

    def on_create(self):
        self.image='nano.png'
        self.x=300
        self.y=265
        self.scale=0.35
        self.x_speed=10
        self.is_on_block=False
        self.y_speed=0
        self.add_tag('p2')

    def on_update(self, dt):
        if game_manager.timer > 5:
            self.y+=self.y_speed
            p1 = window.get_sprites_with_tag('p1')
            if window.get_key(KeyCode.A):
                self.x-=self.x_speed
                if len(p1) > 0 and self.touching_sprite(p1[0]):
                    p1[0].x=self.x-self.width/2-p1[0].width/2
            
            if window.get_key(KeyCode.D):
                self.x+=self.x_speed
                if len(p1) > 0 and self.touching_sprite(p1[0]):
                    p1[0].x=self.x+self.width/2+p1[0].width/2
                
            if self.touching_any_sprite_with_tag('block'):
                self.is_on_block=True
                while self.touching_any_sprite_with_tag('block'):
                    self.y+=0.5
                self.y_speed=0
            if  window.get_key_down(KeyCode.SPACE) and self.is_on_block:
                self.is_on_block=False
                self.y_speed=8
            else:
                self.y_speed-=0.5
            
            global time
            time+=dt
            time_label.text = str(int(time))
            if time >180:
                if game_manager.timer < 186:  
                    print("Congratulations!You are so great!!!")
                else:
                    window.close()
            if self.touching_window_edge():
                self.delete()
                global dead_player
                dead_player+=1
                
            if dead_player == 2:
                print("You lose!!!HaHaHa!")


p1=window.create_sprite(Player)
window.create_sprite(StartBlock)
p2=window.create_sprite(SecondPlayer)
window.run()