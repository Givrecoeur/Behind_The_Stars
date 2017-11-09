# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:23:24 2017

@author: Benoît
"""

import pygame
import InterfaceElements as IE
import CstSystem as csts

path = "data/images/TitleScreen/"

class TitleScreen(IE.Window):
    
    def __init__(self, sys):
        
        background = pygame.image.load(path + "Background.png")
        IE.Window.__init__(self, None, 0, 0, csts.SCREEN_WIDTH, csts.SCREEN_HEIGHT, background, sys)
        
        mainmenu_image = pygame.image.load(path + "MainMenu.png")
        width =  mainmenu_image.get_width()
        height = mainmenu_image.get_height()
        mainmenu = IE.Window(self, 1420, 100, width, height, mainmenu_image)
        
        IE.create_button(mainmenu, 1460, 140, path, "NewGame", self.new_game)
        IE.create_button(mainmenu, 1460, 260, path, "Continue", self.continue_game)
        IE.create_button(mainmenu, 1460, 380, path, "Settings", self.open_settings)
        IE.create_button(mainmenu, 1460, 500, path, "More", self.see_more)
        IE.create_button(mainmenu, 1460, 620, path, "Quit", self.quit_game)

        
    def new_game(self):
        pass
    
    
    def continue_game(self):
        pass
    
    
    def open_settings(self):
        pass
    
    
    def see_more(self):
        pass
    