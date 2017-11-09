# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:23:59 2017

@author: Benoît
"""
import pygame
import random
import Objects
import Math_operations as mtop

path = "data/images/BulletsSprites/"

class Bullet(Objects.Object):
    
    def __init__(self, name, desc, image, speed, armor, mag, power_or_mass, fct = None):
        Objects.Object.__init__(self, name, desc, image, speed)
        
        self.time = 0
        
        self.armor  = armor
        self.mag = mag
        if not self.armor:
            self.power = power_or_mass
        else:
            self.mass = power_or_mass
            
        self.fct = fct
            
        
    def duplicate(self):
        if not self.armor:
            dupli = Bullet(self.name, self.desc, self.image, self.speed, self.armor, self.mag, self.power)
        else:
            dupli = Bullet(self.name, self.desc, self.image, self.speed, self.armor, self.mag, self.mass)
        return dupli
        
        
    def be_attracted(self, attractor, strength):
        dx = attractor.x - self.x
        dy = attractor.y - self.y
        dx, dy = mtop.trig_normalize(dx, dy, strength)
        self.dx += dx
        self.dy += dy
        
    
    def update(self):
        Objects.Object.update(self)
        if self.fct != None:
            self.dx, self.dy = self.fct(self.time)
        self.time += 1
        if self.time > 2000:
            del self
        
#=============================================================================#   
#=============================================================================#
#=============================================================================#
        
class MultiBullet(Bullet):
    
    def __init__(self, name, desc, image, speed, armor, mag, power_or_mass, timer, output, nb_output, l_param, fct = None):
        Bullet.__init__(self, name, desc, image, speed, armor, mag, power_or_mass)
        
        self.timer = timer
        self.output = output
        self.nb_output = nb_output
        self.l_param = l_param #should be like [int = angle of projection, int = angle of dispertion, bool = randomness of repartition, bool = randomness of speed output]
        if self.l_param[1] == 360:
            self.l_param[1] = 360 * (1 - 1/self.nb_output) #avoid to stack 2 bullets on 0° and 360°
            
            
    def update(self):
        if self.timer == self.time:
            self.explode()
            self.kill()
            del self
            return 0
        Bullet.update(self)

    
    def explode(self):
        
        if not self.l_param[2]:
            if self.nb_output > 1:
                small_angle = self.l_param[1] / (self.nb_output - 1)
                starting_angle = mtop.get_angle(self.dx, self.dy) - self.l_param[1] / 2 + self.l_param[0]
            else:
                small_angle = 0
                starting_angle = mtop.get_angle(self.dx, self.dy) + self.l_param[0]
            for i in range(0, self.nb_output):
                shot = self.output.duplicate()
                shot.x = self.x
                shot.y = self.y
                shot.rect = pygame.Rect(shot.x, shot.y, shot.width, shot.height)
                if self.l_param[3]:
                    shot.speed = random.uniform(0.7, 1.1) * shot.speed
                dx, dy = mtop.get_dir(starting_angle + small_angle * i)
                shot.set_dir(dx, dy)
                for grp in self.groups():
                    shot.add(grp)
                
        else:
            starting_angle = mtop.get_angle(self.dx, self.dy) - self.l_param[1] / 2 + self.l_param[0]
            ending_angle = starting_angle + self.l_param[1]
            for i in range(0, self.nb_output):
                shot = self.output.duplicate()
                shot.x = self.x
                shot.y = self.y
                shot.rect = pygame.Rect(shot.x, shot.y, shot.width, shot.height)
                if self.l_param[3]:
                    shot.speed = random.uniform(0.7, 1.1) * shot.speed
                dx, dy = mtop.get_dir(random.randint(int(starting_angle), int(ending_angle)))
                shot.set_dir(dx, dy)
                for grp in self.groups():
                    shot.add(grp)


    def duplicate(self):
        if not self.armor: 
            dupli = MultiBullet(self.name, self.desc, self.image, self.speed, self.armor, self.mag, self.power, self.timer, self.output, self.nb_output, self.l_param) 
        else: 
            dupli = MultiBullet(self.name, self.desc, self.image, self.speed, self.armor, self.mag, self.mass, self.timer, self.output, self.nb_output, self.l_param) 
        return dupli
                    
        
#=============================================================================#   
#=============================================================================#
#=============================================================================#      
        
#Bullet Sprite
        
    #Armored Bullets
s_simple_bullet = pygame.image.load(path + "bullet2.png")

    #Energetic bullets
s_yellow_plasma = pygame.image.load(path + "plasma1.png")
s_red_plasma = pygame.image.load(path + "plasma2.png")

#=============================================================================#
#=============================================================================#
#=============================================================================#

#Bullet Definition

    #Armored Bullets
t1_bullet = Bullet("t1_bullet", "", s_simple_bullet, 15, 1, True, 0.05)
t1_sniper_bullet = Bullet("t1_sniper_bullet", "", s_simple_bullet, 35, 1, True, 0.3)
t1_shotgun_bullet = MultiBullet("t1_shotgun_bullet", "", s_simple_bullet, 20, 1, True, 0.2, 2, t1_bullet, 8, [0, 30, True, True])

    #Energetic Bullets
t1_plasma = Bullet("t1_plasma", "", s_yellow_plasma, 7, False, False, 10)
t1_double_plasma = MultiBullet("t1_double_plasma", "", s_yellow_plasma, 1, False, False, 0, 0, t1_plasma, 2, [0, 30, False, False])
t1_triple_plasma = MultiBullet("t1_triple_plasma", "", s_yellow_plasma, 1, False, False, 0, 0, t1_plasma, 3, [0, 45, False, False])
t1_quad_plasma = MultiBullet("t1_quad_plasma", "", s_yellow_plasma, 1, False, False, 0, 0, t1_plasma, 4, [0, 60, False, False])
t1_penta_plasma = MultiBullet("t1_penta_plasma", "", s_yellow_plasma, 1, False, False, 0, 0, t1_plasma, 5, [0, 75, False, False])

t1_exploding_plasma = MultiBullet("t1_exploding_plasma", "", s_red_plasma, 5, False, False, 30, 150, t1_plasma, 9, [0, 360, False, False])
t1_exploding_double_plasma = MultiBullet("t1_exploding_double_plasma", "", s_red_plasma, 5, False, False, 30, 150, t1_double_plasma, 9, [0, 360, False, False])











simple_bullet = Bullet("simple bullet", "a bullet", s_simple_bullet, 10, 10, True, 1)

snipe = Bullet("simple bullet", "a bullet", s_simple_bullet, 50, 10, True, 1)
simple_plasma = Bullet("simple plasma", "a plasma", s_yellow_plasma, 15, False, False, 50)
shotgun = MultiBullet("simple plasma", "a plasma", s_simple_bullet, 10, 10, True, 10, 5, simple_bullet, 10, [0, 20, True, True])

#simple_multi_plasma = MultiBullet(None, ["simple plasma", "a plasma", s_simple_plasma, False, False, 50, 30, 40, simple_plasma, 4, [0, 180, False, False]])
#simple_multi_plasma2 = MultiBullet(None, ["simple plasma", "a plasma", s_simple_plasma, False, False, 50, 30, 40, simple_multi_plasma, 2, [0, 180, False, False]])
#simple_multi_plasma3 = MultiBullet(None, ["simple plasma", "a plasma", s_simple_plasma, False, False, 50, 30, 0, simple_multi_plasma2, 8, [0, 360, False, False]])

shotgun_bullet = MultiBullet("simple plasma", "a plasma", s_simple_bullet, 5, 10, True, 10, 5, simple_bullet, 20, [0, 40, True, True])