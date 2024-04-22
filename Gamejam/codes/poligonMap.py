import pygame
import sys
import random
import math

pygame.init()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# music
pygame.mixer.music.load("music/backgraund.mp3")
pygame.mixer.music.play(-1)

# coordinates
x = -20
y = -400
x1_enemy = 923
x2_enemy = 1450
y1_enemy = 650
y2_enemy = 1200

# loading image
playerRun = [
    pygame.transform.scale(pygame.image.load("image/run/run1.png"), (90, 75)),
    pygame.transform.scale(pygame.image.load("image/run/run2.png"), (90, 75))
]

enemyRun = [
    pygame.transform.scale(pygame.image.load("image/enemy/enemy1.png"), (90, 75)),
    pygame.transform.scale(pygame.image.load("image/enemy/enemy2.png"), (90, 75))
]

playerHit = [
    pygame.transform.scale(pygame.image.load("image/hit/hit1.png"), (90, 75)),
    pygame.transform.scale(pygame.image.load("image/hit/hit2.png"), (90, 75))
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

# animation settings
animEnemy = 0
anim = 0
anim_last = 3
anim_divide = 2
enemyAnimation = "run"
last_direction = "right"

# Class for enemies
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])

    # Method to draw enemy
    def draw(self):
        if self.direction == "right":
            screen.blit(reverse_enemyRun[animEnemy // anim_divide], (self.x, self.y))
        else:
            screen.blit(enemyRun[animEnemy // anim_divide], (self.x, self.y))

    # Method to update enemy position
    def update(self, player_x, player_y, shift_x, shift_y):
        self.x = self.x + shift_x
        self.y = self.y + shift_y
        if self.is_player_visible(player_x, player_y):
            # Move towards player
            angle = math.atan2(player_y - self.y, player_x - self.x)
            self.x += self.speed * math.cos(angle)
            self.y += self.speed * math.sin(angle)
        else:
            # Move randomly
            if self.direction == "up":
                self.y -= self.speed
            elif self.direction == "down":
                self.y += self.speed
            elif self.direction == "left":
                self.x -= self.speed
            elif self.direction == "right":
                self.x += self.speed

            # Change direction upon reaching screen edge
            if self.x < x1_enemy or self.x > x2_enemy or self.y < y1_enemy or self.y > y2_enemy:
                self.direction = random.choice(["up", "down", "left", "right"])

    # Method to determine player visibility
    def is_player_visible(self, player_x, player_y):
        distance = math.sqrt((player_x - self.x) ** 2 + (player_y - self.y) ** 2)
        return distance < 200  # Visibility distance

# Create enemies
enemies = [Enemy(random.randint(923, 1500), random.randint(650, 1250), 4) for _ in range(5)]

# Player position
player_x, player_y = screen_width // 2, screen_height // 2
player_speed = 13

running = True

# Function to draw semi-transparent polygon
def draw_semi_transparent_polygon(surface, color, points, alpha):
    temp_surface = surface.copy()
    temp_surface.set_alpha(alpha)
    pygame.draw.polygon(temp_surface, color, points)
    surface.blit(temp_surface, (0, 0))

# Function to check if a point is inside a polygon
def is_point_inside_polygon(x, y, polygon_points):
    n = len(polygon_points)
    inside = False
    p1x, p1y = polygon_points[0]
    for i in range(n+1):
        p2x, p2y = polygon_points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    animation = "peace"
    shift_x = 0
    shift_y = 0

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if is_point_inside_polygon(player_x + player_speed, player_y, [(240 + x, 610 + y), (678 + x, 610 + y), (678 + x, 1070 + y), (240 + x, 1070 + y)]):
            x -= player_speed
            shift_x = shift_x - player_speed
            animation = "run"
            x1_enemy -= player_speed
            x2_enemy -= player_speed
            last_direction = "right"
    if keys[pygame.K_a]:
        if is_point_inside_polygon(player_x - player_speed, player_y, [(240 + x, 610 + y), (678 + x, 610 + y), (678 + x, 1070 + y), (240 + x, 1070 + y)]):
            x += player_speed
            shift_x = shift_x + player_speed
            animation = "run"
            x1_enemy += player_speed
            x2_enemy += player_speed
            last_direction = "left"
    if keys[pygame.K_s]:
        if is_point_inside_polygon(player_x, player_y + player_speed, [(240 + x, 610 + y), (678 + x, 610 + y), (678 + x, 1070 + y), (240 + x, 1070 + y)]):
            y -= player_speed
            shift_y = shift_y - player_speed
            animation = "run"
            y1_enemy -= player_speed
            y2_enemy -= player_speed
    if keys[pygame.K_w]:
        if is_point_inside_polygon(player_x, player_y - player_speed, [(240 + x, 610 + y), (678 + x, 610 + y), (678 + x, 1070 + y), (240 + x, 1070 + y)]):
            y += player_speed
            shift_y = shift_y + player_speed
            animation = "run"
            y1_enemy += player_speed
            y2_enemy += player_speed

    # Draw semi-transparent polygon on the background
    level1_copy = level1.copy()
    draw_semi_transparent_polygon(level1_copy, (100, 100, 100), [(240, 610), (678, 610), (678, 1070), (240, 1070), (00, 500)], 200)
    screen.blit(level1_copy, (x, y))

    # Display and update enemy positions
    for enemy in enemies:
        enemy.update(player_x, player_y, shift_x, shift_y)
        enemy.draw()

    # Animation
    if enemyAnimation == "run":
        if animEnemy == anim_last:
            animEnemy = 0
        else:
            animEnemy += 1
    if animation == "hit":
        if anim == anim_last:
            anim = 0
        else:
            anim += 1
    elif animation == "run":
        if anim == anim_last:
            anim = 0
        else:
            anim += 1
    if animation == "peace":
        if anim > 1:
            anim = 0

    # Display player
    if keys[pygame.K_f]:
        if last_direction == "left":
            screen.blit(reverse_playerHit[anim // anim_divide], (player_x, player_y))
        else:
            screen.blit(playerHit[anim // anim_divide], (player_x, player_y))
    elif keys[pygame.K_w]:
        screen.blit(playerRun[anim // anim_divide], (player_x, player_y))
    elif keys[pygame.K_a]:
        screen.blit(reverse_playerRun[anim // anim_divide], (player_x, player_y))
    else:
        if last_direction == "left":
            screen.blit(reverse_playerRun[anim // anim_divide], (player_x, player_y))
        else:
            screen.blit(playerRun[anim // anim_divide], (player_x, player_y))

    pygame.display.flip()
    clock.tick(15)

pygame.quit()
sys.exit()
