# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:57:28 2017

@author: Benoît
"""

import pygame

import Background
import CstSystem as csts
import CstGame as cstg
import Player
import Input_managment as inp
import InterfaceElements as IE
import ShooterInterface as SI

boss = cstg.very_first_boss


class Shooter_syst():
    
    def __init__(self, screen):
        
        #self.screen = screen
        self.image = pygame.Surface((csts.SCREEN_WIDTH, csts.SCREEN_HEIGHT))
        self.main_window = SI.MainWindow(self)
        self.done = False
        self.pause = False
        
        self.input = inp.InputManagment(self, "shooter", csts.KEYBOARD_INPUT)
        
        #self.interface = Interface.ShooterInterface(self)
        
        self.mouse_pos = (0,0)
        
        self.obj_player = pygame.sprite.Group()
        self.obj_neutral = pygame.sprite.Group()
        self.obj_enemy = pygame.sprite.Group()
        self.obj_bullet = pygame.sprite.Group()
        self.obj_enemy_bullet = pygame.sprite.Group()
        self.obj_mag = pygame.sprite.Group()        
        
        self.background = Background.Background(5, 0.5)
        self.player = Player.Player(self)
        self.player.set_system(self)
        
        
        self.obj_player.add(self.player)
        self.player.x = 900
        self.player.y = 800
        
        
        self.l_events = []
        self.boss = False
        self.time = 0
        
        self.display()
        
        
    def quit_game(self):
        self.done = True
        
        
    def set_pause(self):
        if self.pause:
            self.pause = False
            self.main_window.close()
            self.input = inp.InputManagment(self, "shooter", csts.KEYBOARD_INPUT)
            
        else:
            self.pause = True
            self.main_window.open_menu()
            self.input = inp.InputManagment(self, "menu", csts.KEYBOARD_INPUT)
                                              
                                            
    def manage_events(self):

        for event in self.l_events:
            event.update()
            
            
    def update_nonbullet(self):
        self.player.update()
        self.obj_enemy.update()
        self.obj_neutral.update()
        
        
    def update_bullets(self):
        self.obj_bullet.update()
        self.obj_enemy_bullet.update()
        
    
    def manage_logic(self):
        self.update_nonbullet()
        self.update_bullets()
        
        self.collision_player_bullet()
        self.collision_player_ennemy()
        self.collision_player_neutral()
        self.collision_ennemy_bullet()
        self.collision_neutral_bullet()


    def collision_player_bullet(self):
        player_hit = pygame.sprite.spritecollide(self.player, self.obj_enemy_bullet, False)
        for hit in player_hit:
            test = self.player.take_dammage(hit)
            if self.player.hp < 0:
                self.player.hp = 0 
            if not test:
                hit.kill()
         
         
    def collision_player_ennemy(self):
        player_collision = pygame.sprite.spritecollide(self.player, self.obj_enemy, False)
        for collision in player_collision:
            self.player.collide(collision)
            if self.player.hp < 0:
                self.player.hp = 0 
        
        
    def collision_player_neutral(self):    
        player_collision = pygame.sprite.spritecollide(self.player, self.obj_neutral, False)
        for collision in player_collision:
            self.player.collide(collision)
            if self.player.hp < 0:
                self.player.hp = 0 
            
            
    def collision_ennemy_bullet(self):
        enemy_hit = pygame.sprite.groupcollide(self.obj_enemy, self.obj_bullet, False, False)
        for enemy in enemy_hit.keys():
            for hit in enemy_hit[enemy]:
                test = enemy.take_dammage(hit)
                if not test:
                    hit.kill()
                    
                    
    def collision_neutral_bullet(self):
        neutral_hit = pygame.sprite.groupcollide(self.obj_neutral, self.obj_bullet, False, False)
        for neutral in neutral_hit.keys():
            for hit in neutral_hit[neutral]:
                test = neutral.take_dammage(hit)
                if not test:
                    hit.kill()            
    
        
    def display(self):
        
        self.image.blit(self.background.sky, (0,0), self.background.update_sky_rect()) 
        self.obj_bullet.draw(self.image)
        self.obj_enemy_bullet.draw(self.image) 
        self.obj_neutral.draw(self.image)
        self.obj_enemy.draw(self.image)
        self.obj_player.draw(self.image)
        #self.interface.update()
        #self.interface.display()
        
        
    def run(self):
        self.input.manage_function()

        if not self.pause:
            self.manage_logic()
            self.display()
            self.manage_events()
            self.time += 1
            
        self.main_window.display(self.image)
        return self.image

        
        
        
        
        
        
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((csts.SCREEN_WIDTH, csts.SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.HWSURFACE)
    pygame.display.set_caption("Sky_generator")
    
    SS = Shooter_syst(screen)
    clock = pygame.time.Clock()
    #SS.l_events.append(Events.Asteroid_spawn(SS, [1200, asteroid, 100, (16,-9)]))
    #SS.l_events.append(Events.Enemy_spawn(SS, [400, [enemy, enemy, enemy, enemy], [(-100, -100),(-100, 1180),(2020, -100),(2020, 1180)] ]))
    #SS.l_events.append(Events.Enemy_spawn(SS, [400, [enemy_charge, enemy_charge, enemy_charge, enemy_charge], [(2000, 100),(2000, 300),(2000, 500),(2000, 700)] ]))
    SS.l_events.append(Events.Boss_spawn(SS, [200, boss]))


    
    while not SS.done:
        SS.run()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
            