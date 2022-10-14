import pygame
from constants import *

class Player():
    def __init__(self, name: str):
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.direction = RIGHT
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.mooving = [0, 0, 0, 0]
        #self.image_pack = ['data/archerr.png','data/archerd.png','data/archerl.png','data/archeru.png']
        # self.images = []
        # for image in self.image_pack:
        #     temp = pygame.image.load(image).convert_alpha()
        #     i=[]
        #     i.append(temp.subsurface(0,0,64,64))
        #     i.append(temp.subsurface(64, 0, 64, 64))
        #     i.append(temp.subsurface(128, 0, 64, 64))
        #     self.images.append(i)
        temp = pygame.image.load('data/wizard.png').convert_alpha()
        i = []
        i.append(temp.subsurface(240, 186, 60, 88))
        i.append(temp.subsurface(0, 0, 60, 88))
        i.append(temp.subsurface(0, 363, 59, 87))
        i.append(temp.subsurface(300, 0, 60, 88))
        i.append(temp.subsurface(60, 0, 60, 88))
        self.image = i



    def moove(self):


        if self.mooving[RIGHT] == 1:
            self.x+=PLAYER_SPEED
        if self.mooving[DOWN]:
            self.y+=PLAYER_SPEED
        if self.mooving[LEFT]:
            self.x-=PLAYER_SPEED
        if self.mooving[UP]:
            self.y-=PLAYER_SPEED

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH-35: self.x = SCREEN_WIDTH-35
        if self.y >= SCREEN_HEIGHT-75: self.y = SCREEN_HEIGHT-75


    def render(self, screen):
       # screen.blit(self.images[self.direction][self.state], (self.x, self.y))
       screen.blit(self.image[self.direction], (self.x, self.y))
    def render_ui(self, screen):
        pass


