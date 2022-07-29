from turtle import color
from data import config
from Game import units
from sys import exit
import numpy as np
import pygame
import game

settings = config.game()
CLOUDS = settings.textures['Clouds']
clouds_quant = settings.clouds_quant + 5
position_clouds = [[np.random.randint(300,900),np.random.randint(20,600)] for i in range(clouds_quant)]
velocity = [np.random.randint(1,8) /100 for i in range(clouds_quant)]
clouds = [CLOUDS[np.random.randint(1,4)] for i in range(clouds_quant)]
world_velocity = 0.0005

def main():
    settings = config.game()
    screen = pygame.display.set_mode(settings.screen)


    while True:

        screen.fill(settings.sky_mode()[1])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for cloud in range(clouds_quant):

            screen.blit(clouds[cloud],position_clouds[cloud])

            position_clouds[cloud][0] -= velocity[cloud]

            if position_clouds[cloud][0] <= -120:
                    position_clouds[cloud][0] = 1150

            velocity[cloud] += world_velocity / 100
    
        screen.blit(settings.show_text('Run Man',settings.font_title,(255,255,255)),(420,50))
        
        play = units.Button(460,300,settings.textures['buttons']['play'],screen,'play')

        play.draw()
        
        if play.clicked:
            play.clicked = False
            game.game_run()

        
        pygame.display.update()

if  __name__ == '__main__':
    main()