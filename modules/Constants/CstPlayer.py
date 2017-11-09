# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 18:02:54 2017

@author: Benoît
"""

import Bullets
import Weapons
import Abilities


"""Player"""
PLAYER_SPRITE = "player2.png"
PLAYER_SPEED = 8
PLAYER_ARMOR = 10
PLAYER_HEALTH = 1000
PLAYER_MAX_HEALTH = 1000
PLAYER_MAX_ENERGY = 3000
PLAYER_MAX_SHIELD = 100
PLAYER_ENERGY_REGEN = 0.7
PLAYER_WEAPONS = [Weapons.crappy_gun, Weapons.crappy_plasma]
PLAYER_BULLETS = [Bullets.shotgun_bullet, Bullets.simple_plasma]
PLAYER_ABILITIE_1 = Abilities.abilitie_none
PLAYER_ABILITIE_2 = Abilities.abilitie_test