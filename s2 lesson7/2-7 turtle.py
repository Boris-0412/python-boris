from pycat.core import Window, Sprite


window = Window()



class Turtle(Sprite):

    def on_create(self):
        self.is_visible=False


    
    def draw_triangle(self, length):
        
        A = self.position
        self.move_forward(length)
        B = self.position
        self.rotation += 120
        self.move_forward(length)
        C = self.position

        # l1 = window.create_line(A.x, A.y, B.x, B.y, width = 0.1)
        # l1.opacity = 100
        # window.create_line(B.x, B.y, C.x, C.y, width = 0.1)
        # window.create_line(C.x, C.y, A.x, A.y, width = 0.1)

        window.create_line(A.x, A.y, B.x, B.y, width = 1)
        window.create_line(B.x, B.y, C.x, C.y, width = 1)
        window.create_line(C.x, C.y, A.x, A.y, width = 1)

        

    def on_update(self, dt):
        t.position = window.center
        window.clear_drawables()
        t.draw_triangle(t.scale*50)
        t.rotation += 100
        t.scale *= 1.001
        
t = window.create_sprite(Turtle)




window.run()