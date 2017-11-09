"""This module manage UI objects like windows, buttons, drag and drop...
These class are basics, provide not resizable during use objects, and should be 
inherited by more specific class to make more specifics UI"""

import pygame

path = "data/fonts/"

class InterfaceElement():
    """abstract class"""
    
    def __init__(self, motherWin, x, y, width, height, sys = None):
        """abstract constructor, x, y, height, width must be positiv. x, y, height,
        width are the position and dimension in pixel  of the element. If x, y, height,
        width are between 0 and 1, they represents position, dimension relative 
        to the the motherWin position, dimension."""
              
        
        self.childWin = []  
        self.image = None
        
        self.r_clicked = False
        self.l_clicked = False
        
        self.font = pygame.font.Font(path + "LiberationSans-Regular.ttf", 10)
        
        self.motherWin = motherWin
        if self.motherWin == None:
            self.system = sys  
            self.rank = 0
            self.x = x
            self.y = y
            self.height = height
            self.width = width
            
        else:   
            self.system = self.motherWin.system
            self.motherWin.childWin.append(self)
            self.rank = motherWin.rank + 1
            
            if x < 1:
                self.x = self.motherWin.width * (1 + x)
            else:
                self.x = x
            
            if y < 1:
                self.y = self.motherWin.height * (1 + y)
            else:
                self.y = y
                
            if width < 1:
                self.width = self.motherWin.width * width
            else:
                self.width = width
                
            if height < 1:
                self.height = self.motherWin.height * height
            else:
                self.height = height
                
    
    def set_font(self, size, bold, italic):
        if bold:
            self.font = pygame.font.Font(path + "LiberationSans-Bold.ttf", size)
        if italic:
            self.font = pygame.font.Font(path + "LiberationSans-Italic.ttf", size)
        if italic and bold:
            self.font = pygame.font.Font(path + "LiberationSans-BoldItalic.ttf", size)
        else:
            self.font = pygame.font.Font(path + "LiberationSans-Regular.ttf", size)
        
        
        
    def write(self, pos, text, color = (0,0,0), rot = 0):
        text_image = self.font.render(text, True, color)
        if rot != 0:
            text_image = pygame.transform.rotate(text_image, rot)
        self.image.blit(text_image, pos)
        
                
    def set_pause(self):
        pass
    
    
    def quit_game(self):
        self.system.done = True
                
                
    def display(self, surf):
        surf.blit(self.image, (self.x, self.y))
        
        for child in self.childWin:
            child.display(surf)
            
    
    def scroll(self, dy):
        pass
    
    
    def r_click(self):
        pass
    
    
    def l_click(self):
        pass
    
    
    def r_unclick(self):
        self.r_clicked = False
        for win in self.childWin:
            win.r_unclick()
    
    
    def l_unclick(self):
        self.l_clicked = False
        for win in self.childWin:
            win.l_unclick()
    
    
    def mouse_overflown(self):
        pass
    
    
    def click_out(self):
        pass
    
    
    def get_overflown_window(self, pos):
        x = pos[0]
        y = pos[1]
        if x >= self.x and x <= self.x + self.width and y >= self.y and y <= self.y + self.height:
            for child in self.childWin:
                test = child.get_overflown_window(pos)
                if test != None:
                    return test
            return self
        return None



#=============================================================================#
#=============================================================================#
#=============================================================================#
           
            

class Window(InterfaceElement):
    """A basic window, which can contain Buttons, Items... and other windows"""
    
    def __init__(self, motherWin, x, y, width, height, image, sys = None):
        """Constructor, x, y, height, width are the position and dimension in pixel 
        of the window. If x, y, height, width are between 0 and 1, they represents
        position, length relative to the the motherWin position, length. A window
        with None as mother win can't use such arguments"""
        
        InterfaceElement.__init__(self, motherWin, x, y, width, height, sys)
        
        self.image = image
        
        

#=============================================================================#
#=============================================================================#
#=============================================================================#

        
        
class HostedWindow(InterfaceElement):
    
    def __init__(self, motherWin, x, y, width, height, image, sys = None):
        
            
        InterfaceElement.__init__(self, motherWin, x, y, width, height, sys) 

        
        self.host = self.system.main_window
        self.system.main_window = self
            
        self.image = image
        
        
    def close(self):
        self.system.main_window = self.host
        
        
    def display(self, surf):
        if self.system.main_window == self:
            InterfaceElement.display(self, surf)


#=============================================================================#
#=============================================================================#
#=============================================================================#

          

