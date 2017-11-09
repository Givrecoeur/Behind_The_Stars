# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 02:39:34 2017

@author: Benoît
"""

import pygame
import CstPlayer as cstp
import CstSystem as csts
import Objects
import Math_operations as mtop


path = "data/images/PlayerSprites/"

class Player(Objects.Solid_Object):
    """The user-controlled object class, contain all method and attribute that 
    allow it to interact with the rest of the code"""
    
    def __init__(self, sys):
        Objects.Solid_Object.__init__(self, "Player", "It's you, dummy", pygame.image.load(path + cstp.PLAYER_SPRITE), cstp.PLAYER_SPEED, cstp.PLAYER_HEALTH, cstp.PLAYER_ARMOR)
        
        self.vx = 0
        self.vy = 0
        self.dx = 0
        self.dy = 0
        
        self.max_hp = cstp.PLAYER_MAX_HEALTH
        self.max_energy = cstp.PLAYER_MAX_ENERGY
        self.energy = self.max_energy
        self.energy_regen = cstp.PLAYER_ENERGY_REGEN
        self.max_shield = cstp.PLAYER_MAX_SHIELD
        self.shield = self.max_shield
        
        self.l_weapon = cstp.PLAYER_WEAPONS
        self.l_bullet = cstp.PLAYER_BULLETS
        
        for i in range(0, len(self.l_weapon)):
            self.l_weapon[i].user = self
            self.l_weapon[i].install(self.system, self.l_bullet[i])
        self.weapon = self.l_weapon[0]
        self.num_weapon = 0
        self.weapon_pos = (0, 0)
        
        self.abilitie_1 = cstp.PLAYER_ABILITIE_1
        self.abilitie_1.set_user(self)
        self.abilitie_2 = cstp.PLAYER_ABILITIE_2
        self.abilitie_2.set_user(self)
        
        self.shooting = False
        
        #self.image = pygame.transform.scale(self.image, (50,50))
        #self.width = self.image.get_width()
        #self.shield_icon = pygame.image.load("shield.png")
        #self.shield_icon = pygame.transform.scale(self.shield_icon, (int(self.width*2), int(self.width*2)))
        #self.shield_icon.set_alpha(175)
        #self.shield = Objects.Object(self.system, ["shielf", "shield", self.shield_icon])
        #self.system.obj_neutral.add(self.shield)
    
    def set_system(self, sys):
        self.system = sys
        sys.obj_player.add(self)
        
        
    def update(self):
        
        self.manage_speed()
        self.x += self.dx
        self.y += self.dy
        
        #self.shield.x = self.x -85
        #self.shield.y = self.y -85
        
        
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > csts.SCREEN_WIDTH -self.width:
            self.x = csts.SCREEN_WIDTH -self.width
        if self.y > csts.SCREEN_HEIGHT -self.height:
            self.y = csts.SCREEN_HEIGHT -self.height
            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.dx = 0
        self.dy = 0
        self.weapon_pos = (self.x + 13, self.y + 0)
        
        self.energy += self.energy_regen
        if self.energy > self.max_energy:
            self.energy = self.max_energy
        
        if self.hp <= 0:
            self.kill()
        
        if self.shooting:
            self.shoot()
        
        
    def set_speed(self, vx, vy):
        self.vx = vx
        self.vy = vy
        
        
    def add_speed(self, ax, ay):
        self.vx += ax
        self.vy += ay
        
        
    def manage_speed(self):
        self.dx, self.dy = mtop.trig_normalize(self.vx, self.vy, self.speed)
        
        
    def shoot(self):
        self.weapon.shoot()
        
        
    def next_weapon(self):
        self.num_weapon += 1
        self.weapon = self.l_weapon[(self.num_weapon) % (len(self.l_weapon))]

    
    def previous_weapon(self):
        self.num_weapon -= 1
        self.weapon = self.l_weapon[(self.num_weapon) % (len(self.l_weapon))]
        
        
    def use_abilitie_1(self):
        self.abilitie_1.execute()

        
        
    def use_abilitie_2(self):
        self.abilitie_2.execute()