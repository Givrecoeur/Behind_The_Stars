# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:59:30 2017

@author: Benoît
"""

import Asteroid
import Enemies
import Boss
import random
import CstSystem as csts

class Spawn():
    
    def __init__(self, sys, start_time):
        self.system = sys
        self.start_time = start_time

        
    def update(self):
        if self.system.time == self.start_time:
            self.execute()
    
    def execute(self):
        return None
        
        
        
class Asteroid_spawn(Spawn):
    
    def __init__(self, sys, start_time, asteroid_type, nb, direction):
    
        Spawn.__init__(self, sys, start_time)
        self.asteroid_type = asteroid_type
        self.nb_asteroid = nb
        self.direction = direction
        

    def execute(self):

        dx = self.direction[0]
        dy = self.direction[1]
        
        for k in range(0, self.nb_asteroid):
            asteroid = Asteroid.Asteroid(self.system, self.asteroid_type, dx, dy)
            
            if dx == 0:
                asteroid.x = random.randint(0, csts.SCREEN_WIDTH - asteroid.width)
            elif dx > 0:
                asteroid.x = random.randint(-csts.SCREEN_WIDTH, 0 - asteroid.width)
            else:
                asteroid.x = random.randint(csts.SCREEN_WIDTH, 2 * csts.SCREEN_WIDTH - asteroid.width)
                
            if dy == 0:
                asteroid.y = random.randint(0, csts.SCREEN_HEIGHT - asteroid.height)
            elif dy > 0:
                asteroid.y = random.randint(-csts.SCREEN_HEIGHT, 0 - - asteroid.height)
            else:
                asteroid.y = random.randint(csts.SCREEN_HEIGHT, 2 * csts.SCREEN_HEIGHT - asteroid.height)
                
            self.system.obj_neutral.add(asteroid)
            
            if asteroid.mag:
                self.system.obj_mag.add(asteroid)
                
                
    
class Enemy_spawn(Spawn):
    
    def __init__(self, sys, start_time, l_enemy, l_pos):
        
        Spawn.__init__(self, sys, start_time)
        self.l_enemy = l_enemy
        self.l_pos = l_pos
        
        
    def execute(self):
        
        for i in range(0, len(self.l_enemy)):
            self.l_enemy[i] = self.l_enemy[i].duplicate()
            self.l_enemy[i].set_system(self.system)
            self.l_enemy[i].x = self.l_pos[i][0]
            self.l_enemy[i].y = self.l_pos[i][1]
                

class Boss_spawn(Spawn):
    
    def __init__(self, sys, l_spec):
        
        Spawn.__init__(self, sys, l_spec)
        self.boss = Boss.Very_First_Boss(self.system, l_spec[1])
        
    def execute(self):
        self.system.obj_enemy.add(self.boss)
        self.system.boss = self.boss

            
                
                
                
            
