# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:00:04 2017

@author: Benoît
"""

path = "data/images/AbilitiesIcons/"

import pygame

class Abilitie():
    
    def __init__(self, name, cooldown, cost, function, icon):
        
        self.user = None
        self.name = name
        self.cooldown = cooldown
        self.cost = cost
        self.function = function
        self.icon = icon
        
        self.last_use = 0
        
        
    def execute(self):
        if self.function != None:
            if self.user.system.time - self.last_use >= self.cooldown and self.user.energy > self.cost:
                self.function()
                self.user.energy -= self.cost
                self.last_use = self.user.system.time
            
            
    def set_user(self, user):
        self.user = user
            
def test():
    pass







abilitie_test = Abilitie("test", 300, 50,  test, pygame.image.load(path + "test.png"))


none_icon = pygame.image.load(path + "None.png")
none_icon.set_colorkey((0,0,0))
abilitie_none = Abilitie("None", 1, 0, None, none_icon)