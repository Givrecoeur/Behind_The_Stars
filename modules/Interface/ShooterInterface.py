# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 09:25:51 2017

@author: Benoît
"""

import CstSystem as csts
import pygame
import InterfaceElements as IE

path = "data/images/MenuShooter/"


class MainWindow(IE.Window):
    
    def __init__(self, sys):
        
        IE.Window.__init__(self, None, 0, 0, csts.SCREEN_WIDTH, csts.SCREEN_HEIGHT, sys.image, sys)
        pygame.mouse.set_visible(False)
        
        PlayerStats(self)
        PlayerWeapons(self)
        PlayerAbilities(self)
        
        self.menu = ShooterMenu(self)
        
        self.mouse = pygame.image.load(path + "MouseShooter.png")
        self.mouse.set_colorkey((0,0,0))
        

    def display(self, surf):
        IE.Window.display(self, surf)
        self.image.blit(self.mouse, self.system.mouse_pos)
        
        
    def open_menu(self):
        
        pygame.mouse.set_visible(True)
        self.system.main_window = self.menu



class PlayerStats(IE.Window):
    
    def __init__(self, motherWin):
        
        self.full_hp = pygame.image.load(path + "HpFull.png")
        self.low_hp = pygame.image.load(path + "HpLow.png")
        self.very_low_hp = pygame.image.load(path + "HpVeryLow.png")
        
        self.shield = pygame.image.load(path + "Shield.png")
        self.shield.set_alpha(110)
        
        self.energy = pygame.image.load(path + "Energy.png")
        
        self.background = pygame.image.load(path + "StatsBack.png")
        self.background.set_colorkey((0,0,0))
        width = self.background.get_width()
        height = self.background.get_height()
        
        image = pygame.Surface((width, height))
        image.set_colorkey((0,0,0))
        image.set_alpha(200)
        IE.Window.__init__(self, motherWin, 50, 50, width, height, image)        
        
    
    def display(self, surf):
        self.update()
        surf.blit(self.image, (self.x, self.y))
    
    
    def update(self):
        
        self.image.fill((0,0,0))
        self.image.blit(self.background, (0,0))        
        
        ratio = self.system.player.hp / self.system.player.max_hp
        width = self.full_hp.get_width()
        height = self.full_hp.get_height()
        if ratio > 0.33:
            self.image.blit(self.full_hp, (51, 5), pygame.Rect(0, 0, int(ratio * width), height))
        elif ratio > 0.1:
            self.image.blit(self.low_hp, (51, 5), pygame.Rect(0, 0, int(ratio * width), height))
        else:
            self.image.blit(self.very_low_hp, (51, 5), pygame.Rect(0, 0, int(ratio * width), height))
    
        ratio = self.system.player.shield / self.system.player.max_shield
        self.image.blit(self.shield, (51, 5), pygame.Rect(0, 0, int(ratio * width), height))
        
        ratio = self.system.player.energy / self.system.player.max_energy
        width = self.energy.get_width()
        height = self.energy.get_height()
        self.image.blit(self.energy, (86, 40), pygame.Rect(0, 0, int(ratio * width), height))
        
        self.write((170, 8), str(int(self.system.player.hp)) + " / " + str(self.system.player.max_hp), (255,255,255))
        self.write((170, 20), "( " + str(int(self.system.player.shield)) + " / " + str(self.system.player.max_shield) + " )", (255,255,255))
        self.write((190, 50), str(int(self.system.player.energy)) + " / " + str(self.system.player.max_energy), (255,255,255))
    
    
class PlayerWeapons(IE.Window):
    
    def __init__(self, motherWin):
        
        self.background = pygame.image.load(path + "WeaponBack.png")
        width = self.background.get_width()
        height = self.background.get_height()
        
        image = pygame.Surface((width, height))
        image.set_colorkey((0,0,0))
        image.set_alpha(200)
        IE.Window.__init__(self, motherWin, 50, 180, width, height, image)
    
    
    def display(self, surf):
        self.update()
        surf.blit(self.image, (self.x, self.y))
        
        
    def update(self):
        
        self.image.blit(self.background, (0, 0))
        
        self.image.blit(self.system.player.weapon.icon, (5, 5))
        
        #if not self.system.player.weapon.output.armor:
        #    self.write((18, 32), "Cost : " + str(self.system.player.weapon.output.energy_cost), (255,255,255))
        #else:
        #    self.write((18, 32), "Ammo : " + str(self.system.player.weapon.output.ammunition), (255,255,255))
    
    
    
class PlayerAbilities(IE.Window):
    
    def __init__(self, motherWin):
        self.background = pygame.image.load(path + "AbilitiesBack.png")
        self.background.set_colorkey((0,0,0))
        width = self.background.get_width()
        height = self.background.get_height()
        
        self.cooldown = pygame.image.load(path + "Cooldown.png")
        self.cooldown.set_colorkey((0,0,0))
        self.cooldown.set_alpha(180)
        
        image = pygame.Surface((width, height))
        image.set_colorkey((0,0,0))
        image.set_alpha(200)
        IE.Window.__init__(self, motherWin, 1720, 880, width, height, image)  
        self.set_font(20, True, False)
    
    
    def display(self, surf):
        self.update()
        surf.blit(self.image, (self.x, self.y))
        
        
    def update(self):
        
        self.image.blit(self.background, (0, 0))
        
        ratio = (self.system.time - self.system.player.abilitie_1.last_use) / self.system.player.abilitie_1.cooldown
        if ratio >= 1:
            ratio = 1
        
        self.image.blit(self.system.player.abilitie_1.icon, (95,5))
        self.image.blit(self.cooldown, (95, 5), pygame.Rect((int(ratio * 49) * 75, 0, 75, 75)))
        
        ratio = (self.system.time - self.system.player.abilitie_2.last_use) / self.system.player.abilitie_2.cooldown
        if ratio >= 1:
            ratio = 1
        
        self.image.blit(self.system.player.abilitie_2.icon, (5,95))
        self.image.blit(self.cooldown, (5, 95), pygame.Rect((int(ratio * 49) * 75, 0, 75, 75)))
        
        remaining_time = self.system.player.abilitie_1.cooldown - (self.system.time - self.system.player.abilitie_1.last_use)
        remaining_time /= 60
        if remaining_time >= 1:
            self.write((120, 30), str(int(remaining_time)), (255,255,255))
        if remaining_time > 0:
            self.write((120, 30), str(round(remaining_time, 1)), (255,255,255))
            
        remaining_time = self.system.player.abilitie_2.cooldown - (self.system.time - self.system.player.abilitie_2.last_use)
        remaining_time /= 60
        if remaining_time >= 1:
            self.write((28, 120), str(int(remaining_time)), (255,255,255))
        if remaining_time > 0:
            self.write((28, 120), str(round(remaining_time, 1)), (255,255,255))
            
                        
            
        
            
    
    
    
class ShooterMenu(IE.HostedWindow):
    
    def __init__(self, motherWin):
        
        menu = pygame.image.load(path + "MenuBackground.png")
        width = menu.get_width()
        height = menu.get_height()
        
        IE.InterfaceElement.__init__(self, motherWin, 800, 200, width, height)
        
        self.image = menu
        self.mouse = pygame.image.load(path + "MouseShooter.png")
        
        IE.create_button(self, 850, 250, path, "Unpause", self.system.set_pause)
        IE.create_button(self, 850, 310, path, "Settings", self.open_settings)
        IE.create_button(self, 850, 370, path, "QuitToMenu", "placeholder")
        IE.create_button(self, 850, 430, path, "QuitGame", self.system.quit_game)

        self.host = motherWin
        
        
    def display(self, surf):
        IE.HostedWindow.display(self, surf)
        
        
    def close(self):
        pygame.mouse.set_visible(False)
        IE.HostedWindow.close(self)
        
        
        
    def open_settings(self):
        pass
    