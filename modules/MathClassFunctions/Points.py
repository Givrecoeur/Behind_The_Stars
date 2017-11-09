# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:33:09 2016

@author: Benoît
"""

import math

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def __eq__(self, other):
        
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    
    def relativ_pos(self, other):
        """return where the other point is relativ to the first one. It return two value : if it is higher, and if it is more on right"""
        up = None
        right = None
        
        if self.y < other.y:
            up = True
        elif self.y > other.y:
            up = False
            
        if self.x < other.x:
            right = True
        elif self.x > other.x:
            right = False
            
        return up, right
        
        
    def axial_sym(self, line):
        
        if line.dir == None:
            return Point(2*line.ori - self.x ,self.y)
            
        if line.dir == 0 :
            return Point(self.x, 2*line.ori - self.y)
            
        ortho = line.ortho(self)
        inter = line.intersection(ortho)
        
        x = 2*inter.x - self.x
        return Point(x, ortho.dir*x + ortho.ori)
        
        
    def dist(self, other):
        
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
     
     
    def move(self, x, y):
        
        self.x = x
        self.y = y
        
    

            
        
        
        
        
        
    
        
    
        
        
        
        
        
        