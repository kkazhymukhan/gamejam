import pygame

class Button:
    anim=0
    def Menu(self, screen):
            self.anim_last=9
            self.anim_divide=5
            UI_image =[
            pygame.transform.scale(pygame.image.load("image/UI/UI_play_1.png"), (800, 600)),
            pygame.transform.scale(pygame.image.load("image/UI/UI_play_2.png"), (800, 600))
            ]
            print(self.anim)
            if self.anim ==self.anim_last:
                self.anim=0
            else:
                self.anim+=1
            screen.blit(UI_image[self.anim//self.anim_divide], (0, 0))
    def __init__(self, visible):
        self.visible = visible
        self.rect = pygame.Rect(270, 195, 260, 90)  # Пример прямоугольной области для кнопки
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.visible = False
                pygame.display.flip()  # Обновляем экран после изменения видимости

class Lose:
    anim=0
    restart_clicked=True
    def Menu(self, screen):
            
            lose_image =pygame.transform.scale(pygame.image.load("image/UI/lose.png"), (800, 600))
            losebutton_image =pygame.transform.scale(pygame.image.load("image/UI/losebutton.png"), (288, 72))
            
            screen.blit(lose_image, (0, 0))
            screen.blit(losebutton_image, (260, 300))
    def __init__(self, visible):
        self.visible = visible
        self.rect = pygame.Rect(260, 300, 260, 90)  # Пример прямоугольной области для кнопки
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.restart_clicked = False
                pygame.display.flip()  # Обновляем экран после изменения видимости

