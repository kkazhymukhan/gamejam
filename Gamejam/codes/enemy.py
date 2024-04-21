import sys
import random
import math
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])

    # Метод для отображения врага
    def draw(self,screen,reverse_enemyRun, enemyRun, anim_divide, animEnemy):
        if self.direction == "right":
            screen.blit(reverse_enemyRun[animEnemy // anim_divide], (self.x, self.y))
        else:
            screen.blit(enemyRun[animEnemy // anim_divide], (self.x, self.y))

    # Метод для обновления позиции врага
    def update(self, player_x, player_y, shift_x, shift_y,x1_enemy,x2_enemy, y1_enemy, y2_enemy):
        print(self.x ,",", self.y, "----------", x1_enemy, ",", x2_enemy,"--", y1_enemy,",",y2_enemy)
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

