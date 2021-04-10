from pycat.core import Window, Sprite, Color, Scheduler
from random import randint

M = 5
N = 8
CELL_SIZE = 100

window = Window(width=N*CELL_SIZE, height=M*CELL_SIZE)



class Cell(Sprite):

    def on_create(self):
        self.scale = CELL_SIZE-1
        self.color = Color.ORANGE

    def set_ij(self, i, j):
        self.i = i
        self.j = j

    def on_left_click(self):
        print(self.i, self.j)
        self.toggle_neighbors()
        self.check_for_win()
        

    def toggle_neighbors(self):
        i = self.i
        j = self.j
        if j-1 >= 0:
            grid[i][j-1].toggle_color()
        if j+1 < N:
            grid[i][j+1].toggle_color()
        if i-1 >= 0:
            grid[i-1][j].toggle_color()
        if i+1 < M:
            grid[i+1][j].toggle_color()

    def toggle_color(self):
        if self.color == Color.ORANGE:
            self.color = Color.WHITE
        else:
            self.color = Color.ORANGE

    def check_for_win(self):
        for i in range(M):
            for j in range(N):
                if grid[i][j].color == Color.WHITE:
                    return
        print("You win!")
        Scheduler.wait(2, window.close)

grid = [[window.create_sprite(Cell) for j in range(N)]for i in range(M)]

x0 = y0 = CELL_SIZE/2

for i in range(M):
    for j in range(N):
        grid[i][j].x = x0 + j*CELL_SIZE
        grid[i][j].y = y0 + i*CELL_SIZE
        grid[i][j].set_ij(i, j)


count = 0
def map(dt):
    global count
    i = randint(0, M-1)
    j = randint(0, N-1)
    grid[i][j].toggle_neighbors()
    count += 1
    if count > 4:
        Scheduler.cancel_update(map)

Scheduler.update(map, delay=0.1)
        

window.run()