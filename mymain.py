import pygame
from constants import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.main_loop()

    def handle_events(self):
        pass

    def render(self):

        self.screen.blit(self.background,(0,0))
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            self.render()
# проверка связи
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game = Main(screen)