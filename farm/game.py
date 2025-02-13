
import pygame 
import os
from farmer.farmer import Farmer
from trees.tree import Tree
from menu.menu import Menu  
from mouse.mouse import Mouse

from properties.properties import WoodLog , RockLog

from bases.homebase import HomeBase
from bases.rockbase import RockBase




class Game:

    def __init__(self):
        # background
        self.width = 1000 
        self.height = 800 
        self.win = pygame.display.set_mode((self.width , self.height))
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/background","grass-bg.png")) , (1500, 1500) )
        self.click = (0,0)
        
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
        

        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize objects
        # woodlog  
        self.woodlog = WoodLog()

        # rocklog
        self.rocklog = RockLog()
        
        # tree
        self.trees = []
        #self.upgrade_times = [10 , 30]
        #self.trees.append(Tree(120, 200, 200, 150, self.upgrade_times))
        self.max_tree_count = [3,6,12,15] # each element is the level of homebase for eg: level 1 --> max 3 tree
        # farmer
        self.farmer = Farmer() # create an instance from class Farmer
        self.farmer_pos = (self.farmer.x, self.farmer.y)
        self.is_tree_dragable = 1

        # menu
        self.menu_result = None
        self.menu = Menu()

        # Bases        
        # home base
        self.homebase = HomeBase()

        # rock base
        self.rock_base = None

        # Camera Position
        self.MAP_WIDTH, self.MAP_HEIGHT = self.bg.get_size()
        self.camera_x, self.camera_y = 0, 0

        # Scrolling Settings
        self.SCROLL_SPEED = 10
        self.EDGE_MARGIN = 2

        # Drag object
        self.drag_object = False

        # Mouse
        self.mouse_is_defult = 1
        self.mouse_style = Mouse()
        self.default_cursor = pygame.SYSTEM_CURSOR_ARROW 
        pygame.mouse.set_cursor(self.default_cursor)

        # Level dict
        self.home_base_level = 1


        self.obj_on_map = {'homebase':self.homebase , 'farmer':self.farmer, 'trees':[] }

    def run(self):
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if self.drag_object:
                        if self.menu_result == 'tree':
                            tree_x = event.pos[0]  + self.camera_x - 75
                            tree_y = event.pos[1]  + self.camera_y - 75
                            new_tree = Tree(tree_x, tree_y, 150, 150)
                            self.trees.append(new_tree)
                            self.obj_on_map['trees'].append(new_tree)
                            self.drag_object = False
                            pygame.mouse.set_visible(True)                            
                            self.mouse_is_defult = 1
                        elif self.menu_result == 'rb':
                            rb_x = event.pos[0] + self.camera_x - 100
                            rb_y = event.pos[1] + self.camera_y  - 105
                            self.rock_base = RockBase(rb_x, rb_y , 256 , 256)
                            self.obj_on_map['rock_base'] = self.rock_base
                            print('rock base has been created')
                            self.drag_object = False
                            pygame.mouse.set_visible(True)                            
                            self.mouse_is_defult = 1

                    if self.menu.hb_menu_visible:
                        self.menu_result = self.menu.which_button_is_clicked(event.pos) 
                        if self.menu_result: 
                            self.menu.hb_menu_visible = False
                            if self.menu_result == 'tree' and len(self.trees) <  self.max_tree_count[self.home_base_level - 1]:
                                    self.drag_object = True
                                    self.mouse_is_defult = 0
                                    print('drag object is true => tree')
                            if self.menu_result == 'rb':
                                    self.drag_object = True
                                    self.mouse_is_defult = 0
                                    print('drag object is true => rb')
                        else:
                            self.drag_object = False

                    self.which_object_is_clicked(event.pos)
                    
                    if  len(self.trees) >= self.max_tree_count[self.home_base_level - 1]:
                        self.is_tree_dragable = 0
                    else: 
                        self.is_tree_dragable = 1

                    if not self.farmer.farmer_clicked: 
                        if self.farmer.farmer_pre_clicked:
                            self.farmer.is_allowed_to_move = True
                            self.farmer_pos = event.pos 
                            self.farmer.cam_x_moment = self.camera_x
                            self.farmer.cam_y_moment =  self.camera_y
                            self.farmer.farmer_pre_clicked = True
                           

                    

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


            self.draw( self.camera_x, self.camera_y)
 
        pygame.quit()

 
    
    def which_object_is_clicked(self, clicked_pos):
        background_flag = 1 
        for obj_name , obj in self.obj_on_map.items(): 
            if isinstance(obj, list):
                for tree in self.trees:
                    if tree.is_clicked(clicked_pos):
                        tree.tree_clicked = True

                        # disable other objects
                        self.farmer.farmer_clicked =  False 
                        self.farmer.farmer_pre_clicked = False
                        self.menu.hb_menu_visible = False
                        self.homebase.homebase_clicked = False
                        #self.rock_base.rockbase_clicked = False
                        background_flag = 0
                    else: 
                        tree.tree_clicked = False
            
            else :
                if obj.is_clicked(clicked_pos): 
                    if obj_name == 'farmer':
                        # enable the farmer clicked variable
                        self.farmer.farmer_clicked = True
                        self.farmer.farmer_pre_clicked = False 
                        background_flag = 0
                        # disable other objects 
                        for tree in self.trees:
                            tree.tree_clicked = False

                        self.menu.hb_menu_visible = False
                        self.homebase.homebase_clicked = False
                        if self.rock_base:
                            self.rock_base.rockbase_clicked = False
                        break
                        
                    elif obj_name == 'homebase':
                        # homebase clicked 
                        self.homebase.homebase_clicked = True
                        background_flag = 0
                        # enable main menu object
                        self.menu.hb_menu_visible = True
                        self.menu.rb_menu_visible = False
                        # disable other objects
                        self.farmer.farmer_clicked = False
                        for tree in self.trees:
                            tree.tree_clicked = False            
                        self.farmer.farmer_pre_clicked = False
                        if self.rock_base:
                            self.rock_base.rockbase_clicked = False
                        break
                        
                    elif obj_name == 'rock_base':
                        background_flag = 0
                        # homebase clicked 
                        self.rock_base.rockbase_clicked = True
                        # enable main menu object
                        self.menu.hb_menu_visible = False
                        self.menu.rb_menu_visible = True
                        # disable other objects
                        self.homebase.homebase_clicked = False
                        self.farmer.farmer_clicked = False
                        for tree in self.trees:
                            tree.tree_clicked = False
                        self.farmer.farmer_pre_clicked = False
                        break
        if background_flag == 1:
            print('background_flag is 1')
            # disable all the objects
            if self.farmer.farmer_clicked == True:
                self.farmer.farmer_clicked = False
                self.farmer.farmer_pre_clicked = True
            for tree in self.trees:
                tree.tree_clicked = False
            self.menu.hb_menu_visible = False
            self.menu.rb_menu_visible = False
            self.homebase.homebase_clicked = False
            if self.rock_base:
                self.rock_base.rockbase_clicked = False

        '''
        flag = 0
        for tree in self.trees:
            if tree.is_clicked(clicked_pos):
                # enable the tree clicked variable
                tree.tree_clicked = True
                flag = 1
           
                # disable other objects
                self.farmer.farmer_clicked =  False 
                self.farmer.farmer_pre_clicked = False
                self.menu.hb_menu_visible = False
                self.homebase.homebase_clicked = False
                #self.rock_base.rockbase_clicked = False
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

                self.menu.hb_menu_visible = False
                self.homebase.homebase_clicked = False
                #self.rock_base.rockbase_clicked = False

            


            elif self.homebase.is_clicked(clicked_pos):
                # homebase clicked 
                self.homebase.homebase_clicked = True
                # enable main menu object
                self.menu.hb_menu_visible = True
                # disable other objects
                self.farmer.farmer_clicked = False
                for tree in self.trees:
                    tree.tree_clicked = False            
                self.farmer.farmer_pre_clicked = False
                #self.rock_base.rockbase_clicked = False

            elif self.rock_base and self.rock_base.is_clicked(clicked_pos):
                # homebase clicked 
                self.rock_base.rockbase_clicked = True
                # enable main menu object
                self.menu.hb_menu_visible = True
                # disable other objects
                self.farmer.farmer_clicked = False
                for tree in self.trees:
                    tree.tree_clicked = False            
                self.farmer.farmer_pre_clicked = False
            else:
                # disable all the objects
                if self.farmer.farmer_clicked == True:
                    self.farmer.farmer_clicked = False
                    self.farmer.farmer_pre_clicked = True
                    
                for tree in self.trees:
                    tree.tree_clicked = False
                self.menu.hb_menu_visible = False
                self.homebase.homebase_clicked = False
                #self.rock_base.rockbase_clicked = False
                '''
    def draw(self, cam_x , cam_y):

        # Draw background image
        self.win.blit(self.bg , (- cam_x, - cam_y))

        # Draw farmer mr.potato 
        self.farmer.draw(self.win,cam_x , cam_y , self.farmer_pos )

        # Draw tree and calculate woodlog score
        for tree in self.trees[::-1]:
            tree.draw(self.win, cam_x , cam_y)
            collect_wood_from_each_tree = tree.calculate_woodlog_score()
            if collect_wood_from_each_tree != 0: 
                self.woodlog.score = self.woodlog.score + collect_wood_from_each_tree        

        if self.rock_base:
            collect_rock = self.rock_base.calculate_rocklog_score()
           
            self.rocklog.score = self.rocklog.score + collect_rock

        # Draw woodlog score
        self.woodlog.draw(self.win )

        # Draw rocklog score
        self.rocklog.draw(self.win)

        # Draw homebase
        self.homebase.draw(self.win, cam_x, cam_y)

        # Draw rockbase
        if self.rock_base: 
            self.rock_base.draw(self.win, cam_x, cam_y)
        
        # Draw menues
        # 1- Draw home base menu
        self.menu.draw_hm_menu(self.win , self.is_tree_dragable )
        self.menu.draw_rb_menu(self.win)

        # Draw arrows directions
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
            pygame.draw.circle(self.win, (0, 0, 0), (mouse_x, mouse_y), 0)

        if self.mouse_is_defult == 0 :
            self.mouse_style.draw(self.win, mouse_x, mouse_y )

        p = self.click
        pygame.draw.circle(self.win, (255,0,0) , (p[0],p[1]), 5, 0) # help to see where i click
        # Update the display
        pygame.display.flip()
        pygame.display.update()


g = Game()
g.run()


