import pygame
import os
import time 
from loading.load import Loading  
from properties.properties import ShowLevel, render_text_with_stroke  as rtws


# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

imgs = []
for x in range(2):
    x += 1
    add_str = str(x)
    
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/trees",  'tree_'+ add_str +".png")),
        (128, 128)))


class Tree:
    def __init__(self, x, y, width, height):
        #self.rect = pygame.Rect(x, y, width, height)
       
        #self.img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/trees/tree_1.png")),(200, 200))
        self.imgs = imgs
        self.img = self.imgs[0]
        self.tree_x = x
        self.tree_y = y
        self.tree_clicked = False
        self.rect = self.img.get_rect(topleft=(self.tree_x , self.tree_y))
        self.level = 0 
        self.upgrade_times = [15 , 120 , 300]
        self.is_updating = True # first time that we call this class we will wait for 15 sec
        self.tree_updating = Loading()
        self.upgrade_start_time = time.time()
        self.showlevel = ShowLevel()
        self.wood_collect_start_time = time.time()
        self.wood_collect = 0

    def draw(self, win ,camera_x , camera_y):

        if not self.is_updating:

            if self.tree_clicked == True:
                self.range = 100
                surface = pygame.Surface((self.range*4 , self.range*4), pygame.SRCALPHA, 32) 
                pygame.draw.ellipse(surface,(0,255,0,100),(0 ,  0 , 200, 120))
                rotated_surface = pygame.transform.rotate(surface, - 20)  
                self.showlevel.draw(win, camera_x , camera_y , self.tree_x , self.tree_y , self.level)
                win.blit(rotated_surface,(self.tree_x - camera_x  - 150 , self.tree_y - camera_y ))

            self.rect = self.img.get_rect(topleft=(self.tree_x - camera_x , self.tree_y - camera_y))
            win.blit(self.img ,(self.tree_x - camera_x , self.tree_y - camera_y))
        else:
            self.tree_updating.draw(win, camera_x , camera_y, self.tree_x - 20 , self.tree_y - 20 , self.upgrade_times[self.level] )
            # loaing timer
            font = pygame.font.Font(None, 34)
            remaining_time = self.upgrade_times[self.level] - (time.time() - self.upgrade_start_time) 

            text_surface = rtws(time.strftime("%Hh %Mm %Ss", time.gmtime(remaining_time)), font, (210, 140, 70), (0, 0, 0))
            
            win.blit(text_surface, (self.tree_x - camera_x - 40 , self.tree_y - camera_y + 100  ))

            self.update()

        # Display the tree level above the tree
        #font = pygame.font.Font(None, 36)
        #level_text = font.render(f"Level: {self.level}", True, (0, 0, 0))
        #win.blit(level_text, (self.tree_x + 20 , self.tree_y - 30))

    def calculate_woodlog_score(self):
        elapsed_time = time.time() - self.wood_collect_start_time
        if elapsed_time > 5:
            r =  elapsed_time / 5
            self.wood_collect_start_time = time.time()
            self.wood_collect =  self.level * round(r)
            return self.wood_collect
        return 0
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    
    def start_upgrade(self):
        """Start the upgrade process if not already upgrading and levels are available."""
        if not self.is_updating : #and self.level < len(self.images) - 1:
            self.is_updating = True 
            self.upgrade_start_time = time.time()
            print(f"Upgrade from level {self.level} started!")

    def complete_upgrade(self):
        """Complete the upgrade if enough time has passed."""
        if self.is_updating and self.upgrade_start_time:
            elapsed_time = time.time() - self.upgrade_start_time
            required_time = self.upgrade_times[self.level]
            if elapsed_time >= required_time:
                self.level += 1
                #self.img = self.imgs[self.level]
                self.is_updating = False
                self.upgrade_start_time = None
                print(f"Upgrade to level {self.level} complete!")

    def update(self):
        """Check if the upgrade can be completed."""
        #if self.is_updating:
        #    self.complete_upgrade()
        """Complete the upgrade if enough time has passed."""
        if self.is_updating and self.upgrade_start_time:
            update_elapsed_time = time.time() - self.upgrade_start_time
            required_time = self.upgrade_times[self.level]
            if update_elapsed_time >= required_time:
                self.level += 1
                #self.img = self.imgs[self.level]
                self.is_updating = False
                self.upgrade_start_time = None
                print(f"Upgrade to level {self.level} complete!")
    
    