import os
import pygame
import sys
import random
import image
from import_image import image

pygame.init()


# Установка экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BOSS FIGHTING")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen.fill(WHITE)
# Загрузка изображений
boss_image = image.boss
hearts_images = image.hearts
player_images = image.playerRun
player_hit_image = image.playerHit
background_imgs = image.boss_bg
platform = pygame.transform.scale(pygame.image.load("image/boss/platform.png"), (100, 80))
win_image=image.win



boss_health = 10
heart_index = 0
current_player_img_index = 0
anim = 0
anim_last = 5
divid_anim = 3
last_direction = "right"
bg_anim = 0
anim_boss = 0
last_anim_boss = 7
divid_anim_boss = 4
frame=0

# Границы прямоугольника
left_boundary = 75
right_boundary = 565
top_boundary = 59
bottom_boundary = 567
background_img = pygame.transform.scale(background_imgs[0], (600, 600))
safe_zone_x1, safe_zone_x2, safe_zone_y1, safe_zone_y2 = -500, -500, 0, 0

# Объекты игры
class Boss:
    def __init__(self):
        self.x = 270
        self.y = 40

boss = Boss()
player_rect = player_images[0].get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 7

# Таймеры и флаги
interval_timer = 1000
enemy_timer = 5000
safe_zone_timer = 3000
countdown_timer = 3000
water_active = False
show_water = False
water_duration = 1500
water_counter = water_duration
show_safe_zone = False
safe_zone_duration = 3000
safe_zone_counter = safe_zone_duration

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
        current_player_img_index = (current_player_img_index + 1) % len(player_images)
        last_direction = "left"
    if keys[pygame.K_d]:
        player_rect.x += player_speed
        current_player_img_index = (current_player_img_index + 1) % len(player_images)
        last_direction = "right"
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
        current_player_img_index = (current_player_img_index + 1) % len(player_images)
    if keys[pygame.K_s]:
        player_rect.y += player_speed
        current_player_img_index = (current_player_img_index + 1) % len(player_images)

    # Гарантия, что игрок остается в пределах границ
    player_rect.x = max(left_boundary, min(player_rect.x, right_boundary - player_rect.width))
    player_rect.y = max(top_boundary, min(player_rect.y, bottom_boundary - player_rect.height))
    
    # Обновление таймеров и состояния игры
    enemy_timer -= 60
    if enemy_timer <= 0 and not water_active:
        water_active = True
        safe_zone_x1 = random.randint(left_boundary, right_boundary - 100)
        safe_zone_x2 = random.randint(left_boundary, right_boundary - 100)
        safe_zone_y1 = random.randint(top_boundary+200, bottom_boundary - 200)
        safe_zone_y2 = random.randint(top_boundary+200, bottom_boundary - 200)
        enemy_timer = 4000
    #print(player_rect.x,",",player_rect.y,"______",safe_zone_x1,",",safe_zone_x1+80,"__", safe_zone_y1,",", safe_zone_y1-70)
    if water_active:
        safe_zone_timer -= 60
        #print("relax")
        if safe_zone_timer <= 0:
            #print("water")
            countdown_timer -= 60
            if (player_rect.x>safe_zone_x1-20 and player_rect.x<safe_zone_x1+60 and player_rect.y<safe_zone_y1 and player_rect.y>safe_zone_y1-70) or (player_rect.x>safe_zone_x2-20 and player_rect.x<safe_zone_x2+60 and player_rect.y<safe_zone_y2 and player_rect.y>safe_zone_y2-70):
                #print("YEAH")
                pass
            elif countdown_timer < 1:
                heart_index += 1
        if countdown_timer <= 0:
            enemy_timer = 5000
            safe_zone_timer = 3000
            water_active = False
            countdown_timer = 3000
        if heart_index >= len(hearts_images) - 1:
            running = False

    # Обновление счетчиков анимации
    if anim_boss == last_anim_boss:
        anim_boss = 0
    else:
        anim_boss += 1
    if bg_anim >1:
        screen.blit(background_imgs[0], (100,0))
    if bg_anim >30:
        screen.blit(background_imgs[1], (100,0))
    if safe_zone_timer < 1500:
        screen.blit(background_imgs[2], (100,0))
    if safe_zone_timer < 1100:
        screen.blit(background_imgs[3], (100,0))
    if safe_zone_timer < 600:
        screen.blit(background_imgs[4], (100,0))
    if safe_zone_timer <200:
        screen.blit(background_imgs[5], (100,0))
    if safe_zone_timer <=0:
        screen.blit(background_imgs[6], (100,0))
    if countdown_timer < 800:
        screen.blit(background_imgs[7], (100,0))
    if countdown_timer < 600:
        screen.blit(background_imgs[8], (100,0))
    if countdown_timer <400:
        screen.blit(background_imgs[9], (100,0))
    if countdown_timer <200:
        screen.blit(background_imgs[10], (100,0))

    bg_anim += 1

    # Рендеринг игровых элементов
    screen.blit(hearts_images[heart_index], (10, 10))
    screen.blit(boss_image[anim_boss // divid_anim_boss], (boss.x, boss.y))
    screen.blit(platform, (safe_zone_x1, safe_zone_y1))
    screen.blit(platform, (safe_zone_x2, safe_zone_y2))
    #print(player_rect.x,",", player_rect.y, "_             _", boss.y+50,",", boss.y-50)


    # Анимация движения игрока
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        screen.blit(player_hit_image[1], player_rect)
        if boss.x + 170 >= player_rect.x and boss.x - 70 <= player_rect.x:
            if boss.y + 70 >= player_rect.y and boss.y  - 50 <= player_rect.y:
                boss_health -= 1 
                print("-1")
    else:
        if keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d]:
            if last_direction == "left":
                screen.blit(player_images[anim // divid_anim], (player_rect.x, player_rect.y))
            else:
                screen.blit(player_images[anim // divid_anim], (player_rect.x, player_rect.y))
            if anim == anim_last:
                anim = 0
            else:
                anim += 1
        else:
            if last_direction == "left":
                screen.blit(player_images[0], (player_rect.x, player_rect.y))
            else:
                screen.blit(player_images[0], (player_rect.x, player_rect.y))
    if boss_health<1:
        if frame>1:
            screen.blit(win_image[0],(0,0))
        if frame>2:
            screen.blit(win_image[1],(0,0))
        if frame>4:
            screen.blit(win_image[2],(0,0))
        if frame>6:
            screen.blit(win_image[3],(0,0))
            if frame==8:
                frame=1
        print(frame)
        frame+=1
    pygame.display.flip()
    pygame.time.Clock().tick(15)

pygame.quit()   
sys.exit()
