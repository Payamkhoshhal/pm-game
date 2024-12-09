import pygame
import os
import math


imgs = []
for x in range(10):
    x += 1
    add_str = str(x)
    
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/charachters", "corrected_walking_frame_" + add_str + ".png")),
        (64, 64)))


class Farmer:


    def __init__(self):
        self.name = 'farmer'
        self.animation_count = 0 
        #self.img =  pygame.transform.scale(pygame.image.load(os.path.join("game_assets/charachters", "farmer.png" )), (128, 128))
        self.imgs = imgs
        self.vel = 0
        self.path = [(200,150),(700,150)]
        #self.path = [(450, 175),(401, 196),(319, 229),(297, 239),(353, 280),(400, 317),(454, 367),(497, 405),(527, 438),(474, 491)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.speed = 2
        self.step = 1
        self.flipped = False  

    def draw(self, win):
        """
        Draws the Farmer with the given images
        :param win: sufrace
        :return: None 
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        win.blit(self.img, (self.x , self.y))
        self.move()


    def collide (self , x, y):
        pass


    def move(self):

        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        next_x , next_y = self.path[self.step]


        current_x = self.x 
        current_y = self.y

        #if next_x == current_x and next_y == current_y:
        #    # reached to the next point
        #    self.step += 1 

        dx = next_x - current_x  #current[0]
        dy = next_y - current_y  #current[1]

        # Calculate the distance
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normalize the direction and scale by speed
        if distance != 0:  # Avoid division by zero
            dx = (dx / distance) * self.speed
            dy = (dy / distance) * self.speed


        # direction of the charachter
        #if next_x > current_x:
        #    print(next_x , current_x) 
        #    #self.flipped = True
        #    print(self.flipped)
        #    self.img = pygame.transform.flip( self.img, True , False )  

        # Update the current position
        self.x += dx
        self.y += dy

        # Check if close enough to the target to stop
        if abs(next_x - current_x) < self.speed and abs(next_y - current_y) < self.speed:
            current_x = next_x
            current_y = next_y
            self.step += 1
            if self.step  >= len(self.path):
                return False
        return True
       # if self.step < len(self.path)-1:
       #     self.step += 1
       #     print(self.step)
       #     print(len(self.path))

      
    
       
    
        
    
