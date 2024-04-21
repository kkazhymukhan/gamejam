import pygame
import sys
import random
import math

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
x1_enemy = 873
x2_enemy = 1400
y1_enemy = 150
y2_enemy = 600

# Загрузка изображений
hearts = [
    pygame.transform.scale(pygame.image.load("image/hearts/xpfull.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp1.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp2.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp3.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp4.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp5.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp6.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp7.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp8.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp9.png"), (320, 60)),
    pygame.transform.scale(pygame.image.load("image/hearts/xp10.png"), (320, 60)),
]

playerRun = [
    pygame.transform.scale(pygame.image.load("image/run/run1.png"), (100, 80)),
    pygame.transform.scale(pygame.image.load("image/run/run2.png"), (100, 80))
]

enemyRun = [
    pygame.transform.scale(pygame.image.load("image/enemy/enemy1.png"), (90, 85)),
    pygame.transform.scale(pygame.image.load("image/enemy/enemy2.png"), (90, 85))
]

playerHit = [
    pygame.transform.scale(pygame.image.load("image/hit/hit1.png"), (100, 80)),
    pygame.transform.scale(pygame.image.load("image/hit/hit2.png"), (100, 80))
]

reverse_playerRun = [
    pygame.transform.flip(playerRun[0], True, False),
    pygame.transform.flip(playerRun[1], True, False)
]

reverse_playerHit = [
    pygame.transform.flip(playerHit[0], True, False),
    pygame.transform.flip(playerHit[1], True, False)
]

reverse_enemyRun = [
    pygame.transform.flip(enemyRun[0], True, False),
    pygame.transform.flip(enemyRun[1], True, False)
]

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
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])

    # Метод для отображения врага
    def draw(self):
        if self.direction == "right":
            screen.blit(enemyRun[animEnemy // anim_divide], (self.x, self.y))
        else:
            screen.blit(reverse_enemyRun[animEnemy // anim_divide], (self.x, self.y))

    # Метод для обновления позиции врага
    def update(self, player_x, player_y, shift_x, shift_y):
        self.x = self.x + shift_x
        self.y = self.y + shift_y
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
    if keys[pygame.K_d]:
        x -= player_speed
        shift_x = -player_speed
        last_direction = "right"
    elif keys[pygame.K_a]:
        x += player_speed
        shift_x = player_speed
        last_direction = "left"
    else:
        shift_x = 0

    if keys[pygame.K_s]:
        y -= player_speed
        shift_y = -player_speed
    elif keys[pygame.K_w]:
        y += player_speed
        shift_y = player_speed
    else:
        shift_y = 0

    # Отображение фона
    screen.blit(level1, (x, y))

    # Отображение сердец
    screen.blit(hearts[0], (10, 10))

        # отображение и обновление позиции врагов, анимация бега
    for enemy in enemies:
        enemy.update(player_x, player_y, shift_x, shift_y)
        enemy.draw()
        animEnemy = (animEnemy + 1) % (len(enemyRun) * anim_divide)  # Обновление переменной для анимации врагов



    # Анимация удара
    if hit_animation:
        if last_direction == "left":
            screen.blit(reverse_playerHit[anim // anim_divide], (player_x, player_y))
        else:
            screen.blit(playerHit[anim // anim_divide], (player_x, player_y))
        if anim == anim_last:
            anim = 0
        else:
            anim += 1
    else:
        # Анимация бега только при движении
        if shift_x != 0 or shift_y != 0:
            if last_direction == "left":
                screen.blit(reverse_playerRun[anim // anim_divide], (player_x, player_y))
            else:
                screen.blit(playerRun[anim // anim_divide], (player_x, player_y))
            if anim == anim_last:
                anim = 0
            else:
                anim += 1
        else:
            # Отображение стоящего персонажа
            if last_direction == "left":
                screen.blit(reverse_playerRun[0], (player_x, player_y))
            else:
                screen.blit(playerRun[0], (player_x, player_y))

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
