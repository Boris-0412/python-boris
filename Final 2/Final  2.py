from random import choice, randint
from pycat.base.color import Color
from pycat.core import Window, Sprite
from pyglet.gl.glext_arb import GL_MAT_COLOR_INDEXES_BIT_PGI

w = Window()

frogs = []

current_frog = None

grids = []


class Grid(Sprite):

    def on_create(self):
        self.scale = 30

    def set_position(self, i, j):
        self.i = i
        self.j = j
        self.x = X0 + j * CELL_SIZE
        self.y = Y0 + i * CELL_SIZE


    def on_left_click(self):
        global current_frog
        if current_frog is None:
            # go throgh frogs and find frog with self.i, self.j
            for f in frogs:
                if f.i == self.i and f.j == self.j:
                    current_frog = f
                    f.color = Color.ORANGE
            # set to current frog
        else:
            if current_frog.distance_to (self.position) > 2: 
                # if not clicked on current_frog cell
                print("set pre post, ave, Green")
                pre_position = current_frog.position
                post_position = self.position
                current_frog.color = Color.GREEN
                average_position = (pre_position + post_position)/2
                print(pre_position, post_position, current_frog.color, average_position)


                for frog in frogs:
                    if frog != current_frog:
                        if frog.distance_to (average_position) < 2:
                            frog.delete()
                            current_frog.set_position(self.i, self.j)
                            print(current_frog.position)
                            break
                    
                current_frog = None


class GreenFrog(Sprite):

    def on_create(self):
        self.layer = 1
        self.scale = 30
        self.color = Color.GREEN

    # def on_left_click(self):
    #     global current_frog
    #     current_frog = self
    #     self.color = Color.ORANGE

    def set_position(self, i, j):
        self.i = i
        self.j = j
        self.x = X0 + j * CELL_SIZE
        self.y = Y0 + i * CELL_SIZE


M = 5
N = 8
X0 = 300
Y0 = 150
CELL_SIZE = 100




frog_grid = [[None for _ in range(N)]for _ in range(M)]

def create_frogs(n: int):
    i = randint(0,M-1)
    j = randint(0,N-1)
    g = w.create_sprite(GreenFrog)
    g.set_position(i, j)
    frog_grid[i][j] = g
    frogs.append(g)

    for _ in range(n-1):
        while not frog_grid[i][j] is None:
            i = randint(0,M-1)
            j = randint(0,N-1)

        g = w.create_sprite(GreenFrog)
        g.set_position(i, j)
        frog_grid[i][j] = g
        frogs.append(g)
    # for i in range(5):
    #     for j in range(5):
    #         if grids[i][j] is None:
    #             frog_grid.append(grids[i, j])
         

# for i in range(4):
#     g = w.create_sprite(GreenFrog)
#     frogs.append(g)

create_frogs(20)

for i in range(M):
    for j in range(N):
        cell = w.create_sprite(Grid)
        cell.set_position(i, j)
        grids.append(cell)

w.run()