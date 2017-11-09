# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 20:43:58 2017

@author: Benoît
"""

import math

def length(x, y):
    """return the lenght of a vector"""
    
    return math.sqrt((x)**2 + (y)**2)
    

def distance(x1, y1, x2, y2):
    """return the distance within 2 objects"""
    
    return length(x1 - x2, y1 - y2)
    

def trig_normalize(x, y, force):
    """this function take a vector and resize it to a certain value without 
    changing its direction"""
    if x != 0:
        xf = force * math.cos(math.atan(abs(y / x)))
        yf = force * math.sin(math.atan(abs(y / x)))
    
    elif y != 0 :
        xf = force * math.cos(math.pi/2)
        yf = force * math.sin(math.pi/2)    
    
    else:
        return 0, 0
        
        
    if x < 0:
        xf = -xf
    if y < 0:
        yf = -yf
    
    if abs(xf) < 0.00001:
        xf = 0
    if abs(yf) < 0.00001:
        yf = 0
    return xf, yf
        


def trig_project(x1, y1, x2, y2, force):
    """this fuction take the position of two objects (the attractor "1"
    and the attracted "2") in space, and a force, and return the 
    projection of it on x and y axes"""
    
    Dx = x1 - x2
    Dy = y1 - y2
    
    return trig_normalize(Dx, Dy, force)
    
    
def get_angle(dx, dy):

    if dx == 0 and dy == 0:
        return 0
        
    unsigned_dx = abs(dx)
    unsigned_dy = abs(dy)
    
    if unsigned_dx != 0:
        angle = math.degrees(math.atan(unsigned_dy/unsigned_dx))
    else:
        angle = 90
    
    if dx >= 0 and dy >= 0:
        return angle
    elif dx >= 0 and dy <= 0:
        return 360 - angle
    elif dx <= 0 and dy >= 0:
        return 180 - angle
    else:
        return 180 + angle
        
        
def get_dir(angle):
    angle = math.radians(angle)
    dx = math.cos(angle)
    dy = math.sin(angle)
    if abs(dx) < 0.00001:
        dx = 0
    if abs(dy) < 0.00001:
        dy = 0
    return dx, dy
    
if __name__ == "__main__":
    #print(trig_project(-1000,1000,1000,-1000,1000))
    #print(trig_normalize(1, 1, 1))
    print(get_angle(0,0))
    print(get_angle(0, 1))
    print(get_angle(1, 0))
    print(get_angle(0, -1))
    print(get_angle(-1, 0))
    print(get_angle(1, 1))
    print(get_angle(-1, 1))
    print(get_angle(1, -1))
    print(get_angle(-1, -1))
    print(" ")
    print(get_dir(0))
    print(get_dir(90))
    print(get_dir(180))
    print(get_dir(270))
    print(get_dir(360))
    print(get_dir(45))
    print(get_dir(225))
    print(get_dir(60))