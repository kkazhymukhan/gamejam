import pygame
import sys
import random
import math 
from UI import Button
from UI import Lose
from poligon import Poligon



def restart_game():
    global i, x, y, x1_enemy, x2_enemy, y1_enemy, y2_enemy, enemies, player_x, player_y, running
    i = 0
    x = -50
    y = -500
    x1_enemy = 843
    x2_enemy = 1350
    y1_enemy = 120
    y2_enemy = 670
    enemies = [Enemy(random.randint(x1_enemy, x2_enemy), random.randint(y1_enemy, y2_enemy), 4) for _ in range(5)]
    player_x, player_y = screen_width // 2, screen_height // 2
    running = True

pygame.init()
button=Button(True)
lose=Lose(True)

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
poligon=Poligon()


# Загрузка музыки
background_song = pygame.mixer.Sound("music/backgraund.mp3")
stop_start = 0
background_UI_song = pygame.mixer.Sound("music/backgraund_UI.mp3")
background_UI_song.play()
ui_visible = True


hit_sound = [
    pygame.mixer.Sound("music/hit1.mp3"),
    pygame.mixer.Sound("music/hit2.mp3")
]
number_sound = 0

# Координаты
x = -50
y = -500
x1_enemy = 843
x2_enemy = 1350
y1_enemy = 120
y2_enemy = 670

# Загрузка изображений
from import_image import image
hearts=image.hearts
enemyRun=image.enemyRun
playerHit=image.playerHit
playerRun=image.playerRun
reverse_enemyRun=image.reverse_enemyRun
reverse_playerHit=image.reverse_playerHit
reverse_playerRun=image.reverse_playerRun

level1_image = pygame.image.load("image/level1.png")
level1 = pygame.transform.scale(level1_image, (2400, 2400))
# Настройки анимации
i=0
animEnemy = 0
anim = 0
anim_heart = 0
anim_last = 1
anim_divide = 1
enemyAnimation = "run"

last_direction = "right"

# Класс для врагов
from enemy import Enemy

# Создание врагов
enemies = [Enemy(random.randint(x1_enemy, x2_enemy), random.randint(y1_enemy, y2_enemy), 4) for _ in range(5)]

# Позиция игрока
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 15

running = True
hit_animation = False
mouse_button_down = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    


    if button.visible:
        button.Menu(screen)
        button.handle_event(event)
        ui_visible = True


    elif button.visible==False:
        


        if ui_visible==True:
            background_UI_song.stop()
            background_song.play()
            ui_visible = False
        
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #print("Удар!")
                hit_animation = True
                animation="hit"
                if number_sound == 0:
                    hit_sound[0].play()
                    number_sound = 1
                else:
                    hit_sound[1].play()
                    number_sound = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                hit_animation = False
    # Движение игрока
        keys = pygame.key.get_pressed()
        shift_x=0
        shift_y=0
        animation = "peace"
        
        if keys[pygame.K_d] and poligon.is_inside_polygons(x-player_speed,y):
            x -= player_speed
            shift_x=shift_x-player_speed
            animation="run"
            x1_enemy-=player_speed
            x2_enemy-=player_speed
            last_direction = "right"
        elif keys[pygame.K_a] and poligon.is_inside_polygons(x+player_speed,y):
            x += player_speed
            shift_x=shift_x+player_speed
            animation="run"
            x1_enemy+=player_speed
            x2_enemy+=player_speed
            last_direction = "left"
        if keys[pygame.K_s] and poligon.is_inside_polygons(x,y-player_speed):
            y -= player_speed
            shift_y=shift_y-player_speed
            animation="run"
            y1_enemy-=player_speed
            y2_enemy-=player_speed
        elif keys[pygame.K_w]and poligon.is_inside_polygons(x,y+player_speed):
            y += player_speed
            shift_y=shift_y+player_speed
            animation="run"
            y1_enemy+=player_speed
            y2_enemy+=player_speed



        if enemyAnimation=="run":
                if animEnemy==anim_last:
                    animEnemy=0
                else:
                    animEnemy +=1
        if animation=="hit":
                if anim==anim_last:
                    anim=0
                else:
                    anim +=1

        elif animation=="run":
               if anim==anim_last:
                    anim=0
               else:
                    anim +=1
    

    # Отображение фона
        screen.blit(level1, (x, y))

    # Отображение сердец
        screen.blit(hearts[i], (10, 10))
        poligon.draw(screen)
        poligon.is_inside_polygons(x,y)
        
        
    # Отображение и обновление позиции врагов
        for enemy in enemies:
            enemy.update(player_x, player_y, shift_x, shift_y,x1_enemy,x2_enemy, y1_enemy, y2_enemy)
            enemy.draw(screen,reverse_enemyRun, enemyRun, anim_divide, animEnemy)
            if enemy.x  + 50 >= player_x and enemy.x - 50 <= player_x:
                if enemy.y + 50 >= player_y and enemy.y - 50 <= player_y:
                    angle = math.atan2(player_y - enemy.y, player_x - enemy.x)
                    enemy.x += 10*enemy.speed * math.cos(angle+math.pi)
                    enemy.y += 10*enemy.speed * math.sin(angle+math.pi)
                    enemy.draw(screen,reverse_enemyRun, enemyRun, anim_divide, animEnemy)
                    if i<9:
                        i+=1
                    #print(i)
                    #print(len(hearts))
                    
            
                #print("VJVJSVBKJBVJKBVJKBKJBJKSJBVKSBVVJBJKBKVS")


    # Анимация удара
        if hit_animation:
            if last_direction == "left":
                screen.blit(reverse_playerHit[anim // anim_divide], (player_x, player_y))
            else:
                screen.blit(playerHit[anim // anim_divide], (player_x, player_y))
        
        else:
        # Анимация бега только при движении
        
            if last_direction == "left":
                screen.blit(reverse_playerRun[anim // anim_divide], (player_x, player_y))
            else:
                screen.blit(playerRun[anim // anim_divide], (player_x, player_y))
            
        
            # Отображение стоящего персонажа
            if last_direction == "left":
                screen.blit(reverse_playerRun[anim // anim_divide], (player_x, player_y))
            else:
                screen.blit(playerRun[anim // anim_divide], (player_x, player_y))

    # Остановка и возобновление музыки
        if keys[pygame.K_t]:
            background_song.stop()
            stop_start = 1
        if keys[pygame.K_y] and stop_start == 1:
            background_song.play()
            stop_start = 0
    


    if i >= len(hearts)-1:
        lose.restart_clicked=True
        lose.Menu(screen)
        lose.handle_event(event)


        if lose.restart_clicked==False:
            restart_game()
        
    #print(x,",",y)
        
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()


