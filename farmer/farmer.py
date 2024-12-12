import pygame
import os
import math


imgs = []
for x in range(8):
    x += 1
    add_str = str(x)
    
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/potato",  add_str +".png")),
        (32, 32)))


class Farmer:


    def __init__(self):
        self.name = 'farmer'
        self.animation_count = 0
        #self.img =  pygame.transform.scale(pygame.image.load(os.path.join("game_assets/charachters", "farmer.png" )), (128, 128))
        self.imgs = imgs
        self.vel = 0
        #self.path = [(200,150),(700,150)]
        self.path = [(500,220),(370, 280),(517, 445),(460 , 500), (532, 560),(838, 455),(851, 370),(660, 189)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.speed = 5
        self.flipped = False  
        self.direction = 'left'
        self.img = self.imgs[self.animation_count]
        #self.rect = self.img.get_rect(topleft=(self.x - cam_x , self.y - cam_y))
        self.farmer_clicked = False
        self.farmer_pre_clicked = False
        self.is_allowed_to_move = False
        self.is_moving = False
        # we need it because when we are moving the map, the clicked position will change 
        # if we add the cam_x each time so we have to store the cam_x at that moment to keep it constant
        self.cam_x_moment = 0
        self.cam_y_moment = 0

    def draw(self,win,cam_x , cam_y , pos):
        """
        Draws the Farmer with the given images
        :param win: sufrace
        :return: None 
        """
        

        if self.farmer_clicked == True:
            self.range = 100
            surface = pygame.Surface((self.range*4 , self.range*4), pygame.SRCALPHA, 32) 
            pygame.draw.circle(surface,(210, 140, 70,150),(self.range,self.range),self.range, 0)
            win.blit(surface,(self.x - cam_x  - 70, self.y - cam_y - 70))

        if self.is_moving:
            current_x = self.x
            current_y = self.y
        else:
            current_x = self.x - cam_x
            current_y = self.y - cam_y 

        self.img = self.imgs[self.animation_count] 
        if self.is_allowed_to_move :
            # if we reached to the point don't need to move anymore
            next_x = pos[0] + self.cam_x_moment
            next_y = pos[1] + self.cam_y_moment
           
            if abs(next_x - current_x) > self.speed and abs(next_y - current_y) > self.speed:
                self.is_moving = True
                self.move_to(pos, cam_x , cam_y)
                
            else:
                self.is_allowed_to_move = False
                self.is_moving = False

        self.rect = self.img.get_rect(topleft=(self.x - cam_x, self.y - cam_y ))
        win.blit(self.img, (self.x - cam_x , self.y - cam_y))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def move_to(self, pos , cam_x , cam_y ):
        next_x = pos[0] + self.cam_x_moment
        next_y = pos[1] + self.cam_y_moment
        
        current_x = self.x 
        current_y = self.y

        self.animation_count += 1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        dx = next_x - current_x  
        dy = next_y - current_y  

        # Calculate the distance
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normalize the direction and scale by speed
        if distance != 0:  # Avoid division by zero
            dx = (dx / distance) * self.speed
            dy = (dy / distance) * self.speed

        # direction of the charachter
        if dx > 0 :
            if self.direction == 'left':
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False) 
            self.direction = 'right'
        if dx < 0:
            if self.direction == 'right':
                for x, img in enumerate(self.imgs):
                    self.imgs[x] = pygame.transform.flip(img, True, False)  
            self.direction = 'left'

        # Update the current position
        self.x = self.x + dx
        self.y = self.y + dy 

        # Check if close enough to the target to stop
        if abs(next_x - current_x) < self.speed and abs(next_y - current_y) < self.speed:
            current_x = next_x
            current_y = next_y

            

    
       