class Button(Window):
    """A clickable button, linked to a function"""
    
    def __init__(self, motherWin, x, y, width, height, image_not_clicked, image_overflown, image_clicked, function):
        """Constructor, x, y, height, width are the position and dimension in pixel 
        of the button. If x, y, height, width are between 0 and 1, they represents
        position, length relative to the the motherWin position, length. A button 
        must have a motherWin and must not have childWin"""

        Window.__init__(self, motherWin, x, y, width, height, image_not_clicked)
        
        self.image_clicked = image_clicked
        self.image_overflown = image_overflown
        self.image_not_clicked = image_not_clicked
        self.function = function
        self.overflown = False
        
        
    def execute(self):
        self.function()
        
            
    def display(self, surf):
        if not self.l_clicked:
            surf.blit(self.image_not_clicked, (self.x, self.y))
    
        if self.overflown:
            surf.blit(self.image_overflown, (self.x, self.y))
            self.overflown = False
        
        if self.l_clicked:
            surf.blit(self.image_clicked, (self.x, self.y))
            
    
    def mouse_overflown(self):
        self.overflown = True
        
        
    def l_click(self):
        self.l_clicked = True
        
        
    def l_unclick(self):
        
        if self.overflown and self.l_clicked:
            self.function()
        self.l_clicked = False
            
            
def create_button(motherWin, x, y, path, name, function):
    """a shorter way to generate button, name stands for a string containing the
    name of the file of the image of the non cliked button and path is the realtiv 
    path to access it The function return None because the button will be declared 
    in its motherWin"""
    
    image = pygame.image.load(path + name + ".png")
    width = image.get_width()
    height = image.get_height()
    image_overflown = pygame.image.load(path + name + "Overflown.png")
    image_clicked = pygame.image.load(path + name + "Clicked.png")
    Button(motherWin, x, y, width, height, image, image_overflown, image_clicked, function)
            
        
        
#=============================================================================#
#=============================================================================#
#=============================================================================#
 
       

class ItemList(InterfaceElement):
    """an container specialized in the display of a list of items"""
    
    def __init__(self, motherWin, x, y, width, height, item_list,  display_type):
        """Constructor, x, y, height, width are the position and dimension in pixel 
        of the ListDisplay. If x, y, height, width are between 0 and 1, they represents
        position, length relative to the the motherWin position, length. A ListDisplay 
        must have a motherWin and must not have childWin"""
        
        InterfaceElement.__init__(self, motherWin, x, y, width, height)
        
        self.l_item = item_list
        self.display_type = display_type
        self.y_scrolling = 0
        self.surf = None
        self.item_width = self.l_item[0][0].image.get_width()
        self.item_height = self.l_item[0][0].image.get_height() #items are supposed to have all the same size if in the same list
        self.set_display()
        
        
    def scroll(self, dy):
        self.y_scrolling += dy
        diff = self.surf.get_height() - self.height
        if self.y_scrolling < 0:
            self.y_scrolling = 0
        elif self.y_scrolling > diff:
            if diff < 0:
                self.y_scrolling = 0
            else:
                self.y_scrolling = diff
        
        self.modified = True
        
        
    def set_display(self):
        
        if self.display_type == "v_list":
            self.set_display_v_list()
        elif self.display_type == "table":
            self.set_display_table()
    
    
    def set_display_v_list(self):
        self.surf = pygame.Surface((self.width, len(self.l_item)* self.item_height))
        for i in range(0, len(self.l_item)):
            self.surf.blit(self.l_item[i][0].image, (0, self.height_item * i))
            
       
    def set_display_table(self):
        nb_item_per_line = self.width // self.item_width
        self.surf = pygame.Surface((self.width, ((len(self.l_item) // nb_item_per_line) + 1) * self.item_height))
        for i in range(0, self.l_item):
            self.surf.blit(self.l_item[i][0].image, (i % nb_item_per_line * self.item_width, i // nb_item_per_line * self.item_height))
            
            
    def display(self, surf):
        if self.modified:
            surf.blit(self.surf, (self.x, self.y), pygame.Rect(self.x, self.y_scrolling, self.width, self.height))
            self.modified = False
        
    
    def remove_one(self, item):
        for i in range(0, self.l_item):
            if self.l_item[i][0] == item:
                self.l_item[i][1] -= 1
                if self.l_item[i][1] == 0:
                    del self.l_item[i]
                self.set_display()
                break
            
        self.modified = True


    def remove_all(self, item):
        for i in range(0, self.l_item):
            if self.l_item[i][0] == item:
                nb = self.l_item[i][1]
                del self.l_item[i]
                self.set_display()
                return nb
                
        self.modified = True


    def add(self, item, nb_item, position):
        for i in range(0, self.l_item):
            if self.l_item[i][0] == item:
                self.l_item[i][1] += nb_item
                self.set_display()
                return True
        self.l_item = self.l_item[:i] + [item, nb_item] + self.l_item[i:]
        self.set_display()
        
        self.modified = True
        
        
    def select(self, pos):
        x = pos[0]
        y = pos[1]
        
        x -= self.x
        y -= self.y
        
        nb_item_per_line = self.width // self.item_width
        
        nb = nb_item_per_line * (y//self.item_height) + (x//self.item_width)
        self.l_item[nb].select()

        
        
        

class Item():
    """An entity with an id number, which is meant to be displayed, by himself or
    in an ItemList"""
    pass

if __name__ == "__main__":
    win = Window(None, 0,0, 10, 20, "tt")
    print(win)



    