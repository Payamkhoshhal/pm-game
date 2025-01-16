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
        self.hb_menu_options = ['tree', 'rock_base']
        self.hb_menu_visible  = False

        # hm menu
        # tree icon
        self.tree_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu/home-base-icons",  "tree_icon.png")),(64, 64))
        self.tree_icon_y_target = 660
        self.tree_icon_speed = 8
        self.tree_icon_x = 100 
        self.tree_icon_y = 800        
        self.rect_tree_icon = pygame.Rect(self.tree_icon_x, self.tree_icon_y, 64, 64)
        self.tree_icon_disabled = self.tree_icon.copy()  # Make a copy for the disabled state

        # rockbase icon
        self.rb_icon = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/RockBase",  "rockbase.png")),(64 , 64))
        self.rb_icon_y_target = 660
        self.rb_icon_speed = 8
        self.rb_icon_x = 200
        self.rb_icon_y = 800        
        self.rect_rb_icon = pygame.Rect(self.rb_icon_x, self.rb_icon_y, 64, 64)
        self.rb_icon_disabled = self.rb_icon.copy()  # Make a copy for the disabled state

        # rect list of all items in the menu of home base
        self.item_rects = [self.rect_tree_icon , self.rect_rb_icon]

    def draw(self, win):
        if self.y >= self.target_y:
            self.y = self.y - self.show_menu_speed
        win.blit(self.menu_img, (self.x , self.y)) 

    def is_clicked(self, pos):
        #self.y = 800 # every time that the base got clicked the menu should disapear again
        #self.tree_icon_y = 800
        return self.rect.collidepoint(pos)

    def draw_hm_menu(self, win , is_tree_dragable ):
       if self.hb_menu_visible:             
            if self.tree_icon_y >= self.tree_icon_y_target:
                self.tree_icon_y = self.tree_icon_y - 8
            if self.rb_icon_y  >=  self.rb_icon_y_target:
                self.rb_icon_y = self.rb_icon_y - 8

            self.draw(win)
            win.blit(self.tree_icon, (self.tree_icon_x , self.tree_icon_y )) 
            win.blit(self.rb_icon,  (self.rb_icon_x , self.rb_icon_y))
            self.rect_tree_icon = pygame.Rect(self.tree_icon_x, self.tree_icon_y, 64, 64)
            self.rect_rb_icon = pygame.Rect(self.rb_icon_x, self.rb_icon_y, 64, 64)

            if not is_tree_dragable:
            # Create a semi-transparent overlay for the disabled state
                overlay = pygame.Surface(self.tree_icon.get_size(), pygame.SRCALPHA)
                overlay.fill((0, 0, 0, 128))  # 50% black transparency
                win.blit(overlay,(self.tree_icon_x , self.tree_icon_y ))

    def which_button_is_clicked(self, pos):
        tree_rect = pygame.Rect(self.rect_tree_icon.x  , self.rect_tree_icon.y , 64, 64)
        rb_rect = pygame.Rect(self.rect_rb_icon.x , self.rect_tree_icon.y, 64, 64)
        if tree_rect.collidepoint(pos):
            option = 'tree'
            print(option)
            return option
        elif rb_rect.collidepoint(pos):
            option = 'rb'
            print(option)
            return option
        return None
        



