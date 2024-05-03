import os
import pygame
import sys
import random
import image
from import_image import image

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BOSS FIGHTING")
boss_image = image.boss
start_time = pygame.time.get_ticks()
water_height = 0
water_speed = 1
show_water = False
water_duration = 1500
water_counter = water_duration
show_safe_zone = False
safe_zone_duration = 3000
safe_zone_counter = safe_zone_duration
last_direction="right"
bg_anim=0
anim=0
anim_last=5
divid_anim=3
class Boss:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT //2 - 100
        self.HP = 3


hearts_images = image.hearts
heart_index = 0

player_images = image.playerRun
player_hit_image = image.playerHit

player_rect = player_images[0].get_rect()
player_rect.centerx = WIDTH // 2
player_rect.bottom = HEIGHT - 10
player_speed = 7
current_player_img_index = 0

# Rectangle boundaries
left_boundary = 75
right_boundary = 565
top_boundary = 59
bottom_boundary = 567

interval_timer = 1000

last_anim_boss=7
anim_boss=0
divid_anim_boss=4

boss_health = 3
enemy_timer = 5000
safe_zone_timer = 3000
countdown_timer = 3000
water_active = False

background_imgs = image.boss_bg
background_img = pygame.transform.scale(background_imgs[0], (600, 600))
background_rect = background_img.get_rect()
platform=pygame.transform.scale(pygame.image.load("image/boss/platform.png"), (100, 80))
safe_zone_x1, safe_zone_x2, safe_zone_y1, safe_zone_y2 = 0, 0, 0, 0
boss = Boss()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if anim_boss==last_anim_boss:
        anim_boss=0
    else :
        anim_boss+=1
    
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

    player_rect.x = max(left_boundary, min(player_rect.x, right_boundary - player_rect.width))
    player_rect.y = max(top_boundary, min(player_rect.y, bottom_boundary - player_rect.height))
    
    

    enemy_timer -= 60
    if enemy_timer <= 0 and not water_active:
        water_active = True
        safe_zone_x1 = random.randint(left_boundary, right_boundary - 100)
        safe_zone_x2 = random.randint(left_boundary, right_boundary - 100)
        safe_zone_y1 = random.randint(top_boundary, bottom_boundary - 20)
        safe_zone_y2 = random.randint(top_boundary, bottom_boundary - 20)
        enemy_timer = 4000
    if water_active:
        safe_zone_timer -= 60
        pygame.draw.rect(screen, RED, (safe_zone_x1, safe_zone_y1, 80, 70))
        pygame.draw.rect(screen, RED, (safe_zone_x2, safe_zone_y2, 80, 70))
        if safe_zone_timer <= 0:
            pygame.draw.rect(screen, BLUE, (left_boundary, top_boundary, right_boundary - left_boundary, bottom_boundary - top_boundary))
            countdown_timer -= 60
            if (not (player_rect.x - 120 <= safe_zone_x1 and player_rect.x + 120 >= safe_zone_x1 and player_rect.y - 96 <= safe_zone_y1 and player_rect.y + 96 >= safe_zone_y1)
                    and not (player_rect.x - 120 <= safe_zone_x2 and player_rect.x + 120 >= safe_zone_x2 and player_rect.y - 96 <= safe_zone_y2 and player_rect.y + 96 >= safe_zone_y2)):
                interval_timer -= 60
            if interval_timer < 1:
                print('e')
                heart_index += 1
                interval_timer = 1000
        pygame.draw.rect(screen, RED, (safe_zone_x1, safe_zone_y1, 80, 70))
        pygame.draw.rect(screen, RED, (safe_zone_x2, safe_zone_y2, 80, 70))
        if countdown_timer <= 0:
            enemy_timer = 5000
            safe_zone_timer = 3000
            water_active = False
            countdown_timer = 3000
    if heart_index >= len(hearts_images) - 1:
        running = False

    if bg_anim<20:
        screen.blit(background_img, background_rect)
    if bg_anim<150 and bg_anim>20:
        screen.blit(background_imgs[1], background_rect)
    if bg_anim>600:
        screen.blit(background_imgs[4], background_rect)
    bg_anim+=1
    screen.blit(hearts_images[heart_index], (10, 10))
    screen.blit(boss_image[anim_boss//divid_anim_boss], (170,40))
    screen.blit(platform, (safe_zone_x1, safe_zone_y1))
    screen.blit(platform, (safe_zone_x2, safe_zone_y2))

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        screen.blit(player_hit_image[1], player_rect)
        if boss.rect.x + 50 >= player_rect.x and boss.rect.x - 50 <= player_rect.x:
            if boss.rect.y + 50 >= player_rect.y and boss.rect.y  - 50 <= player_rect.y:
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
                    print(anim)
            else:
                if last_direction == "left":
                    screen.blit(player_images[0], (player_rect.x, player_rect.y))
                else:
                    screen.blit(player_images[0], (player_rect.x, player_rect.y))

    if boss_health == 0:
        running = False
    pygame.display.flip()

    pygame.time.Clock().tick(15)

pygame.quit()   
sys.exit()