# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:51:55 2017

@author: Benoît
"""

import pygame
import CstSystem as csts
import Math_operations as mtop


#=============================================================================#
#=============================================================================#
#=============================================================================#

class Object(pygame.sprite.Sprite):
    """abstract class, to be used by its sons. Contain basic method and attribute
    for Objects movable and visible on screen, such as asteroid, enemies, player..."""
    
    def __init__(self, name, desc, image, speed):
        super().__init__()
        self.system = None
        self.out = True #memorize if the object has already been visible on screen
        self.stay_in_screen = False #tell if the object must or not stay on screen after its arrival on it
        
        self.x = 0
        self.y = 0
        
        self.dx = 0
        self.dy = 0        
        
        self.name = name
        self.desc = desc 
        self.image = image
        self.speed = speed
        self.image.set_colorkey((0,0,0))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


        
    def update(self):
        
        self.x += self.dx
        self.y += self.dy
        
        if self.stay_in_screen and not self.out:
            if self.x < 0:
                self.x = 0
            if self.y < 0:
                self.y = 0
            if self.x > csts.SCREEN_WIDTH -self.width:
                self.x = csts.SCREEN_WIDTH -self.width
            if self.y > csts.SCREEN_HEIGHT -self.height:
                self.y = csts.SCREEN_HEIGHT -self.height
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        if self.out:        
            if self.rect.x < -csts.SCREEN_WIDTH or self.rect.x > csts.SCREEN_WIDTH*2:
                self.kill()
                del self
            elif self.rect.y < -csts.SCREEN_HEIGHT or self.rect.y > csts.SCREEN_HEIGHT*2:
                self.kill()
                del self
            elif self.rect.x > 0 - self.width and self.rect.x < csts.SCREEN_WIDTH and self.rect.y > 0 - self.height and self.rect.y < csts.SCREEN_HEIGHT:
                self.out = False
        else:
            if self.rect.x < 0 - self.width or self.rect.x > self.rect.x < csts.SCREEN_WIDTH:
                self.kill()
                del self
            elif self.rect.y < 0 - self.height or self.rect.y > csts.SCREEN_HEIGHT:
                self.kill()
                del self
                
                
    def vect_dist(self, other):
        return other.x - self.x, other.y - self.y
                
                
    def move_to(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        
    def set_dir(self, dx, dy):
        self.dx = dx
        self.dy = dy
        self.dx, self.dy = mtop.trig_normalize(self.dx, self.dy, self.speed)

        
    def go_to(self, pos):
        self.dx = pos[0] - self.x
        self.dy = pos[1] - self.y
        self.dx, self.dy = mtop.trig_normalize(self.dx, self.dy, self.speed)
        
        
    def stop(self):
        self.dx = 0
        self.dy = 0
        
        
    def actual_speed(self):
        """should be called if the object has been affected by speed modificators"""
        return mtop.length(self.dx, self.dy)

        
#=============================================================================#
#=============================================================================#
#=============================================================================#

class Solid_Object(Object):
    """abstract class based on Object, add new method and attribute to object that 
    be your "units" in the game"""
    
    def __init__(self, name, desc, image, speed, hp, armor):
        Object.__init__(self, name, desc, image, speed)

        self.hp = hp
        self.armor = armor
        
    
    def take_dammage(self, projectile):
        if not projectile.armor:
            self.hp -= projectile.power
            return None
        else:
            diff_armor = self.armor - projectile.armor
            damage = 0.5 * projectile.mass * (projectile.actual_speed())**2
            if diff_armor < 0:
                self.hp -= damage * 2
                return True
            else:
                self.hp -= damage / (2**diff_armor)
                return False
        if self.hp < 0:
            self.hp = 0
        
                
    def update(self):
        Object.update(self)
        if self.hp <= 0:
            self.kill()
            
            
    def collide(self, other): 
        diff_armor = self.armor - other.armor
        if diff_armor <= 0:
            self.hp -= other.hp
            other.hp -= self.hp/(1.1**(-diff_armor))
        else:
            self.hp -= other.hp/(1.1**diff_armor)
            other.hp -= self.hp
            
            
#=============================================================================#
#=============================================================================#
#=============================================================================# 
        

        
#=============================================================================#
#=============================================================================#
#=============================================================================#
        