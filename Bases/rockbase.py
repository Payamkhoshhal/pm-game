import pygame
import os

imgs = []
for x in range(5):
    x += 1
    add_str = str(x)
    
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/RockBase",  "rockbase_"+add_str +".png")),
        (256, 256)))

class RockBase:
    def __init__(self , x , y , w , h):
        self.rb_x = x # 600
        self.rb_y = y # 600
        self.width = w # 128
        self.height = h #128       
        self.rockbase_visible = True
        self.rockbase_clicked = False
        self.imgs = imgs
        self.animation_count = 0
        self.img = self.imgs[self.animation_count]
        self.frame_delay = 4
        self.current_delay = 0
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/RockBase",  "rockbase.png")),(256, 256))
        self.rect = self.img.get_rect(topleft=(self.rb_x , self.rb_y))

    def draw(self, win , cam_x , cam_y):
        
        self.rect = pygame.Rect(self.rb_x - cam_x, self.rb_y - cam_y, self.width, self.height)
        if self.rockbase_clicked:
            self.range = 100
            surface = pygame.Surface((self.range*4 , self.range*4), pygame.SRCALPHA, 32) 
            pygame.draw.ellipse(surface,(153, 102, 0 ,150),(0 , 0 , 300, 180))
            rotated_surface = pygame.transform.rotate(surface, - 20)  # Rotate by 30 degrees

            win.blit(rotated_surface,(self.rb_x - cam_x  - 210 , self.rb_y - cam_y  - 70))
       # if self.rockbase_visible:
       #     self.current_delay += 1
       #     if self.current_delay >= self.frame_delay:
       #         self.current_delay = 0
       #         self.animation_count += 1
       #         if self.animation_count >= len(self.imgs):
       #             self.animation_count = 0
       #     self.img = self.imgs[self.animation_count]
        win.blit(self.img ,(self.rb_x - cam_x   , self.rb_y - cam_y ))

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