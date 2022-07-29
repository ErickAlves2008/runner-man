import numpy as np
import game
import pygame

try:
    from game import settings
except ModuleNotFoundError and ImportError:
    from main import settings

ROCKS = settings.textures['rocks']

class rock:

    rock_type = 1

    def __init__(self,velocity,win):

        self.img = ROCKS[np.random.randint(0,3)]
        self.position = pygame.Vector2(1300,563)
        self.rocks = [self]
        self.velocity = velocity
        self.win = win

    def draw(self):

        self.position[0] -= self.velocity

        self.win.blit(self.img,self.position)

class rock2:
    rock_type = 2

    def __init__(self,distance,velocity,win):
        
        self.rock_1 = rock(velocity,win)
        self.rock_2 = rock(velocity,win)
        self.rocks = [self.rock_1,self.rock_2]

        self.rock_2.position[0] = self.rock_1.position[0] + distance
        self.position = self.rock_2.position
        self.velocity = velocity
        self.win = win

    def draw(self):

        self.rock_1.position[0] -= self.velocity
        self.rock_2.position[0] -= self.velocity

        self.win.blit(self.rock_1.img,self.rock_1.position)
        self.win.blit(self.rock_2.img,self.rock_2.position)

class rock3:
    rock_type = 3

    def __init__(self,distance,velocity,win):
        
        self.rock_1 = rock(velocity,win)
        self.rock_2 = rock(velocity,win)
        self.rock_3 = rock(velocity,win)
        self.rocks = [self.rock_1,self.rock_2,self.rock_3]

        self.rock_2.position[0] = self.rock_1.position[0] + distance
        self.rock_3.position[0] = self.rock_2.position[0] + distance
        self.position = self.rock_3.position
        self.velocity = velocity
        self.win = win

    def draw(self):

        self.rock_1.position[0] -= self.velocity
        self.rock_2.position[0] -= self.velocity
        self.rock_3.position[0] -= self.velocity

        self.win.blit(self.rock_1.img,self.rock_1.position)
        self.win.blit(self.rock_2.img,self.rock_2.position)
        self.win.blit(self.rock_3.img,self.rock_3.position)

def generate_rock(velocity,win,distance):

    choice = np.random.randint(0,6)

    if choice < 2:
        return rock(velocity,win)
    elif choice < 5:
        return rock2(distance,velocity,win)
    else:
        return rock3(distance,velocity,win)