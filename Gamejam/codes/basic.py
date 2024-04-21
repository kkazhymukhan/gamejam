import pygame
import sys
import random


pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Загрузка музыки
background_song = pygame.mixer.Sound("music/backgraund.mp3")
background_song.play(-1)
stop_start = 0

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
player_speed = 13

running = True
hit_animation = False
mouse_button_down = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Удар!")
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
    if keys[pygame.K_d]:
        x -= player_speed
        shift_x=shift_x-player_speed
        animation="run"
        x1_enemy-=player_speed
        x2_enemy-=player_speed
        last_direction = "right"
    elif keys[pygame.K_a]:
        x += player_speed
        shift_x=shift_x+player_speed
        animation="run"
        x1_enemy+=player_speed
        x2_enemy+=player_speed
        last_direction = "left"
    if keys[pygame.K_s]:
        y -= player_speed
        shift_y=shift_y-player_speed
        animation="run"
        y1_enemy-=player_speed
        y2_enemy-=player_speed
    elif keys[pygame.K_w]:
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
    screen.blit(hearts[0], (10, 10))

    # Отображение и обновление позиции врагов
    for enemy in enemies:
        enemy.update(player_x, player_y, shift_x, shift_y,x1_enemy,x2_enemy, y1_enemy, y2_enemy)
        enemy.draw(screen,reverse_enemyRun, enemyRun, anim_divide, animEnemy)
        

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

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()


