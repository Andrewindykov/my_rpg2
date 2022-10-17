import pygame
import time
from pygame.locals import *
from constants import *
from MyPlayer import Player
from Projective import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player('Grut')
        self.projective = []
        self.background = pygame.image.load('data/background.jpg')
        self.running = True
        self.count = 0

        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == USEREVENT+1:
                self.player.tick()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.mooving = [1,0,0,0]
                if event.key == K_DOWN:
                     self.player.mooving = [0,1,0,0]
                if event.key == K_LEFT:
                       self.player.mooving = [0,0,1,0]
                if event.key == K_UP:
                    self.player.mooving = [0,0,0,1]

                if event.key == K_SPACE:
                    self.player.hp-=5
                    if self.player.state != DEAD:
                        self.player.state = DEAD
                        self.player.direction = DIE
                    else:
                        self.player.state = ALIVE
                        self.player.direction = UP

                if event.key == K_z:
                    if self.player.mp >= SKILL1_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL1_COST
                        self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()


                        if self.player.direction == RIGHT:
                            self.projective.append(Arrow(self.player.x+12, self.player.y, self.player.direction))
                        elif self.player.direction == DOWN:
                            self.projective.append(Arrow(self.player.x, self.player.y+12, self.player.direction))
                        elif self.player.direction == LEFT:
                            self.projective.append(Arrow(self.player.x-12, self.player.y, self.player.direction))
                        else:
                            self.projective.append(Arrow(self.player.x, self.player.y-12, self.player.direction))

                if event.key == K_x:
                    if self.player.mp >= SKILL2_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL2_COST
                        self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()


                        if self.player.direction == RIGHT:
                            self.projective.append(Firearrow(self.player.x+12, self.player.y, self.player.direction))
                        elif self.player.direction == DOWN:
                            self.projective.append(Firearrow(self.player.x, self.player.y+12, self.player.direction))
                        elif self.player.direction == LEFT:
                            self.projective.append(Firearrow(self.player.x-12, self.player.y, self.player.direction))
                        else:
                            self.projective.append(Firearrow(self.player.x, self.player.y-12, self.player.direction))




            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.mooving[RIGHT] = 0
                if event.key == K_DOWN:
                    self.player.mooving[DOWN] = 0
                if event.key == K_LEFT:
                    self.player.mooving[LEFT] = 0
                if event.key == K_UP:
                    self.player.mooving[UP] = 0


    def render(self):

        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.projective:
            i.render(screen)
        pygame.display.flip()

    def main_loop(self):
        while self.running == True:
            if self.player.state != DEAD:
                self.player.moove()
            for i in self.projective:
                i.moove()
            self.render()
            self.handle_events()
            #self.pygame.time.Clock.tick(33)
            clock.tick(50)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT+1, 100)
game = Main(screen)