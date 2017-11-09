import random
import pygame
import Objects
import Bullets
import Math_operations as mtop

path = "data/images/BossSprites/"

class Boss(Objects.Solid_Object):

    def __init__(self, sys, l_spec):
        Objects.Solid_Object.__init__(self, sys, l_spec)
        self.max_hp = self.hp
        
        self.time = 0
        self.action = None
        
    def go_to(self, x, y):
        if mtop.distance(self.x, self.y, x, y) > self.speed:
            self.dx = x - self.x
            self.dy = y - self.y
            self.dx, self.dy = mtop.trig_normalize(self.dx, self.dy, self.speed)
        else:
            self.dx = 0
            self.dy = 0
            self.action = None
            
        
    def take_action(self):
        return 0
    
    
    def chose_action(self):
        return 0
    
    def update(self):
        if self.action == None:
            self.chose_action()
        if self.action != None:
            self.action()
        Objects.Solid_Object.update(self)
        
#=============================================================================#   
#=============================================================================#
#=============================================================================#
        
class Very_First_Boss(Boss):
    
    def __init__(self, sys, l_spec):
        Boss.__init__(self, sys, l_spec)
        
        self.x = 810
        self.y = -500
        
        #Subammo
        self.subammoend = Bullets.Bullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30])
        
        self.subammo2_zone = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 30, self.subammoend, 5, [180, 10, True, True]])
        self.subammo1_zone = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 30, self.subammo2_zone, 5, [180, 10, False, False]])

        self.subammo2_maxi_zone = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 25, self.subammoend, 7, [180, 10, True, True]])
        self.subammo1_maxi_zone = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 25, self.subammo2_maxi_zone, 5, [180, 10, False, False]])

        self.subammo_focus = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 20, self.subammoend, 3, [0, 35, False, False]])
        self.subammo_harder_focus = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 25, self.subammoend, 10, [0, 180, True, True]])
        
        #Ammo
        self.charge1 = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 10, self.subammoend, 18, [0, 25, True, True]])
        self.charge1.speed = 14     
        self.charge2 = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 0, self.subammoend, 10, [0, 360, False, False]])
        self.charge2.speed = 2
        
        self.zone = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 0, self.subammo1_zone, 12, [0, 135, False, False]])
        self.zone.speed = 5
        self.focus = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 0, self.subammo_focus, 3, [0, 15, False, False]])
        self.focus.speed = 18
        
        self.maxi_zone = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 0, self.subammo1_maxi_zone, 12, [0, 135, False, False]])
        self.maxi_zone.speed = 7
        self.harder_focus = Bullets.MultiBullet(self.system, ["simple plasma", "a plasma", Bullets.s_boss_plasma, False, False, 50, 30, 0, self.subammo_harder_focus, 3, [0, 15, False, False]])
        self.harder_focus.speed = 18
       
        
    def chose_action(self):
        self.time = 0
        
        if self.y < 0:
            self.action = self.go_to_center
            
        elif self.hp / self.max_hp >= 0.5:
            rand = random.randint(1, 4)
            if rand == 1:
                self.action = self.zone_attack
            elif rand == 2:
                self.action = self.focus_attack
            else:
                self.action = self.charge_attack
            
        else:
            rand = random.randint(1, 4)
            if rand == 1:
                self.action = self.harder_focus_attack
            elif rand == 2 or rand == 3:
                self.action = self.maxi_zone_attack
            else:
                self.action = self.charge_attack
        
        
    def go_to_center(self):
        self.go_to(810, 390)
        
        
    def zone_attack(self):
        if self.time < 101:
            if self.time%100 ==0:
                randx = random.random() *2 -1
                randy = random.random() *2 -1
                
                shot = self.zone.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(randx, randy)
                self.system.obj_enemy_bullet.add(shot)
                
                shot = self.zone.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(-randx, -randy)
                self.system.obj_enemy_bullet.add(shot)
            self.time += 1
        elif self.time >= 101 and self.time < 300:
            self.time += 1
        else:
            self.action = None
            self.time = 0
        
        
    def focus_attack(self):
        if self.time < 300:
            if self.time%30 ==0:
                shot = self.focus.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(self.system.player.rect.centerx -self.rect.centerx, self.system.player.rect.centery - self.rect.centery)
                self.system.obj_enemy_bullet.add(shot)
            self.time += 1
        elif self.time >= 300 and self.time < 400:
            self.time += 1
        else:
            self.action = None
            self.time = 0
            
        
    def charge_attack(self):
        if self.time == 0:
            self.speed = 2*self.speed
            self.time += 1
        elif self.time < 180:
            self.dx = self.system.player.rect.centerx - self.rect.centerx
            self.dy = self.system.player.rect.centery - self.rect.centery
            self.dx, self.dy = mtop.trig_normalize(self.dx, self.dy, self.speed)
            if self.time%20 == 0:
                shot = self.charge1.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(self.system.player.rect.centerx -self.rect.centerx, self.system.player.rect.centery - self.rect.centery)
                self.system.obj_enemy_bullet.add(shot)
            if self.time%40 == 0:
                shot = self.charge2.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(self.system.player.rect.centerx -self.rect.centerx, self.system.player.rect.centery - self.rect.centery)
                self.system.obj_enemy_bullet.add(shot)
            
            self.time += 1
        else:
            self.speed = self.speed / 2
            self.dx = 0
            self.dy = 0
            self.time = 0
            self.action = None
        
        
    def harder_focus_attack(self):
        if self.time < 180:
            if self.time%15 == 0:
                shot = self.harder_focus.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(self.system.player.rect.centerx -self.rect.centerx, self.system.player.rect.centery - self.rect.centery)
                self.system.obj_enemy_bullet.add(shot)
            self.time += 1
        elif self.time >= 180 and self.time < 240:
            self.time += 1
        else:
            self.action = None
            self.time = 0
        
        
    def maxi_zone_attack(self):
        if self.time < 181:
            if self.time%90 ==0:
                randx = random.random() *2 -1
                randy = random.random() *2 -1
                
                shot = self.maxi_zone.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(randx, randy)
                self.system.obj_enemy_bullet.add(shot)
                
                shot = self.maxi_zone.duplicate()
                shot.x = self.x + self.width / 2
                shot.y = self.y + self.height / 2
                shot.set_dir(-randx, -randy)
                self.system.obj_enemy_bullet.add(shot)
            self.time += 1
        elif self.time >= 181 and self.time < 320:
            self.time += 1
        else:
            self.action = None
            self.time = 0
        
#=============================================================================#   
#=============================================================================#
#=============================================================================#        
        
s_boss = pygame.image.load(path + "boss1.png")