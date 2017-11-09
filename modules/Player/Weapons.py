# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 21:49:22 2017

@author: Benoît
"""

import pygame

path = "data/images/WeaponsIcons/"

class Weapon():
    """A class for weapons item, containing their stats and icon, and the methods
    they use to shoot"""
    
    def __init__(self, l_spec):
        
        self.user = None #note taht the weapon is created with no owner, you'll have to give it one in order to use it
        self.output = None #note that the weapon is initialized without bullet, you MUST call install() on it before using it (see below)
        
        
        self.frequency = l_spec[0] #it is not really a frequency but rather a period : the number of frames between each shot (starting at 0)
        self.launch_speed = l_spec[1]
        self.last_shot_time = 0

        self.icon = l_spec[2]
        
    
    def duplicate(self):
        """should be called everytime that you want to create a new weapon identical
        to another, since using = only create reference"""
        
        return Weapon([self.frequency, self.launch_speed, self.icon])

        
    
    def shoot_bullet(self):
        """shoot the bullet assigned to the weapon according to the vector (dx, dy),
        used on ammunition-based bullets"""
        
        time = self.user.system.time
        if time - self.last_shot_time > self.frequency and self.output.ammunition > 0:
            self.last_shot_time = time
            self.output.ammunition -= 1
            
            shot = self.output.duplicate()
            shot.x = self.user.weapon_pos[0]
            shot.y = self.user.weapon_pos[1]
            shot.go_to(self.user.system.mouse_pos)
            
            if self.user == self.user.system.player:
                shot.add(self.user.system.obj_bullet)
            else:
                shot.add(self.user.system.obj_enemy_bullet)
            if shot.mag:
                shot.add(self.user.system.obj_mag)
                    
    
    def shoot_plasma(self):
        """shoot the bullet assigned to the weapon according to the vector (dx, dy),
        used on energy-based bullets"""
        
        time = self.user.system.time
        if time - self.last_shot_time > self.frequency and self.user.energy > self.output.energy_cost:
            self.last_shot_time = time
            self.user.energy -= self.output.energy_cost
            
            shot = self.output.duplicate()
            shot.x = self.user.weapon_pos[0]
            shot.y = self.user.weapon_pos[1]
            shot.go_to(self.user.system.mouse_pos)
            
            if self.user == self.user.system.player:
                shot.add(self.user.system.obj_bullet)
            else:
                shot.add(self.user.system.obj_enemy_bullet)
            if shot.mag:
                shot.add(self.user.system.obj_mag)
                
                
    def install(self, sys, shot):
        """MUST be called before weapon usage, set the projectile the weapon use"""
        
        self.output = shot #Bullet type
        self.output.system = sys
        self.output.speed = self.launch_speed
        if not self.output.armor: #energy bullet have no armor
            self.shoot = self.shoot_plasma
        else:
            self.shoot = self.shoot_bullet
            
#=============================================================================#
#=============================================================================#
#=============================================================================#
                     

"""Available Weapons"""
crappy_gun_icon = pygame.image.load(path  + "crappy_gun.png")
crappy_plasma_icon = pygame.image.load(path + "crappy_plasma.png")

crappy_gun = Weapon([8, 12,  crappy_gun_icon])
crappy_plasma = Weapon([10, 5, crappy_plasma_icon])