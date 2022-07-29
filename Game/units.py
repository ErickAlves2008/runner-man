from numpy import rad2deg
import pygame
import math

def isCollision(enemy_x,enemy_y,bullet_x,bullet_y,distance_for_collider):
    distance = math.sqrt( (math.pow(enemy_x - bullet_x,2)) + (math.pow(enemy_y - bullet_y,2)))

    if distance <= distance_for_collider:
        return [True,distance]
    else:
        return [False,distance]

class Button():
    def __init__(self,x,y,image,win,name):

        self.image = image
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2()
        self.position.xy = x,y
        self.clicked = False
        self.name = name
        self.win = win

        
    def draw(self):
        pos = pygame.mouse.get_pos()

        self.rect.topleft =  self.position

        if self.rect.collidepoint(pos):

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print(f'Clicked {self.name}')

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.win.blit(self.image, self.position)

def check_for_save(points, settings):

    p = False

    if settings.player_achievements['max_points'] < points:
        p = True

    if p:
        settings.player_achievements['max_points'] = round(points,1)
