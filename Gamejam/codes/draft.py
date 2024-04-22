import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Движение круга в сложной области")

# Создание поверхности для фона
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(WHITE)

# Размеры круга
CIRCLE_RADIUS = 20

# Скорость перемещения круга
SPEED = 2

# Вершины сложной фигуры
polygon_rectangles = [
    pygame.Rect(200, 100, 200, 200),  # прямоугольник без выступов
    pygame.Rect(400, 300, 200, 200),  # прямоугольник без выступов
    pygame.Rect(600, 100, 200, 200),  # прямоугольник без выступов
    pygame.Rect(200, 200, 100, 100),  # выступ
    pygame.Rect(600, 300, 100, 100)   # выступ
]

# Функция для отрисовки круга
def draw_circle(surface, color, x, y, radius):
    pygame.draw.circle(surface, color, (x, y), radius)

# Функция для отрисовки сложной фигуры
def draw_polygon(surface, color, rectangles):
    for rect in rectangles:
        pygame.draw.rect(surface, color, rect)

# Главная функция игры
def main():
    # Позиция круга
    circle_x = SCREEN_WIDTH // 2
    circle_y = SCREEN_HEIGHT // 2

    # Позиция камеры
    camera_x = 0
    camera_y = 0

    # Основной цикл игры
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Движение круга с помощью клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and circle_x > CIRCLE_RADIUS and is_inside_polygons(circle_x - SPEED, circle_y):
            circle_x -= SPEED
        if keys[pygame.K_RIGHT] and circle_x < SCREEN_WIDTH - CIRCLE_RADIUS and is_inside_polygons(circle_x + SPEED, circle_y):
            circle_x += SPEED
        if keys[pygame.K_UP] and circle_y > CIRCLE_RADIUS and is_inside_polygons(circle_x, circle_y - SPEED):
            circle_y -= SPEED
        if keys[pygame.K_DOWN] and circle_y < SCREEN_HEIGHT - CIRCLE_RADIUS and is_inside_polygons(circle_x, circle_y + SPEED):
            circle_y += SPEED

        # Перемещение камеры за кругом
        camera_x = circle_x - SCREEN_WIDTH // 2
        camera_y = circle_y - SCREEN_HEIGHT // 2

        # Отрисовка фона
        background.fill(WHITE)

        # Отрисовка сложной фигуры
        draw_polygon(background, BLUE, [(rect.left - camera_x, rect.top - camera_y, rect.width, rect.height) for rect in polygon_rectangles])

        # Отрисовка круга
        draw_circle(background, RED, circle_x - camera_x, circle_y - camera_y, CIRCLE_RADIUS)

        # Обновление экрана
        screen.blit(background, (0, 0))
        pygame.display.flip()

# Функция для проверки принадлежности точки сложным фигурам
def is_inside_polygons(x, y):
    for rect in polygon_rectangles:
        if rect.collidepoint(x, y):
            return True
    return False

# Запуск игры
if __name__ == "__main__":
    main()
