import pygame
import sys
import random
import math

pygame.init()
screen_width, screen_height = 800,800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


#music
pygame.mixer.music.load("music/backgraund.mp3")
pygame.mixer.music.play(-1)

#coordinates
x=0
y=0
x1_enemy=923
x2_enemy=1450
y1_enemy=650
y2_enemy=1200



#loading image
playerRun= [
        pygame.transform.scale(pygame.image.load("image/run/run1.png"), (70,70)),
        pygame.transform.scale(pygame.image.load("image/run/run2.png"), (70,70))
]


enemyRun= [
        pygame.transform.scale(pygame.image.load("image/enemy/enemy1.png"), (70,70)),
        pygame.transform.scale(pygame.image.load("image/enemy/enemy2.png"), (70,70))
]

playerHit= [
        pygame.transform.scale(pygame.image.load("image/hit/hit1.png"), (70,70)),
        pygame.transform.scale(pygame.image.load("image/hit/hit2.png"), (70,70))
]
reverse_playerRun=[
        pygame.transform.flip(playerRun[0], True,False),
        pygame.transform.flip(playerRun[1], True,False)
     
]
reverse_playerHit=[
        pygame.transform.flip(playerHit[0], True,False),
        pygame.transform.flip(playerHit[1], True,False)
     
]
reverse_enemyRun=[
        pygame.transform.flip(enemyRun[0], True,False),
        pygame.transform.flip(enemyRun[1], True,False)
     
]
level1_image=pygame.image.load("image/level1.png")
level1=pygame.transform.scale(level1_image, (2400,2400))

#animation settings
animEnemy=0
anim=0
anim_last=3
anim_divide=2
enemyAnimation="run"
last_direction = "right"

# Класс для врагов
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])

    # Метод для отображения врага
    def draw(self):
        if self.direction=="right":
            screen.blit(reverse_enemyRun[animEnemy//anim_divide], (self.x, self.y))
        else:
            screen.blit(enemyRun[animEnemy//anim_divide], (self.x, self.y))
    # Метод для обновления позиции врага
    def update(self, player_x, player_y, shift_x, shift_y):
        self.x=self.x+shift_x
        self.y=self.y+shift_y
        if self.is_player_visible(player_x, player_y):
            # Движение в направлении игрока
            angle = math.atan2(player_y - self.y, player_x - self.x)
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)
        else:
            # Движение в рандомном направлении
            if self.direction == "up":
                self.y -= self.speed
            elif self.direction == "down":
                self.y += self.speed
            elif self.direction == "left":
                self.x -= self.speed
            elif self.direction == "right":
                self.x += self.speed

            # Смена направления при достижении края экрана
            if self.x < x1_enemy or self.x > x2_enemy or self.y < y1_enemy or self.y > y2_enemy:
                self.direction = random.choice(["up", "down", "left", "right"])

    # Метод для определения видимости игрока
    def is_player_visible(self, player_x, player_y):
        distance = math.sqrt((player_x - self.x) ** 2 + (player_y - self.y) ** 2)
        return distance < 200  # Расстояние видимости

# Создание врагов
enemies = [Enemy(random.randint(923,1500), random.randint(650,1250), 4) for _ in range(5)]

# Позиция игрока
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 13


running = True



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    animation="peace"
    shift_x=0
    shift_y=0


    #move a player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x -= player_speed
        shift_x=shift_x-player_speed
        animation="run"
        x1_enemy-=player_speed
        x2_enemy-=player_speed
        last_direction = "right"
    if keys[pygame.K_a]:
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
    if keys[pygame.K_w]:
        y += player_speed
        shift_y=shift_y+player_speed
        animation="run"
        y1_enemy+=player_speed
        y2_enemy+=player_speed
    
    #backgraund
    screen.blit(level1, (x,y))


    # Отображение и обновление позиции врагов
    for enemy in enemies:
        enemy.update(player_x, player_y, shift_x, shift_y)
        enemy.draw()


    #animation
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
    if animation=="peace":
         if anim > 1:
              anim=0
        
    # Отображение игрока
    if keys[pygame.K_f]:
        
        if last_direction == "left":
            screen.blit(reverse_playerHit[anim//anim_divide], (player_x,player_y))
        else:
             screen.blit(playerHit[anim//anim_divide], (player_x,player_y))
    elif keys[pygame.K_w]:
        screen.blit(playerRun[anim//anim_divide], (player_x,player_y))  
    elif keys[pygame.K_a]:
        screen.blit(reverse_playerRun[anim//anim_divide], (player_x,player_y))    
    else:
        if last_direction == "left":
            screen.blit(reverse_playerRun[anim//anim_divide], (player_x,player_y))
        else:
             screen.blit(playerRun[anim//anim_divide], (player_x,player_y))

    
    pygame.display.flip()
    
    clock.tick(15)

pygame.quit()
sys.exit()
