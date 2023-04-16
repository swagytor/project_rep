# Алексей
from random import choice


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for i in range(self.N)] for j in range(self.N)]
        self.init()

    def init(self):
        m = 0
        while m != self.M:
            random_cell = choice(choice(self.pole))
            if random_cell.mine is False:
                random_cell.mine = True
                m += 1

        indx = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].mine:
                    mines_count = sum((self.pole[i+x][j+y].mine for i, j in indx if 0 <= i+x < self.N and 0 <= j+y < self.N))
                    self.pole[x][y].around_mines = mines_count

    def show(self):
        for i in self.pole:
            for j in i:
                if j.fl_open:
                    if j.mine:
                        print('*', end=' ')
                    else:
                        print(j.around_mines, end=' ')
                else:
                    print('#', end=' ')
            print()


game = GamePole(10, 12)

game.show()
