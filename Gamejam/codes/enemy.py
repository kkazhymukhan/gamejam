import pygame
import sys
import random
import math

pygame.init()
x=0
y=0
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
playerRun= [
       pygame.transform.scale(pygame.image.load("image/run/run1.png"), (60,60)),
       pygame.transform.scale(pygame.image.load("image/run/run2.png"), (60,60))
]


playerHit= [
       pygame.transform.scale(pygame.image.load("image/hit/hit1.png"), (60,60)),
       pygame.transform.scale(pygame.image.load("image/hit/hit2.png"), (60,60))
]

level1_image=pygame.image.load("image/level1.png")
level1=pygame.transform.scale(level1_image, (2400,2400))

anim=0
# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Класс для врагов
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])

    # Метод для отображения врага
    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, self.y), 10)

    # Метод для обновления позиции врага
    def update(self, player_x, player_y):
        if self.is_player_visible(player_y, player_x):
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
            if self.x < 0 or self.x > 2400 or self.y < 0 or self.y > 2400:
                self.direction = random.choice(["up", "down", "left", "right"])

    # Метод для определения видимости игрока
    def is_player_visible(self, player_x, player_y):
        distance = math.sqrt((player_x - self.x) ** 2 + (player_y - self.y) ** 2)
        return distance < 200  # Расстояние видимости

# Создание врагов
enemies = [Enemy(random.randint(50, screen_width - 50), random.randint(50, screen_height - 50), 2) for _ in range(5)]

# Позиция игрока
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 5

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #move a player
    animation="peace"
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x -= player_speed
        animation="run"
    if keys[pygame.K_a]:
        x += player_speed
        animation="run"
    if keys[pygame.K_s]:
        y -= player_speed
        animation="run"
    if keys[pygame.K_w]:
        y += player_speed
        animation="run"

    
    screen.blit(level1, (x,y))

    # Отображение и обновление позиции врагов
    for enemy in enemies:
        enemy.update(player_x, player_y)
        enemy.draw()
    #animation
    if animation=="hit":
                if anim==1:
                    anim=0
                else:
                    anim +=1
    elif animation=="run":
               if anim==1:
                    anim=0
               else:
                    anim +=1
    
        
    # Отображение игрока
    if keys[pygame.K_f]:
        screen.blit(playerHit[anim], (player_x,player_y))
    elif keys[pygame.K_w]:
        screen.blit(playerRun[anim], (player_x,player_y))    
    else:
        screen.blit(playerRun[anim], (player_x,player_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()