# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:05:09 2017

@author: Benoît
"""

import pygame
import random

path = "data/images/BackgroundTiles/"

class Background:
    
    def __init__(self, length, scrolling_speed):
        self.pos = 0
        self.length = length
        self.l_tiles = self.import_tiles()
        self.layout = self.set_up_sky(length)
        self.sky = self.paint_sky()
        self.scrolling_speed = scrolling_speed


    def set_up_sky(self, length):
        sky_layout = [0]*144*self.length
        l_empty = []
        
        for i in range(0,144*self.length):
            l_empty.append(i)
            
        while l_empty != []:
            n = l_empty.pop(random.randint(0, len(l_empty) - 1))
            sky_layout[n] = random.randint(0, 32)
            
        return sky_layout
        
        
    def import_tiles(self):
        l_tiles = []
        S = pygame.Surface((120,120), pygame.HWSURFACE)
        S = pygame.image.load(path + "void.png")
        l_tiles.append(S)
        
        for i in range(0,32):
            S = pygame.Surface((120,120), pygame.HWSURFACE)
            S = pygame.image.load(path + "sky_tile_" + str(i) + ".png")
            l_tiles.append(S)
            
        return l_tiles
        
        
    def paint_sky(self):
        sky = pygame.Surface((1920,1080*self.length), pygame.HWSURFACE)
        
        for i in range(0, len(self.layout)):
            S = self.l_tiles[self.layout[i]]
            S = pygame.transform.rotate(S, random.randint(0,3)*90)
            sky.blit(S, (120*(i%16), 120*(i//16)))
            
        return sky
    
        
    def update_sky_rect(self):
        rect = pygame.Rect(0, 1080*5 - (1080 + self.pos), 1920, 1080)
        self.pos += self.scrolling_speed
        
        return rect
    
        
    
    
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN | pygame.HWSURFACE)
    done = False
    pygame.display.set_caption("Sky_generator")
    B = Background(5, 0.5)
    screen.blit(B.sky, (0,0), pygame.Rect(0, 1080*5, 1920, 1080))
    pos=0
    clock = pygame.time.Clock()
    
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        screen.blit(B.sky, (0,0), B.update_sky_rect())
        pos+=1
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()