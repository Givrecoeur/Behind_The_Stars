# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:32:49 2017

@author: Benoît
"""

import Objects
import pygame
import Math_operations as mtop

path = "data/images/BulletsSprites/"

class Mine(Objects.Solid_Object):
    
    def __init__(self, sys, l_spec):
        Objects.Solid_Object.__init__(self, sys, l_spec)
        
        self.radius = l_spec[7]
        self.delay = l_spec[8]
        self.explosion = l_spec[9]
        
        if type(self.explosion) == int:
            self.explode = self.dmg_explosion
            self.explosion_radius = l_spec[10]
        else:
            self.explode = self.bullet_explosion
            self.bullet = l_spec[10][0]
            self.bullet.speed = l_spec[10][1]
            
        self.time = 0
        
    
    def duplicate(self):
        if type(self.explosion) == int:
            return Mine(self.system, [self.name, self.desc, self.image, self.hp, self.armor, self.speed, self.mag, self.radius, self.delay, self.explosion, self.explosion_radius])
        else:
            return Mine(self.system, [self.name, self.desc, self.image, self.hp, self.armor, self.speed, self.mag, self.radius, self.delay, self.explosion, (self.bullet, self.bullet.speed)])

    
    def dmg_explosion(self):
        if self.time < self.delay:
            self.time += 1
        else:
            if abs(mtop.distance(self.rect.centerx, self.rect.centery, self.system.player.rect.centerx, self.system.player.rect.centery)) <= self.explosion_radius:
                self.system.player.hp -= self.dmg_explosion
                
    
    def bullet_explosion(self):
        if self.time < self.delay:
            self.time += 1
        else:
            shot = self.bullet.duplicate()
            shot.x = self.x
            shot.y = self.y
            shot.set_dir(1,0)
            self.system.obj_enemy_bullet.add(shot)
                