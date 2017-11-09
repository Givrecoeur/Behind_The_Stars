# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 00:36:12 2017

@author: Benoît
"""

import random
import Math_operations as mtop

def stop(enemy):
    
    enemy.dx = 0
    enemy.dy = 0

def get_closer_thrust(enemy):
    
    dx = enemy.system.player.x - enemy.x
    dy = enemy.system.player.y - enemy.y
    dx, dy = mtop.trig_normalize(dx, dy, enemy.speed*0.1)
    enemy.dx += dx
    enemy.dy += dy
    if mtop.length(enemy.dx, enemy.dy) > 1.3*enemy.speed:
        enemy.dx, enemy.dy = mtop.trig_normalize(enemy.dx, enemy.dy, enemy.speed*1.3)
    enemy.action = None


def get_closer(enemy):
    
    enemy.dx = enemy.system.player.x - enemy.x
    enemy.dy = enemy.system.player.y - enemy.y
    enemy.dx, enemy.dy = mtop.trig_normalize(enemy.dx, enemy.dy, enemy.speed)
    enemy.time += 1
    if enemy.time == 20:
        enemy.action = None
        enemy.time = 0

        
def attack_1s(enemy):
    
    if enemy.time == 0:
        stop(enemy)
        
    enemy.time += 1
    enemy.weapon.shoot(enemy.system.player.x +13 - enemy.weapon_pos[0], enemy.system.player.y +7 - enemy.weapon_pos[1])
    
    if enemy.time == 60:
        enemy.time = 0
        enemy.action = None
        
        
def dodge_1s(enemy):
    
    if enemy.time == 0:
        test = random.randint(0,1)
        if test == 1:
            enemy.dy = enemy.system.player.x - enemy.x + 13
            enemy.dx = -(enemy.system.player.y - enemy.y + 7)
        else:
            enemy.dy = -(enemy.system.player.x - enemy.x + 13)
            enemy.dx = enemy.system.player.y - enemy.y + 7
        enemy.dx, enemy.dy = mtop.trig_normalize(enemy.dx, enemy.dy, enemy.speed)
        enemy.time += 1
        
    elif enemy.time == 60:
        enemy.time = 0
        enemy.action = None
        
    else:
        enemy.time += 1
        
        
def idle_1s(enemy):
    
    if enemy.time == 0:
        stop(enemy)
    enemy.time += 1
    if enemy.time == 60:
        enemy.action = None
        enemy.time = 0
        