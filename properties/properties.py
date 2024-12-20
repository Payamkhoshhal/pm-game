import pygame
import os

pygame.font.init()  # Initialize the font module
font = pygame.font.Font(os.path.join("game_assets/fonts", "JungleAdventurer.ttf"), 48) 

def render_text_with_stroke(text, font, text_color, stroke_color, stroke_size=2):
    base_text = font.render(text, True, text_color)
    width, height = base_text.get_size()
    surface = pygame.Surface((width + stroke_size * 2, height + stroke_size * 2), pygame.SRCALPHA)

    # Render stroke around the text
    for dx in range(-stroke_size, stroke_size+1):
        for dy in range(-stroke_size, stroke_size+1):
            if dx != 0 or dy != 0:  # Avoid center duplication
                stroke_text = font.render(text, True, stroke_color)
                surface.blit(stroke_text, (dx + stroke_size, dy + stroke_size))

    # Render main text on top
    surface.blit(base_text, (stroke_size, stroke_size))
    return surface

################### Classes
class ShowLevel:
    def __init__(self):
        self.imgs = []
        for x in range(2):
            x += 1
            level = str(x)
            self.imgs.append( pygame.transform.scale(pygame.image.load(os.path.join("game_assets/levels",  "level"+level +".png")),(200, 64)))

    def draw(self, win, cam_x, cam_y, x, y, level):

        win.blit(self.imgs[level - 1] ,(x - cam_x - 40 , y - cam_y - 50))


class WoodLog:
    def __init__(self):
        self.score = 0
        self.x = 940
        self.y = 6
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/wood-log", "woodlog.png")), (50, 50))
         
    def draw(self, win ):
        win.blit(self.img , (self.x  , self.y ))
        font = pygame.font.Font(None, 36)
        score_lable = font.render(f"{self.score} x", True, (101, 67, 33))
        sl_width , sl_heigt = score_lable.get_size()
        win.blit(score_lable, (self.x - 5 - sl_width , self.y + 12 ))
    
