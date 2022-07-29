import pygame
import json

with open('data\info.json','r') as data_file:
    data = json.load(data_file)

class game:

    pygame.init()

    textures = {
        'buttons':{
            'restart': pygame.image.load(r'Buttons\game\Restart.png'),
            'play': pygame.image.load(r'Buttons\home\Play.png'),
            'menu': pygame.image.load(r'Buttons\game\Menu.png')
        },  
        'rocks':[pygame.transform.scale(pygame.image.load(rf'Img\rocks\rock{num}.png'),(50,50)) for num in range(1,4)],
        'Player':[pygame.image.load(r'Img\player1.png'),pygame.image.load('Img\player2.png')],
        'Clouds':[pygame.image.load(rf'Img\Clouds\cloud{num}.png') for num in range(1,5)],
        'Extras':[pygame.image.load(rf'Img\extras\extra{num}.png') for num in range(1,7)],
        'Game_Over':pygame.image.load(r'Img\Game Over.png'),
        'Terrain':pygame.image.load(r'Img\Terrain.png'),
        'Moon':pygame.image.load(r'Img\Moon.png'),
        'Sun':pygame.image.load(r'Img\Sun.png')
    }


    player_achievements = {
        "rounds_played": data["player_data"]["rounds_played"],
        "max_points": data["player_data"]["max_points"],
        "max_speed": data["player_data"]["max_speed"],
        "money": data["player_data"]["money"],
        "skin": data["player_data"]["skin"],
    }

    start_speed = data['game_settings']['start_speed']
    font_title = pygame.font.Font('freesansbold.ttf', 50)
    font = pygame.font.Font('freesansbold.ttf', 20)
    font2 = pygame.font.Font('freesansbold.ttf', 15)
    font3 = pygame.font.Font('freesansbold.ttf', 10)
    font4 = pygame.font.Font('freesansbold.ttf', 8)
    limit_speed = data['game_settings']['limit_speed']
    clouds_quant = data['clouds_quant']
    screen = data['screen']
    mode = data['mode']
    fps = data['fps']

    def sky_mode(self):
        
        if self.mode == 'night':
            return [self.textures['Moon'],(36, 36, 36),(255,255,255)]
        else:
            return [self.textures['Sun'],(5, 134, 255),(0,0,0)]

    def show_text(self,point,font_type,color):

        score = font_type.render(f"{point}",True,color)
        return score

    def save(self):
        data["player_data"]["rounds_played"] = self.player_achievements['rounds_played']
        data['player_data']['max_points'] = self.player_achievements['max_points']
        data['player_data']['max_speed'] = self.player_achievements['max_speed']
        data['player_data']['money'] = self.player_achievements['money']
        data["player_data"]["skin"] = self.player_achievements['skin']
        data['game_settings']['start_speed'] = self.start_speed
        data['game_settings']['limit_speed'] = self.limit_speed
        data['clouds_quant'] = self.clouds_quant
        data['screen'] = self.screen
        data['mode'] = self.mode
        
        with open('data\info.json','w') as data_file:
            data_file.write(json.dumps(data,indent=2))