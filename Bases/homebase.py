import pygame
import os


class HomeBase:
    def __init__(self ):
        self.x =  60
        self.y =  620
        self.width = 128
        self.height = 128       
        #self.menu_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/menu","MenuBar.png")),(950,170))
        self.base_home = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/buildings","base-home.png")),(100,100)) 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.options = ['Add tree' , 'Add nothing' , 'nothing'] 
        #self.visible = False 
        self.homebase_visible = True 

    def draw(self, win):
        #if not self.visible:
        #    return
        #pygame.draw.rect(screen, (200, 200, 200), self.rect)
        #font = pygame.font.Font(None, 36)
        #if self.options:
        #    for i, option in enumerate(self.options):
        #        option_text = font.render(option, True, (0, 0, 0))
        #        screen.blit(option_text, (self.rect.x + 10, self.rect.y + 10 + i * 40))
        if self.homebase_visible:
            #win.blit(self.menu_img, (self.x , self.y)) 
            win.blit(self.base_home,(400-cam_x , 400-cam_y))

    def is_clicked(self, pos):
        print('Home base is clicked')
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