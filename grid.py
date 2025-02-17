import pygame

class Grid:
    def __init__(self, rows, columns):
        self.grid = {}
        self.rows = rows
        self.columns = columns
        
    def initialize_grid(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid[x, y] = 1
        

class Cell:
    def __init__(self, state, pos):
        self.state = state
        self.pos = pos
        