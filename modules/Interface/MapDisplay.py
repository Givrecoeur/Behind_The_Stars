# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:02:23 2017

@author: Benoît
"""
import pygame

import CstSystem as csts
import InterfaceElements as IE
import random
import Background

path = "data/images/map/"

map_background = Background.Background(1, 0)
map_background = map_background.sky

clicked = pygame.image.load(path + "Clicked.png")
clicked.set_colorkey((0,0,0))
overflown = pygame.image.load(path + "Overflown.png")
overflown.set_colorkey((0,0,0))

info_star_win = pygame.image.load(path + "InfoStar.png")
overflown.set_colorkey((0,0,0))

d_star_images = {"brown dwarf": ["Brown_dwarf.png"], "red dwarf": ["Red_dwarf.png"], "yellow dwarf": ["Yellow_dwarf.png"] , "giant red": ["Giant_red.png"] , "giant blue": ["Giant_blue.png"] , "supergiant red": ["Supergiant_red.png"] , "white dwarf": ["White_dwarf.png"] , "black dwarf": ["Black_dwarf.png"], "neutron": ["Neutron.png"], "black hole": ["Black_hole.png"], "white hole": ["White_hole.png"], "void": ["Void.png"]}


class Map(IE.Window):
    
    def __init__(self, sys, world, selected_star):
        
        IE.Window.__init__(self, None, 0, 0, csts.SCREEN_WIDTH, csts.SCREEN_HEIGHT, map_background, sys)
        
        self.selected_star = None
        
        for star in world.l_stars:
            self.childWin.append(ButtonStar(self, star))
            if star == selected_star:
                self.childWin[-1].l_clicked = True
                self.selected_star = self.childWin[-1]
            
        
        
class ButtonStar(IE.Button):
    
    def __init__(self, motherMap, star):
        
        image_not_clicked = pygame.image.load(path + random.choice(d_star_images[star.star_type]))
        image_not_clicked.set_colorkey((0,0,0))
        width = image_not_clicked.get_width()
        height = image_not_clicked.get_height()
        
        image_clicked = image_not_clicked.copy()
        image_clicked.blit(clicked, (0, 0))
    
        image_overflown = image_not_clicked.copy()
        image_overflown.blit(overflown, (0, 0))       
        
        IE.Button.__init__(self, motherMap, star.x - int(width / 2), motherMap.height - star.y - int(height / 2), width, height, image_not_clicked, image_overflown, image_clicked, self.click_on_star)
        
    def l_click(self):
        self.l_clicked = True
        if self.motherWin.selected_star != self:
            self.motherWin.selected_star.l_clicked = False
            self.motherWin.selected_star = self
        
    def l_unclick(self):
        if self.overflown and self.l_clicked:
            self.function()
    
    def click_on_star(self):
        if type(self.system.main_window) == Map:
            InfoStar(self)
        
        
    
class InfoStar(IE.HostedWindow):
    
    def __init__(self, star_button):
        
        self.font = pygame.font.Font(None, 20)
        
        width = info_star_win.get_width()
        height = info_star_win.get_height()
        x = 0
        y = 0
        
        if star_button.x + star_button.width + width < csts.SCREEN_WIDTH:
            x = star_button.x + star_button.width
        else:
            x = star_button.x - width
            
        if star_button.y + star_button.height + height < csts.SCREEN_HEIGHT:
            y = star_button.y + star_button.height
        else:
            y = star_button.y - height
            
        IE.HostedWindow.__init__(self, star_button, x, y, width, height, info_star_win)
    
        
    def click_out(self):
        self.close()
