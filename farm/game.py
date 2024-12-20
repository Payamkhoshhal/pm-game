import pygame 
import os
from farmer.farmer import Farmer
from trees.tree import Tree
from menu.menu import Menu , MainMenu
from loading.load import Loading 
from properties.properties import WoodLog

class Game:

    def __init__(self):
        # background
        self.width = 1000 
        self.height = 800 
        self.win = pygame.display.set_mode((self.width , self.height))
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/background","grass-bg.png")) , (1500, 1500) )
        self.click = (0,0)
        pygame.font.init()  # Initialize the font module
        
        # Load arrows 
        self.which_arrow = 0 # none of them
        # Right = 1
        self.arrow_r =pygame.transform.scale( pygame.image.load(os.path.join("game_assets/arrows","right-arrow.png")),(45,45))
        self.is_r_arrow = False
        # Left = 2
        self.arrow_l =pygame.transform.scale( pygame.image.load(os.path.join("game_assets/arrows","left-arrow.png")),(45,45))
        self.is_l_arrow = False
        # up = 3
        self.arrow_u =pygame.transform.scale( pygame.image.load(os.path.join("game_assets/arrows","up-arrow.png")),(45,45))
        self.is_u_arrow = False
        # down = 4
        self.arrow_d =pygame.transform.scale( pygame.image.load(os.path.join("game_assets/arrows","down-arrow.png")),(45,45))
        self.is_d_arrow = False
        
        self.base_home = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/buildings","base-home.png")),(100,100)) 

        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize objects
        # woodlog  
        self.woodlog = WoodLog()

        # tree
        self.trees = []
        #self.upgrade_times = [10 , 30]
        #self.trees.append(Tree(120, 200, 200, 150, self.upgrade_times))

        # farmer
        self.farmer = Farmer() # create an instance from class Farmer
        self.farmer_pos = (self.farmer.x, self.farmer.y)

        # menu
        self.main_menu = MainMenu()
        self.menu = Menu()
        self.menu_result = None


        self.MAP_WIDTH, self.MAP_HEIGHT = self.bg.get_size()
        # Camera Position
        self.camera_x, self.camera_y = 0, 0

        # Scrolling Settings
        self.SCROLL_SPEED = 10
        self.EDGE_MARGIN = 2

        # Drag object
        self.drag_object = False

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.drag_object:
                        if self.menu_result == 'Add tree':
                            tree_x = event.pos[0]  + self.camera_x - 75
                            tree_y = event.pos[1]  + self.camera_y - 75
                            self.trees.append(Tree(tree_x, tree_y, 150, 150))
                            self.drag_object = False
                    
                    self.which_object_is_clicked(event.pos)

                    if not self.farmer.farmer_clicked:
                        if self.farmer.farmer_pre_clicked:
                            self.farmer.is_allowed_to_move = True
                            self.farmer_pos = event.pos 
                            self.farmer.cam_x_moment = self.camera_x
                            self.farmer.cam_y_moment =  self.camera_y
                            self.farmer.farmer_pre_clicked = True
                            print('farmer is clicked') 

                    if self.menu.menu_visible:
                        self.menu_result = self.menu.which_button_is_clicked(event.pos) 
                        if self.menu_result: 
                            self.menu.menu_visible = False
                            self.drag_object = True
                        else:
                            self.drag_object = False

                                

                    self.click = pos
                    print(pos)
                    # Get Mouse Position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if (mouse_x > 0 or mouse_x <= self.width) and  (mouse_y >= 0 or mouse_y <= self.height): # this condition can be removed
                # Edge Scrolling Logic
                if mouse_x <= self.EDGE_MARGIN :  # Left edge
                    self.camera_x = max(self.camera_x - self.SCROLL_SPEED, 0)
                    self.which_arrow = 2
                elif mouse_x >= self.width - self.EDGE_MARGIN  :  # Right edge
                    self.camera_x = min(self.camera_x + self.SCROLL_SPEED, self.MAP_WIDTH - self.width)
                    self.which_arrow = 1
                elif mouse_y <= self.EDGE_MARGIN:  # Top edge
                    self.camera_y = max(self.camera_y - self.SCROLL_SPEED, 0)
                    self.which_arrow = 3
                elif mouse_y >= self.height - self.EDGE_MARGIN:  # Bottom edge
                    self.camera_y = min(self.camera_y + self.SCROLL_SPEED, self.MAP_HEIGHT - self.height)        
                    self.which_arrow = 4
                else:
                    self.which_arrow = 0


            self.draw(self.farmer_pos, self.camera_x, self.camera_y, self.which_arrow )
 
        pygame.quit()

 
    
    def which_object_is_clicked(self, clicked_pos):
        flag = 0
        for tree in self.trees:
            if tree.is_clicked(clicked_pos):
                # enable the tree clicked variable
                tree.tree_clicked = True
                flag = 1
           
                # disable other objects
                self.farmer.farmer_clicked =  False 
                self.farmer.farmer_pre_clicked = False
                self.menu.menu_visible = False
            else:
                tree.tree_clicked = False
        if flag == 0:
            if self.farmer.is_clicked(clicked_pos):

                # enable the farmer clicked variable
                self.farmer.farmer_clicked = True
                self.farmer.farmer_pre_clicked = False
                # disable other objects 
                for tree in self.trees:
                    tree.tree_clicked = False

                self.menu.menu_visible = False


            elif self.main_menu.is_clicked(clicked_pos):

                # enable main menu object
                self.main_menu.visible = False
                self.menu.menu_visible = True
                # disable other objects
                self.farmer.farmer_clicked = False
                for tree in self.trees:
                    tree.tree_clicked = False            
                self.farmer.farmer_pre_clicked = False

            elif self.menu.is_clicked(clicked_pos):
                # we don't need to disable other object since they are alrady disabled when we see this menu
                self.farmer.farmer_pre_clicked = False
                self.farmer.farmer_clicked = False
                for tree in self.trees:
                    tree.tree_clicked = False

            else:
                # disable all the objects
                if self.farmer.farmer_clicked == True:
                    self.farmer.farmer_clicked = False
                    self.farmer.farmer_pre_clicked = True

                for tree in self.trees:
                    tree.tree_clicked = False
                self.menu.menu_visible = False


    def draw(self,farmer_pos, cam_x , cam_y, is_arrow):
        self.win.blit(self.bg , (- cam_x, - cam_y))
        self.win.blit(self.base_home,(400-cam_x , 400-cam_y))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.which_arrow == 1: 
            self.win.blit(self.arrow_r, (mouse_x -40  , mouse_y - 20))
        elif self.which_arrow == 2: 
            self.win.blit(self.arrow_l, (mouse_x , mouse_y -20 ))
        elif self.which_arrow == 3: 
            self.win.blit(self.arrow_u, (mouse_x -20 , mouse_y ))
        elif self.which_arrow == 4: 
            self.win.blit(self.arrow_d, (mouse_x -20 , mouse_y - 40))
        else:
                # Draw Default Cursor Substitute (Small Circle)
            pygame.draw.circle(self.win, (0, 0, 0), (mouse_x, mouse_y), 5)

       
        self.farmer.draw(self.win,cam_x , cam_y , self.farmer_pos )

        for tree in self.trees[::-1]:
            tree.draw(self.win, cam_x , cam_y)
            collect_wood_from_each_tree = tree.calculate_woodlog_score()
            if collect_wood_from_each_tree != 0: 
                self.woodlog.score = self.woodlog.score + collect_wood_from_each_tree        


        
        #  always stay on screen stuff
        self.main_menu.draw(self.win)

        self.menu.draw(self.win)

        self.woodlog.draw(self.win )

        p = self.click
        pygame.draw.circle(self.win, (255,0,0) , (p[0],p[1]), 5, 0) # help to see where i click
        # Update the display
        pygame.display.flip()
        pygame.display.update()


g = Game()
g.run()
