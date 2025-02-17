import pygame
import sys
from grid import Grid

class Game:
    def __init__(self):
        
        self.SCREEN_HEIGHT = 1024
        self.SCREEN_WIDTH = 720
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((self.SCREEN_HEIGHT, self.SCREEN_WIDTH))
        self.clock = pygame.time.Clock()
        
        self.grid = Grid(10, 10)
        
    def run(self):
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill("black")
            pygame.display.flip()
            self.clock.tick(60)
                        
        
        pygame.quit()
    
Game().run()