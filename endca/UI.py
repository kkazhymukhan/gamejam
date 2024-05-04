import pygame


class cutscen:
     
     def __init__(self,cutscene_bool):
         self.cutscene_frame=0
         self.font3=pygame.font.Font("Pokemon GB.ttf", 17)
         self.font1=pygame.font.Font("Pokemon GB.ttf", 32)
         self.font2=pygame.font.Font("Pokemon GB.ttf", 64)
         self.font1_move=600
         self.cutscene_bool=cutscene_bool
     def scene(self,screen,cutscene):
        self.cutscene_frame += 1
        if self.cutscene_frame%3==0 and self.cutscene_frame%2!=0 and self.cutscene_frame<100:
            screen.blit(cutscene[0], (0, 0))
            text1 = self.font1.render('Attention! Floods have begun across the country, and the cause is unknown.', 1, (0, 0, 0))
            screen.blit(text1, (self.font1_move, 550))
            self.font1_move-=60
        elif self.cutscene_frame%6==0 and self.cutscene_frame<100:
            screen.blit(cutscene[1], (0, 0))
            text1 = self.font1.render('Attention! Floods have begun across the country, and the cause is unknown.', 1, (0, 0, 0))
            screen.blit(text1, (self.font1_move, 550))
            self.font1_move-=60
        if self.cutscene_frame>100:
            screen.blit(cutscene[2], (0, 0))
        if self.cutscene_frame>103 :
            screen.blit(cutscene[3], (0, 0))
        if self.cutscene_frame>106:
            screen.blit(cutscene[4], (0, 0))
            text1 = self.font2.render('WHAT?', 4, (0, 0, 0))
            screen.blit(text1, (480, 520))
        if self.cutscene_frame>118 :
            screen.blit(cutscene[5], (0, 0))
            text1 = self.font2.render('WHAT?', 4, (0, 0, 0))
            screen.blit(text1, (480, 520))
        if self.cutscene_frame>121:
            screen.blit(cutscene[6], (0, 0))
            text1 = self.font2.render('WHAT?', 4, (0, 0, 0))
            screen.blit(text1, (480, 520))
        if self.cutscene_frame>124:
            screen.blit(cutscene[7], (0, 0))
            text1 = self.font2.render('WHAT?', 4, (0, 0, 0))
            screen.blit(text1, (480, 520))
        if self.cutscene_frame>127 :
            screen.blit(cutscene[8], (0, 0))
        if self.cutscene_frame>130 :
            screen.blit(cutscene[9], (0, 0))
        if self.cutscene_frame>133 :
            screen.blit(cutscene[10], (0, 0))
        if self.cutscene_frame>136 :
            screen.blit(cutscene[11], (0, 0))
        if self.cutscene_frame>137 :
            screen.blit(cutscene[12], (0, 0))
        if self.cutscene_frame>140 and self.cutscene_frame<155:
            screen.blit(cutscene[13], (0, 0))
            text1 = self.font3.render('WHAT IS THAT?', 4, (0, 0, 0))
            screen.blit(text1, (220, 150))
        if self.cutscene_frame>155:
            self.cutscene_frame=0
            self.font1_move=600
        return self.cutscene_bool

class Button:
    anim=0
    def Menu(self, screen):
            self.anim_last=9
            self.anim_divide=5
            UI_image =[
            pygame.transform.scale(pygame.image.load("image/UI/UI_play_1.png"), (800, 600)),
            pygame.transform.scale(pygame.image.load("image/UI/UI_play_2.png"), (800, 600))
            ]
            #print(self.anim)
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



