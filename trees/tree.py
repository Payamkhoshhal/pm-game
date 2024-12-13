import pygame
import os
import time 
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
    def __init__(self, x, y, width, height, upgrade_times):
        #self.rect = pygame.Rect(x, y, width, height)
        self.level = 0
        #self.img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/trees/tree_1.png")),(200, 200))
        self.imgs = imgs
        self.img = self.imgs[0]
        self.tree_x = x
        self.tree_y = y
        self.level = 0 
        self.state = 'normal'
        self.upgrade_times = upgrade_times
        self.upgrade_start_time = None
        self.tree_clicked = False

    def draw(self, win ,camera_x , camera_y):
        
        if self.tree_clicked == True:
            self.range = 100
            surface = pygame.Surface((self.range*4 , self.range*4), pygame.SRCALPHA, 32) 
            pygame.draw.ellipse(surface,(0,255,0,100),(0 ,  0 , 200, 120))
            rotated_surface = pygame.transform.rotate(surface, - 20)  
            win.blit(rotated_surface,(self.tree_x - camera_x  - 150 , self.tree_y - camera_y ))

        self.rect = self.img.get_rect(topleft=(self.tree_x - camera_x , self.tree_y - camera_y))
        # Draw the tree as a rectangle
        win.blit(self.img ,(self.tree_x - camera_x , self.tree_y - camera_y))

        # Display the tree level above the tree
        #font = pygame.font.Font(None, 36)
        #level_text = font.render(f"Level: {self.level}", True, (0, 0, 0))
        #win.blit(level_text, (self.tree_x + 20 , self.tree_y - 30))

        self.update()
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    
    def start_upgrade(self):
        """Start the upgrade process if not already upgrading and levels are available."""
        if self.state == "normal" : #and self.level < len(self.images) - 1:
            self.state = "updating"
            self.upgrade_start_time = time.time()
            print(f"Upgrade from level {self.level} started!")

    def complete_upgrade(self):
        """Complete the upgrade if enough time has passed."""
        if self.state == "updating" and self.upgrade_start_time:
            elapsed_time = time.time() - self.upgrade_start_time
            required_time = self.upgrade_times[self.level]
            if elapsed_time >= required_time:
                self.level += 1
                self.img = self.imgs[self.level]
                self.state = "normal"
                self.upgrade_start_time = None
                print(f"Upgrade to level {self.level} complete!")

    def update(self):
        """Check if the upgrade can be completed."""
        if self.state == "updating":
            self.complete_upgrade()