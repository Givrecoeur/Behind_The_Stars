# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:03:29 2017
@author: Benoît
This module contains everything needed to manage input from both controller and
keyboard. It also allow to remap some of the default controls for keyboard. #TODO
"""

import pygame
import CstSystem as csts

path = "data/saves/"

class InputManagment():
    
    def __init__(self, sys, systype, keyboard):
        """Constructor, sys = system that will use the class, keyboard = True if
        keyboard is to be used, False if controler is to be used"""
        
        self.system = sys
        
        #define if we use controler or keyboard and if system is shooter or menu
        self.keyboard = keyboard
        if systype == "shooter":
            self.manage_function = self.manage_input_keyboard_shooter
        else :
            self.manage_function = self.manage_input_keyboard_menu
        
        if not self.keyboard:
            self.joystick = self.init_joystick()
            if self.joystick != None:
                if systype == "shooter":
                    self.manage_function = self.manage_input_controler_shooter
                else:
                    self.manage_function = self.manage_input_controler_menu
        
        #define the file from wich custom control must be imported, the file must
        #be a .txt correctly formated (see the one by default for the patern)
        self.save = path + "control.txt"
        
        #Keyboard mapable controls
        self.up = pygame.K_w
        self.down = pygame.K_s 
        self.right = pygame.K_a
        self.left = pygame.K_d
        self.abilitie1 = pygame.K_q
        self.abilitie2 = pygame.K_e
        
        self.load_control()
        
        
    def load_control(self):
        """load the control from a file"""
        return 0 #TODO
        
        
    def save_control(self):
        """save the control in a file"""
        return 0 #TODO        
        
    
    def remap(self, key, new_key):
        """modify a control"""
        return 0 #TODO
        
        
    def init_joystick(self):
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            return joystick
        else:
            self.keyboard = True
            return None
            
    
    def get_mouse_pos(self):
        
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = (mouse_pos[0] * csts.RATIO, mouse_pos[1] * csts.RATIO)
        return mouse_pos
        
        
    def manage_input_keyboard_menu(self):
        
        self.system.mouse_pos = self.get_mouse_pos()
        
        window = self.system.main_window.get_overflown_window(self.system.mouse_pos)
        if window != None:
            window.mouse_overflown()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.system.done = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.system.set_pause()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if window != None:
                        window.l_click()
                    else:
                        self.system.main_window.click_out()
                elif event.button == 3:
                    if window != None:
                        window.r_click()
                elif event.button == 4:
                    if window != None:
                        window.scroll(10)
                elif event.button == 5:
                    if window != None:
                        window.scroll(-10)                   
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.system.main_window.l_unclick()
                elif event.button == 3:
                    self.system.main_window.r_unclick()   
                    
                    
    def manage_input_controller_menu(self):
        pass
    
    
    def manage_input_keyboard_shooter(self):
        self.system.mouse_pos = self.get_mouse_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.system.done = True
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.system.set_pause()
                elif event.key == self.up:
                    self.system.player.add_speed(0, -1)
                elif event.key == self.right:
                    self.system.player.add_speed(-1, 0)
                elif event.key == self.down:
                    self.system.player.add_speed(0, 1)
                elif event.key == self.left:
                    self.system.player.add_speed(1, 0)
                    
                elif event.key == self.abilitie1:
                    self.system.player.use_abilitie_1()
                elif event.key == self.abilitie2:
                    self.system.player.use_abilitie_2()
            
            elif event.type == pygame.KEYUP:
                if event.key == self.up:
                    self.system.player.add_speed(0, 1)
                elif event.key == self.right:
                    self.system.player.add_speed(1, 0)
                elif event.key == self.down:
                    self.system.player.add_speed(0, -1)
                elif event.key == self.left:
                    self.system.player.add_speed(-1, 0)
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.system.player.shooting = True
                if event.button == 3:
                    self.system.player.next_weapon()
                elif event.button == 4:
                    self.system.player.previous_weapon()
                elif event.button == 5:
                    self.system.player.next_weapon()
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.system.player.shooting = False
                    
                    
    def manage_input_controler_shooter(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.system.done = True
                
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 7:
                    self.system.done = True
                elif event.button == 5:
                    self.system.player.shooting = True
                elif event.button == 4:
                    self.system.player.next_weapon()
            
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 5:
                    self.system.player.shooting = False
        
        l_joy_value = []            
        for i in range(0, 5):
            l_joy_value.append(self.joystick.get_axis(i))
        for i in range(0, len(l_joy_value)):
            if abs(l_joy_value[i]) < 0.1:
                l_joy_value[i] = 0
            
        self.system.player.set_speed(l_joy_value[0],l_joy_value[1])
        
        if l_joy_value[2] > 0.6:
            self.system.player.use_abilitie_1
        elif l_joy_value[2] < -0.6:
            self.system.player.use_abilitie_2
            
        dx = l_joy_value[4]
        dy = l_joy_value[3]
        if dx == 0  and dy == 0:
            dy = -0.1
        self.system.mouse_pos[0] = self.system.player.weapon_pos[0] + dx*500
        self.system.mouse_pos[1] = self.system.player.weapon_pos[1] + dy*500
        if self.system.mouse_pos[0] < 0:
            self.system.mouse_pos[0] = 0
        elif self.system.mouse_pos[0] > csts.SCREEN_WIDTH:
            self.system.mouse_pos[0] = csts.SCREEN_WIDTH
        if self.system.mouse_pos[1] < 0:
            self.system.mouse_pos[1] = 0
        elif self.system.mouse_pos[1] > csts.SCREEN_HEIGHT:
            self.system.mouse_pos[1] = csts.SCREEN_HEIGHT
            
            
    
        