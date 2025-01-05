import pygame
import os

imgs = []
for x in range(7):
    x += 1
    add_str = str(x)
    
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/mouse",  add_str +".png")),
        (50, 50)))

class Mouse:
    def __init__(self ):
        self.animation_count = 0
        self.imgs = imgs
        self.img = self.imgs[self.animation_count]
        self.frame_delay = 4
        self.current_delay = 0

    def draw(self, win , mouse_x , mouse_y):
        pygame.mouse.set_visible(False)
        self.range = 100
        surface = pygame.Surface((self.range*4 , self.range*4), pygame.SRCALPHA, 32) 
        pygame.draw.ellipse(surface,(0, 180 ,250,150),(0 ,  0 , 200, 120))
        rotated_surface = pygame.transform.rotate(surface , - 20)  # Rotate by 30 degrees
        win.blit(rotated_surface,(mouse_x  - 190 , mouse_y ))
        self.current_delay += 1
        if self.current_delay >= self.frame_delay:
            self.current_delay = 0
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0
        self.img = self.imgs[self.animation_count]
        win.blit(self.img, (mouse_x , mouse_y))
        
 