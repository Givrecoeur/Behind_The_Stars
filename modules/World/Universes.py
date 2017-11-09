# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:01:24 2017

@author: Benoît
"""

import random
import Worlds

class Universe():
    """A container for all information relative to the non-shooter part of the 
    game and all methods to generate it"""
    
    def __init__(self, seed, player, save = False):
        
        if not save:
            self.seed = seed
            random.seed(seed)
        
            self.world = Worlds.World(75, 1800, 900)
        
            self.player = player
            
        else:
            self.load()
        
        
    def save(self):
        pass
    
    
    def load(self):
        pass
    
    

if __name__ == "__main__":
    
    U = Universe(random.randint(1,40), None)
    max_length = 0
    for star in U.world.l_stars:
         star.event.display()
    for path in U.world.l_paths:
        if path.length > max_length:
            max_length = path.length
    print(max_length)
         
         
