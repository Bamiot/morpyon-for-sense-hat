from random import randint

class morpyon:

    def __init__(self,grid,activated):
        self.grid = grid
        self.activated = activated

    def play(self,grid):
        self.grid = grid
        for i in range(3):
            if (grid[i][0] == grid[i][1] == 2) and (grid[i][2] == 0): return [i,2]
            elif (grid[i][0] == grid[i][2] == 2) and (grid[i][1] == 0): return [i, 1]
            elif (grid[i][2] == grid[i][1] == 2) and (grid[i][0] == 0): return [i, 0]
        for i in range(3):
            if (grid[0][i] == grid[1][i] == 2) and (grid[2][i] == 0): return [2,i]
            elif (grid[0][i] == grid[2][i] == 2) and (grid[1][i] == 0): return [1,i]
            elif (grid[2][i] == grid[1][i] == 2) and (grid[0][i] == 0): return [0,i]
        if (grid[0][0] == grid[1][1] == 2) and (grid[2][2] == 0): return [2,2]
        elif (grid[0][0] == grid[2][2] == 2) and (grid[1][1] == 0): return [1,1]
        elif (grid[2][2] == grid[1][1] == 2) and (grid[0][0] == 0): return [0,0]
        elif (grid[0][2] == grid[1][1] == 2) and (grid[2][0] == 0): return [2,0]
        elif (grid[0][2] == grid[2][0] == 2) and (grid[1][1] == 0): return [1,1]
        elif (grid[2][0] == grid[1][1] == 2) and (grid[0][2] == 0): return [0,2]
        else:
            #en dessou def | au dessus atk
            for i in range(3):
                if (grid[i][0] == grid[i][1] != 0) and (grid[i][2] == 0): return [i,2]
                elif (grid[i][0] == grid[i][2] != 0) and (grid[i][1] == 0): return [i, 1]
                elif (grid[i][2] == grid[i][1] != 0) and (grid[i][0] == 0): return [i, 0]
            for i in range(3):
                if (grid[0][i] == grid[1][i] != 0) and (grid[2][i] == 0): return [2,i]
                elif (grid[0][i] == grid[2][i] != 0) and (grid[1][i] == 0): return [1,i]
                elif (grid[2][i] == grid[1][i] != 0) and (grid[0][i] == 0): return [0,i]
            if (grid[0][0] == grid[1][1] != 0) and (grid[2][2] == 0): return [2,2]
            elif (grid[0][0] == grid[2][2] != 0) and (grid[1][1] == 0): return [1,1]
            elif (grid[2][2] == grid[1][1] != 0) and (grid[0][0] == 0): return [0,0]
            elif (grid[0][2] == grid[1][1] != 0) and (grid[2][0] == 0): return [2,0]
            elif (grid[0][2] == grid[2][0] != 0) and (grid[1][1] == 0): return [1,1]
            elif (grid[2][0] == grid[1][1] != 0) and (grid[0][2] == 0): return [0,2]
            elif grid[1][1] == 0:
                return [1,1]
            else:
                x = randint(0,2)
                y = randint(0,2)
                enable = True
                while enable:
                    if self.grid[x][y] != 0:
                        enable = True
                        x = randint(0, 2)
                        y = randint(0, 2)
                    elif self.grid[x][y] == 0 :
                        enable = False
                return [x,y]