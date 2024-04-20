import pygame
import sys
import random
import math

pygame.init()
screen_width, screen_height = 800,600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


#music
background_song=pygame.mixer.Sound("music/backgraund.mp3")
background_song.play(-1)
stop_start=0

hit_sound=[
    pygame.mixer.Sound("music/hit1.mp3"),
    pygame.mixer.Sound("music/hit2.mp3")
]
number_sound=0
#coordinates
x=-50
y=-500
x1_enemy=873
x2_enemy=1400
y1_enemy=150
y2_enemy=600



#loading image
hearts=[
     pygame.transform.scale(pygame.image.load("image/hearts/xp0.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp1.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp2.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp3.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp4.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp5.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp6.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp7.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp8.png"), (150,30)),
     pygame.transform.scale(pygame.image.load("image/hearts/xp9.png"), (150,30)),
]

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
anim_heart=0
anim_last=1
anim_divide=1
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
enemies = [Enemy(random.randint(x1_enemy,x2_enemy), random.randint(y1_enemy,y2_enemy), 4) for _ in range(5)]

# Позиция игрока
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 13


running = True

mouse_button_down = False

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

    #screen
    screen.blit(hearts[0], (10,10))

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
    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("Удар!")
                if number_sound == 0:
                    hit_sound[0].play()
                    number_sound = 1
                else:
                    hit_sound[1].play()
                    number_sound = 0
                if last_direction == "left":
                    screen.blit(reverse_playerHit[anim // anim_divide], (player_x, player_y))
                else:
                    screen.blit(playerHit[anim // anim_divide], (player_x, player_y))
                # Переключение между анимациями удара и удара2
                if number_sound == 0:
                    if last_direction == "left":
                        screen.blit(reverse_playerHit[anim // anim_divide], (player_x, player_y))
                    else:
                        screen.blit(playerHit[anim // anim_divide], (player_x, player_y))

    elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_button_down = False

        
    elif keys[pygame.K_w]:
        if last_direction == "left":
            screen.blit(reverse_playerRun[anim//anim_divide], (player_x,player_y))
        else:
             screen.blit(playerRun[anim//anim_divide], (player_x,player_y))
    elif keys[pygame.K_a]:
        screen.blit(reverse_playerRun[anim//anim_divide], (player_x,player_y))    
    else:
        if last_direction == "left":
            screen.blit(reverse_playerRun[anim//anim_divide], (player_x,player_y))
        else:
             screen.blit(playerRun[anim//anim_divide], (player_x,player_y))
    if keys[pygame.K_t]:
        background_song.stop()
        stop_start=1
    if keys[pygame.K_y] and stop_start==1:
        background_song.play()
        stop_start=0
        


    pygame.display.flip()
    
    clock.tick(10)

pygame.quit()
sys.exit()