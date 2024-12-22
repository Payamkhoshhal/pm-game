import pygame
import os

class Menu:
    def __init__(self ):
        self.x =  -10
        self.y =  800
        self.width = 128
        self.height = 128       
        self.menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","MenuBar.png")),(1030,170))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.show_menu_speed = 10 
        self.target_y = 630

        # hm menu
        self.tree_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/trees",  "tree_1.png")),(64, 64))
        self.hb_menu_visible  = False
        self.tree_icon_y_target = 650
        self.tree_icon_speed = 8
        self.tree_icon_x = 100 
        self.tree_icon_y = 800

    def draw(self, win):
        if self.y >= self.target_y:
            self.y = self.y - self.show_menu_speed
        win.blit(self.menu_img, (self.x , self.y)) 

    def is_clicked(self, pos):
        self.y = 800 # every time that the base got clicked the menu should disapear again
        self.tree_icon_y = 800
        return self.rect.collidepoint(pos)

    def draw_hm_menu(self, win):
       if self.hb_menu_visible:             
            if self.tree_icon_y >= self.tree_icon_y_target:
                self.tree_icon_y = self.tree_icon_y - 8
            self.draw(win)
            win.blit(self.tree_icon, (self.tree_icon_x , self.tree_icon_y )) 

    #def which_button_is_clicked(self, pos):
    #    for i, option in enumerate(self.options):
    #        option_rect = pygame.Rect(self.rect.x, self.rect.y + i * 40, self.rect.width, 40)
    #        if option_rect.collidepoint(pos):
    #            print(option)
    #            return option
    #    return None




