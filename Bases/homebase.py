import pygame
import os


class HomeBase:
    def __init__(self ):
        self.x =  400
        self.y =  400
        self.width =  128
        self.height =  128       
        #self.menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","MenuBar.png")),(950,170))
        self.base_home = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/buildings","base-home.png")),(100,100)) 
        self.options = ['Add tree' , 'Add nothing' , 'nothing'] 
        #self.visible = False 
        self.homebase_visible = True 
        self.homebase_clicked = False

    def draw(self, win , cam_x , cam_y):
        
        self.rect = pygame.Rect(self.x - cam_x, self.y - cam_y, self.width, self.height)
        if self.homebase_clicked:
            self.range = 100
            surface = pygame.Surface((self.range*4 , self.range*4), pygame.SRCALPHA, 32) 
            pygame.draw.ellipse(surface,(153, 102, 0 ,150),(0 , 0 , 300, 180))
            rotated_surface = pygame.transform.rotate(surface, - 20)  # Rotate by 30 degrees

            win.blit(rotated_surface,(self.x - cam_x  - 210 , self.y - cam_y  - 70))
        if self.homebase_visible:
            #win.blit(self.menu_img, (self.x , self.y)) 
            win.blit(self.base_home,(self.x -cam_x , self.y -cam_y))

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