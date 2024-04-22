import pygame


class Poligon:
    def draw(self, screen):
        
        poligon1 = pygame.Rect(250, 605, 440, 467)
        pygame.draw.rect(screen, (255, 0, 0), poligon1)
        
        poligon2 = pygame.Rect(670, 855, 270, 130)
        pygame.draw.rect(screen, (255, 255, 0), poligon2)
        
        poligon3 = pygame.Rect(930, 660, 565, 545)
        pygame.draw.rect(screen, (255, 0, 255), poligon3)
        
        poligon4 = pygame.Rect(1490, 735, 240, 100)
        pygame.draw.rect(screen, (0, 255, 0), poligon4)
        
        poligon5 = pygame.Rect(1720, 370, 410, 710)
        pygame.draw.rect(screen, (0, 0, 255), poligon5)
        
        poligon6 = pygame.Rect(1870, 1060, 115, 420)
        pygame.draw.rect(screen, (0, 255, 255), poligon6)
        
        poligon7 = pygame.Rect(1480, 1455, 505, 345)
        pygame.draw.rect(screen, (255, 255, 255), poligon7)
        
        poligon8 = pygame.Rect(920, 1670, 570, 130)
        pygame.draw.rect(screen, (0, 0, 0), poligon8)
        
        # Сохраняем прямоугольники в список
        self.poligans = [poligon1, poligon2, poligon3, poligon4, poligon5, poligon6, poligon7, poligon8]

    def is_inside_polygons(self, x, y):
        for rect in self.poligans:
            if rect.collidepoint((-1)*x+450, (-1)*y+360):
                print("ddoodoododdo")
                return True
        return False
