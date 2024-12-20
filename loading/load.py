
import pygame
import os

imgs = []
for x in range(6):
    x += 1
    add_str = str(x)
    
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/loading",  "loading"+add_str +".png")),
        (350, 350)))

class Loading:

    def __init__(self):
        self.animation_count = 0
        self.imgs = imgs
        self.img = self.imgs[self.animation_count]
        self.frame_delay = 15  # Frames to wait before changing image
        self.current_delay = 0

    def draw(self, win , cam_x , cam_y, x , y, load_time):
        self.current_delay += 1
        if self.current_delay >= self.frame_delay:
            self.current_delay = 0
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0
        self.img = self.imgs[self.animation_count]
        win.blit(self.img, (x - cam_x - 60 , y - cam_y - 70))
        
        