from re import S
import pygame
import time

class Player:

    start_force = 8
    sprite_num = 0
    force = start_force
    comedown = True

    def __init__(self, position,velocity):

        self.sprites = [pygame.image.load('Img\player1.png'),pygame.image.load('Img\player2.png')]
        self.position = pygame.Vector2(position[0],position[1])
        self.sprite = 0
        self.velocity = velocity

    def draw(self):

        h = self.velocity/2

        if self.velocity > 14:
            h = 1
        
        if self.sprite_num >= 0 and self.sprite_num <= 2*h:
            self.sprite = 1
            self.sprite_num += 1

        elif self.sprite_num > 2*h and self.sprite_num <= 4*h:
            self.sprite = 0
            self.sprite_num += 1

        elif self.sprite_num > 4*h:
            self.sprite = 0
            self.sprite_num = 0

    def jump(self):
        self.position.y -= self.force
        self.force -= 0.2