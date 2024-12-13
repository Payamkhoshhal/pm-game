import pygame
import os

class Menu:
    def __init__(self ):
        self.x =  60
        self.y =  620
        self.width = 128
        self.height = 128       
        self.menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","menu.png")),(128,128))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.options = ['Add tree' , 'Add nothing' , 'nothing'] 
        #self.visible = False 
        self.menu_visible = False

    def draw(self, win):
        #if not self.visible:
        #    return
        #pygame.draw.rect(screen, (200, 200, 200), self.rect)
        #font = pygame.font.Font(None, 36)
        #if self.options:
        #    for i, option in enumerate(self.options):
        #        option_text = font.render(option, True, (0, 0, 0))
        #        screen.blit(option_text, (self.rect.x + 10, self.rect.y + 10 + i * 40))
        if self.menu_visible:
            win.blit(self.menu_img, (self.x , self.y)) 

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
        #if not self.visible:
        #    return None
    def which_button_is_clicked(self, pos):
        for i, option in enumerate(self.options):
            option_rect = pygame.Rect(self.rect.x, self.rect.y + i * 40, self.rect.width, 40)
            if option_rect.collidepoint(pos):
                print(option)
                return option
        return None



class MainMenu:
    def __init__(self):
        self.x = 10
        self.y = 750
        self.rect = pygame.Rect(self.x, self.y, 45 , 45)
        self.main_menu_visible = True
        self.main_menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","main-menu.png")),(45,45))

    def draw(self, win):
        if self.main_menu_visible:
            win.blit(self.main_menu_img, (self.x , self.y)) 

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)