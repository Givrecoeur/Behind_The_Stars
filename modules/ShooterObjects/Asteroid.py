# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:18:05 2017

@author: Benoît
"""

import Objects
import Math_operations as mtop
import pygame

path = "data/images/AsteroidSprites/"

class Asteroid(Objects.Solid_Object):
    
    def __init__(self, sys, l_spec, dx, dy):
        Objects.Solid_Object.__init__(self, sys, l_spec)
        
        self.loot = l_spec[7]
            
        self.dx = dx
        self.dy = dy 
        self.dx, self.dy = mtop.trig_normalize(self.dx, self.dy, self.speed)
            
    
    def manage_speed(self):
        return 0
        
#=============================================================================#   
#=============================================================================#
#=============================================================================#

s_small_asteroid1 = pygame.image.load(path + "small_asteroid1.png")