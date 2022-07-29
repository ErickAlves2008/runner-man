from Game import Player, Rocks,units
from data import config
from sys import exit
import numpy as np
import pygame
import main
import math
settings = config.game()
screen = pygame.display.set_mode(settings.screen)

TERRAIN1,TERRAIN2 = settings.textures['Terrain'],settings.textures['Terrain']
GAME_OVER = settings.textures['Game_Over']
PLAYER = settings.textures['Player']
CLOUDS = settings.textures['Clouds']
EXTRAS = settings.textures['Extras']
SATELLITE = settings.sky_mode()[0]

RESTART = units.Button(200,500,settings.textures['buttons']['restart'],screen,'restart')
MENU = units.Button(800,500,settings.textures['buttons']['menu'],screen,'menu')

#game
game_state = True

def game_run():
    pygame.init()

    #sun
    sun_angle = 0
    world_velocity = 0.0005

    # DECORATION

    #Clouds

    clouds_quant = settings.clouds_quant
    position_clouds = [[np.random.randint(700,900),np.random.randint(20,300)] for i in range(clouds_quant)]
    velocity = [np.random.randint(1,8) /10 for i in range(clouds_quant)]
    clouds = [CLOUDS[np.random.randint(1,4)] for i in range(clouds_quant)]

    # extras

    extras = []
    extras_position = []

    # terrain

    y_terrain = 300
    position_terrain = [[-700,y_terrain],[410,y_terrain]]

    #player
    player = Player.Player((100,490),settings.start_speed)
    points = 0
    max_points = settings.player_achievements['max_points']
    clock = pygame.time.Clock()
    jump_permission = False

    #rocks

    rock_distance = 65
    d = Rocks.generate_rock(player.velocity,screen,rock_distance)
    d.position.x += 600
    rocks = [Rocks.generate_rock(player.velocity,screen,rock_distance),d]

    while game_state:

        clock.tick(settings.fps)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                settings.save()
                exit()

            if event.type == pygame.KEYDOWN:
                    
                if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    jump_permission = True
                    player.jump()

        
        screen.fill(settings.sky_mode()[1])

        #Sun
        sun_angle += 0.01
        sun = pygame.transform.rotate(SATELLITE,sun_angle)
        screen.blit(sun,(20,20))
                
        #Clouds
        for cloud in range(clouds_quant):

            screen.blit(clouds[cloud],position_clouds[cloud])

            position_clouds[cloud][0] -= velocity[cloud]

            if position_clouds[cloud][0] <= -120:
                    position_clouds[cloud][0] = 1150

            velocity[cloud] += world_velocity / 100

        #extras

        luck = np.random.randint(0,70000)

        if luck <= 5:
            extras.append(EXTRAS[0])
            extras_position.append([1300,np.random.randint(20,300)])

        elif luck > 5 and luck <= 10:
            extras.append(EXTRAS[np.random.randint(1,3)])
            extras_position.append([1300,np.random.randint(20,300)])

        elif luck > 10 and luck <= 13:
            extras.append(EXTRAS[4])
            extras_position.append([1300,np.random.randint(20,300)])

        elif luck == 50:
            extras.append(EXTRAS[5])
            extras_position.append([1300,np.random.randint(20,300)])

        if len(extras) > 0:

            for extra in range(len(extras)):
                extras_position[extra][0] -= 9
                screen.blit(extras[extra],extras_position[extra])


        # Terrain
        screen.blit(TERRAIN1,position_terrain[0])
        screen.blit(TERRAIN2,position_terrain[1])

        for terrain in range(2):
            screen.blit(TERRAIN1,position_terrain[0])
            screen.blit(TERRAIN2,position_terrain[1])

            position_terrain[terrain][0] -= player.velocity

            if position_terrain[terrain][0] <= -1200:
                position_terrain[terrain][0] = 1000

            #player
            player.draw()
            player.velocity += world_velocity

            if jump_permission:

                if player.position.y >= 490:

                    player.position.y = 490
                    jump_permission = False
                    player.force = player.start_force

                player.jump()

            screen.blit(player.sprites[player.sprite],player.position)

            if player.velocity > settings.limit_speed:
                world_velocity = 0

        #rocks

        for rock in rocks:

            if rock.position[0] < -(np.random.randint(130,180)*player.velocity):
                rocks_distance = np.random.randint(200,500)
                rocks.remove(rock)
                rocks.append(Rocks.generate_rock(player.velocity,screen,rock_distance))
                timer = True

            for part in rock.rocks:
                        
                if units.isCollision(part.position[0],part.position[1],player.position.x,player.position.y,90)[0]:
                    game_over(points)
                    break

            rock.draw()

        points += 0.02

        screen.blit(settings.show_text(f"Score: {round(points,1):.1f}",settings.font,(255,255,255)),(10,160))
        screen.blit(settings.show_text(f"Max Points: {settings.player_achievements['max_points']}",settings.font2,(255,255,255)),(10,180))

        screen.blit(settings.show_text(f"Velocity: {round(player.velocity,1):.1f}",settings.font2,(255,255,255)),(1000,20))
        screen.blit(settings.show_text(f"Max Velocity: {settings.limit_speed}",settings.font3,(255,255,255)),(1010,40))

        pygame.display.update()

def game_over(points):

    units.check_for_save(points,settings)

    settings.save()

    while game_state:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()

        screen.fill((0,0,0))
        screen.blit(GAME_OVER,(350,100))

        RESTART.draw()
        MENU.draw()

        if RESTART.clicked:
            RESTART.clicked = False
            game_run()
            break

        if MENU.clicked:
            MENU.clicked = False
            main.main()

        pygame.display.update()

if __name__ == "__main__":
    game_run()