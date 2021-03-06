from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
import random
window = Window()


class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10
        self.position = window.center
        

    def on_update(self, dt):
        if window.get_key(KeyCode.W):
            self.y += self.speed
        if window.get_key(KeyCode.A):
            self.x -= self.speed
        if window.get_key(KeyCode.S):
            self.y -= self.speed
        if window.get_key(KeyCode.D):
            self.x += self.speed

    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)
        
        

class Bullet(Sprite):

    def on_create(self):
        self.scale = 10
        self.color = Color.AZURE
        self.position = p.position
        self.point_toward_mouse_cursor()
        self.add_tag('bullet')
        self.time = 0
        
    def on_update(self, dt):
        self.move_forward(20)
        if self.time > 0:
            self.delete()
        if self.touching_window_edge(): 
            self.delete()
        if self.touching_any_sprite_with_tag('enemy'):
            self.time += 1

        
class Enemy(Sprite):
    
    def on_create(self):
        self.goto_random_position()
        self.rotation = random.randint(0,360)
        self.scale = 30
        self.color = Color.RED
        self.hp = 2
        self.time = 0
        self.bullet_time = 2
        self.add_tag('enemy')
    
    def on_update(self, dt):
        self.move_forward(2)
        self.time += dt
        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag('bullet'):
            self.hp -= 1
        if self.hp < 1:
            self.delete()
        if self.time > self.bullet_time:
            eb=window.create_sprite(EnemyBullet)
            eb.position = self.position
            eb.point_toward(p.position)
            self.time = 0

class EnemyBullet(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 10
        

    def on_update(self, dt):
        self.move_forward(5)
        if self.touching_window_edge() or self.touching_sprite(p):
            self.delete()


def spawn_enemy():
    window.create_sprite(Enemy)
Scheduler.update(spawn_enemy,delay=0.5)






p = window.create_sprite(Player)
window.run()