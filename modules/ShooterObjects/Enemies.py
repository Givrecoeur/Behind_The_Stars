# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:25:51 2017

@author: Benoît
"""

import pygame
import random
import Objects
import Bullets
import Math_operations as mtop

import CstSystem as csts

path = "data/images/EnemiesSprites/"

class Enemy(Objects.Solid_Object):
    
    def __init__(self, name, desc, image, speed, hp, armor, shot, behavior_fct, loot):
        Objects.Solid_Object.__init__(self, name, desc, image, speed, hp, armor)
        self.stay_in_screen = True
        self.aim = None
        
        self.loot = loot

        self.shot = shot.duplicate()
        
        self.behavior_fct = behavior_fct
        self.time = 0
        self.last_action_time = 0
        self.action = []
        
        
    def set_system(self, sys):
        self.system = sys
        self.aim = sys.player
        sys.obj_enemy.add(self)
        
        
    def duplicate(self):
        return Enemy(self.name, self.desc, self.image, self.speed, self.hp, self.armor, self.shot, self.behavior_fct, self.loot)
        
    
    def update(self):
        if self.action == []:
            if self.out:
                self.action = [(self.get_in_screen, 20)]
            else:
                self.behavior_fct(self)
        self.act()
        
        Objects.Solid_Object.update(self)
        self.time += 1
        
    
    def act(self):
        
        if self.action[0][1] < self.time - self.last_action_time:
            self.stop()
            self.last_action_time = self.time
            del self.action[0]
        
        else:
            self.action[0][0]()
        
        
    #Action functions
        
    def be_idle(self):
        pass
    
    
    def get_in_screen(self):
        self.go_to((csts.SCREEN_WIDTH//2, csts.SCREEN_HEIGHT//2))
    
    
    def shoot(self):
        bullet = self.shot.duplicate()
        bullet.x = self.x + self.width//2
        bullet.y = self.y + self.height//2
        bullet.go_to((self.aim.x + self.aim.width//2, self.aim.y + self.aim.height//2))
        bullet.system = self.system
        self.system.obj_enemy_bullet.add(bullet)
        
        
    def go_in(self):
        dx, dy = self.vect_dist(self.aim)
        self.dx, self.dy = mtop.trig_normalize(dx, dy, self.speed)
    
    
    def back_off(self):
        dx, dy = self.vect_dist(self.aim)
        dx = -dx
        dy = -dy
        self.dx, self.dy = mtop.trig_normalize(dx, dy, self.speed)
    
    
    def dodge_trig(self):
        dx, dy = self.vect_dist(self.aim)
        temp = dx
        dx = dy
        dy = -temp
        self.dx, self.dy = mtop.trig_normalize(dx, dy, self.speed)
    
    
    def dodge_antitrig(self):
        dx, dy = self.vect_dist(self.aim)
        temp = dx
        dx = -dy
        dy = temp
        self.dx, self.dy = mtop.trig_normalize(dx, dy, self.speed)
    
    
    #Behavior functions
    
    def f_long_range_very_slow(self):
        
        aim_dist = mtop.distance(self.x, self.y, self.aim.x, self.aim.y)
        
        if aim_dist > 450:
            choice = random.randint(1, 4)
            if choice == 4:
                time = random.randint(60, 120)
                trig = random.randint(0, 1)
                if trig == 1:
                    self.action = [(self.dodge_trig, time), (self.be_idle, 30)]
                else:
                    self.action = [(self.dodge_antitrig, time), (self.be_idle, 30)]
            else:
                self.action = [(self.be_idle, 180),(self.shoot, 1), (self.be_idle, 30)]
                
        else:
            choice = random.randint(1, 5)
            if choice == 1:
                self.action = [(self.be_idle, 30), (self.shoot, 1), (self.be_idle, 30)]
            elif choice == 2:
                time = random.randint(60, 120)
                trig = random.randint(0, 1)
                if trig == 1:
                    self.action = [(self.dodge_trig, time), (self.be_idle, 30)]
                else:
                    self.action = [(self.dodge_antitrig, time), (self.be_idle, 30)]
            else:
                time = random.randint(60, 120)
                self.action = [(self.back_off, time)]
            
    
    def f_medium_range_quick(self):
        
        aim_dist = mtop.distance(self.x, self.y, self.aim.x, self.aim.y)
        
        if aim_dist > 500:
            self.action = [(self.go_in, 20)]
            
        elif aim_dist < 200:
            self.action = [(self.back_off, 29), (self.shoot, 1)]
                
        else:
            choice = random.randint(1, 4)
            if choice == 1:
                self.action = [(self.dodge_trig, 44), (self.shoot, 1)] * random.randint(1, 3)
            elif choice == 4:
                self.action = [(self.dodge_antitrig, 44), (self.shoot, 1)] * random.randint(1, 3)
            else:
                self.action = [(self.be_idle, 29), (self.shoot, 1)] * random.randint(5, 10)
    
    
    def f_close_range_slow(self):
        
        aim_dist = mtop.distance(self.x, self.y, self.aim.x, self.aim.y)
        
        if aim_dist > 300:
            self.action = [(self.go_in, 20)]
            
        else:
            choice = random.randint(1, 4)
            if choice == 1:
                self.action = [(self.dodge_trig, 29)]
            elif choice == 4:
                self.action = [(self.dodge_antitrig, 29)]
            else:
                self.action = [(self.be_idle, 59), (self.shoot, 1)]


#=============================================================================#
#=============================================================================#
#=============================================================================#

#Ennemies Sprite

s_enemy1 = pygame.image.load(path + "enemy1.png")
s_enemy2 = pygame.image.load(path + "enemy2.png")
s_enemy3 = pygame.image.load(path + "enemy3.png")
       
#=============================================================================#
#=============================================================================#
#=============================================================================#

#Ennemies
       
E_basic_sniper = Enemy("Basic Sniper", "", s_enemy1, 4, 100, 5, Bullets.t1_sniper_bullet, Enemy.f_long_range_very_slow, "")
E_basic_gunner = Enemy("Basic Gunner", "", s_enemy2, 4, 100, 5, Bullets.t1_plasma, Enemy.f_medium_range_quick, "")
E_basic_shotguner = Enemy("Basic Sniper", "", s_enemy3, 4, 100, 5, Bullets.t1_shotgun_bullet, Enemy.f_close_range_slow, "")
