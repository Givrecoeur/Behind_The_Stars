# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:06:06 2017

@author: Benoît
"""

import pygame

path = "data/images/Interface/"

class TextDisplay():
    def __init__(self, pos):
        self.font = pygame.font.Font(None, 20)
        self.x = pos[0]
        self.y = pos[1]

    def display(self, surface, textString, color, rot = 0):
        textBitmap = self.font.render(textString, True, color)
        textBitmap = pygame.transform.rotate(textBitmap, rot)
        surface.blit(textBitmap, [self.x, self.y])
        
#=============================================================================#
#=============================================================================#
#=============================================================================#

class ImageDisplay():
    
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        
    def display(self, surface, image):
        imageBitmap = image
        surface.blit(imageBitmap, [self.x, self.y])
        
#=============================================================================#
#=============================================================================#
#=============================================================================#
        
class RectDisplay():
    
    def __init__(self, pos, width, height, l_image_pos, l_text_pos):
        
        self.x = pos[0]
        self.y = pos[1]        
        self.surface = pygame.Surface((width, height))
        self.surface.set_colorkey((0,0,0))
        self.surface.set_alpha(200)
        
        self.l_text = []
        self.l_image = []
        
        for pos in l_text_pos:
            self.l_text.append(TextDisplay(pos))
            
        for pos in l_image_pos:
            self.l_image.append(ImageDisplay(pos))
            
            
    def display(self, sys, l_image_contents, l_text_contents, l_text_color, l_text_rot):
        
        for i in range(0, len(self.l_image)):
            self.l_image[i].display(self.surface, l_image_contents[i])
        
        for i in range(0, len(self.l_text)):
            self.l_text[i].display(self.surface, l_text_contents[i], l_text_color[i], l_text_rot[i])
            
        sys.screen.blit(self.surface, (self.x, self.y))

#=============================================================================#
#=============================================================================#
#=============================================================================#
            
class ShooterInterface():
    
    def __init__(self, sys):
        
        self.system = sys
        pygame.mouse.set_visible(False)
        
        self.l_surf = []
        self.l_text = []
        
        #import all images #TODO
        self.mouse = pygame.image.load(path + "mouse_shooter.png")  
        self.mouse.set_colorkey((0,0,0))
        
        self.hp_back = pygame.image.load(path + "hp_back.png")
        self.full_hp = pygame.image.load(path +"hp_full.png")
        self.low_hp = pygame.image.load(path +"hp_low.png")
        self.very_low_hp = pygame.image.load(path +"hp_very_low.png")
        
        self.energy_back = pygame.image.load(path +"energy_back.png")
        self.energy = pygame.image.load(path +"energy.png")
        
        self.weapon_back = pygame.image.load(path +"weapon_back.png")
        self.reload_timer = 0
        
        
        self.abilities_back = 0
        self.abilities_1 = 0
        self.abilities_2 = 0
        self.abilities_1_timer = 0
        self.abilities_2_timer = 0
        
        
        #create all internal display areas
        self.hp_display = RectDisplay((50,50), 350, 30, [(0,0), (45,5)], [(160,9)])
        self.energy_display = RectDisplay((50,250), 30, 500, [(0,0), (5, 95)], [(8,250)])
        self.weapon_display = RectDisplay((1770,980), 100, 50, [(0,0), (5,5)], [(7,30)])
        """self.abilities_display = RectDisplay((0,0), 200, 50, [(0,0)], [(0,0)])"""
        

    def update(self):
        
        self.l_surf = []
        self.l_text = []
        self.system.screen.blit(self.mouse, (self.system.mouse_pos[0], self.system.mouse_pos[1]))
        
        #update hp display
        ratio = self.system.player.hp / self.system.player.max_hp
        if ratio > 0.33:
            surf = pygame.transform.scale(self.full_hp, (int(self.full_hp.get_width()*ratio), self.full_hp.get_height()))
        elif ratio > 0.1:
            surf = pygame.transform.scale(self.low_hp, (int(self.full_hp.get_width()*ratio), self.full_hp.get_height()))
        else:
            surf = pygame.transform.scale(self.very_low_hp, (int(self.full_hp.get_width()*ratio), self.full_hp.get_height()))
        self.l_surf.append(surf)
        self.l_text.append(str(int(self.system.player.hp)) + " / " + str(self.system.player.max_hp))
        
        #update energy display
        ratio = self.system.player.energy / self.system.player.max_energy
        surf = pygame.Surface((self.energy.get_width(), self.energy.get_height()))
        surf.blit(self.energy, (0, 0))
        surf.blit(pygame.Surface((self.energy.get_width(), int(self.energy.get_height() * (1-ratio)))), (0,0))
        self.l_surf.append(surf)
        self.l_text.append(str(int(self.system.player.energy)) + " / " + str(self.system.player.max_energy))
        
        #update weapon display
        surf = self.system.player.weapon.icon
        self.l_surf.append(surf)
        if not self.system.player.weapon.output.armor:
            self.l_text.append("Cost : " + str(self.system.player.weapon.output.energy_cost))
        else:
            self.l_text.append("Ammo : " + str(self.system.player.weapon.output.ammunition))
            

        
    def display(self):
        self.hp_display.display(self.system, [self.hp_back, self.l_surf[0]], [self.l_text[0]], [(255,255,255)], [0])
        self.energy_display.display(self.system, [self.energy_back, self.l_surf[1]], [self.l_text[1]], [(150,150,50)], [90])
        self.weapon_display.display(self.system, [self.weapon_back, self.l_surf[2]], [self.l_text[2]], [(255,255,255)], [0])

#=============================================================================#
#=============================================================================#
#=============================================================================#
        
class ShooterMenu():
    
    def __init__(self):
        
        #import all images
        
        
        
        
        
        #create internal display
        return 0
        