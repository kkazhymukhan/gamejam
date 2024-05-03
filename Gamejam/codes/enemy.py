
import random
import math
import time 
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = random.choice(["up", "down", "left", "right"])
        self.hit_count=0
        self.last_direction_change_time = time.time()


    # Метод для отображения врага
    def draw(self,screen,reverse_enemyRun, enemyRun, anim_divide, animEnemy):
        if self.direction == "right":
            screen.blit(reverse_enemyRun[animEnemy // anim_divide], (self.x, self.y))
        else:
            screen.blit(enemyRun[animEnemy // anim_divide], (self.x, self.y))

    # Метод для обновления позиции врага
    def update(self, index, player_x, player_y, shift_x, shift_y,x1_enemy,x2_enemy, y1_enemy, y2_enemy,x1_enemy1,x2_enemy1,y1_enemy1,y2_enemy1, x1_enemy2, x2_enemy2, y1_enemy2, y2_enemy2):
        #print(self.x ,",", self.y, "----------", x1_enemy, ",", x2_enemy,"--", y1_enemy,",",y2_enemy)
        current_time = time.time()  # Получаем текущее время
        time_since_last_change = current_time - self.last_direction_change_time
        
        self.x = self.x + shift_x
        self.y = self.y + shift_y
        if index<8:
            if self.is_player_visible(player_x, player_y) and (player_x > x1_enemy and player_x < x2_enemy and player_y > y1_enemy and player_y < y2_enemy):
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
            if index<8:
                if self.x < x1_enemy or self.x > x2_enemy or self.y < y1_enemy or self.y > y2_enemy:
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"

                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            if index>7 and index<17:
                if self.x < x1_enemy1 or self.x > x2_enemy1 or self.y < y1_enemy1 or self.y > y2_enemy1 :
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"
                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            if index>16:
                if (self.x < x1_enemy2 or self.x > x2_enemy2 or self.y < y1_enemy2 or self.y > y2_enemy2) :
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"

                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
        
        elif index>7 and index< 17:
            if self.is_player_visible(player_x, player_y) and (player_x > x1_enemy1 and player_x < x2_enemy1 and player_y > y1_enemy1 and player_y < y2_enemy1):
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
            if index<8:
                if self.x < x1_enemy or self.x > x2_enemy or self.y < y1_enemy or self.y > y2_enemy:
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"

                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            if index>7 and index<17:
                if self.x < x1_enemy1 or self.x > x2_enemy1 or self.y < y1_enemy1 or self.y > y2_enemy1 :
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"
                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            if index>16:
                if (self.x < x1_enemy2 or self.x > x2_enemy2 or self.y < y1_enemy2 or self.y > y2_enemy2) :
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"

                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
        
        elif index>16:
            if self.is_player_visible(player_x, player_y) and (player_x > x1_enemy2 and player_x < x2_enemy2 and player_y > y1_enemy2 and player_y < y2_enemy2):
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
            if index<8:
                if self.x < x1_enemy or self.x > x2_enemy or self.y < y1_enemy or self.y > y2_enemy:
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"

                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            if index>7 and index<17:
                if self.x < x1_enemy1 or self.x > x2_enemy1 or self.y < y1_enemy1 or self.y > y2_enemy1 :
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"
                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            if index>16:
                if (self.x < x1_enemy2 or self.x > x2_enemy2 or self.y < y1_enemy2 or self.y > y2_enemy2) :
                    if self.direction == "up":
                       self.direction="down"
                    elif self.direction == "down":
                        self.direction="up"
                    elif self.direction == "left":
                        self.direction="right"
                    elif self.direction == "right":
                        self.direction = "left"

                if time_since_last_change >= 5:
                    self.direction = random.choice(["up", "down", "left", "right"])
                    self.last_direction_change_time = current_time
            
    # Метод для определения видимости игрока
    def is_player_visible(self, player_x, player_y):
        distance = math.sqrt((player_x - self.x) ** 2 + (player_y - self.y) ** 2)
        return distance < 200  # Расстояние видимости

