# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:24:50 2017

@author: Benoît
"""

import Lines
import random

class Path(Lines.Segment):
    
    def __init__(self, star1, star2):
        self.dir, self.ori = self.create_line_2p(star1, star2)
        self.angle = self.lign_angle_direction()
        self.ends = [star1, star2]
        self.length = star1.dist(star2)
        self.waves = []
        self.tier = max(star1.tier, star2.tier)
        
    
    def set_path(self):
        nb_waves = int(self.length / 10) + 1
        for i in range(0, nb_waves):
            self.waves.append([[random.choice(l_wavesTier[0])]]) #str(self.tier)
            self.waves[-1].append(random.choice(l_startPos[len(self.waves[-1][-1])]))
        print(self.waves)
            
            


#=============================================================================#
#=============================================================================#
#=============================================================================#

#Starting positions for waves

l_startPos1 = [[(-100, -100)], [(960, -100)], [(2020, -100)]]
l_startPos2 = []
l_startPos3 = [[(-100, -100), (-100, 0), (0, -100)], [(860, -100), (960, -100), (1060, -100)], [(2020, -100), (1920, -100), (2020, 0)]]
l_startPos4 = []
l_startPos5 = []
l_startPos6 = []
l_startPos7 = []
l_startPos8 = []
l_startPos9 = []
l_startPos10 = []
l_startPos15 = []
l_startPos20 = []
l_startPos30 = []

l_startPos = {1: l_startPos1, 2: l_startPos2, 3: l_startPos3, 4: l_startPos4, 5: l_startPos5, 6: l_startPos6, 7: l_startPos7, 8: l_startPos8, 9: l_startPos9, 10: l_startPos10, 15: l_startPos15, 20: l_startPos20, 30: l_startPos30}
       
#=============================================================================#
#=============================================================================#
#=============================================================================#  
       
#Waves definitions
        
import Enemies as E

l_wavesTier0 = [[E.E_basic_gunner], [E.E_basic_sniper], [E.E_basic_gunner, E.E_basic_shotguner, E.E_basic_shotguner], [E.E_basic_gunner, E.E_basic_shotguner, E.E_basic_sniper]]
l_wavesTier1 = [1]
l_wavesTier2 = [2]
l_wavesTier3 = [3]
l_wavesTier4 = [4]
l_wavesTier5 = [5]
l_wavesTier6 = [6]
l_wavesTier7 = [7]
l_wavesTier8 = [8]
l_wavesTier9 = [9]
l_wavesTier10 = [10]

l_wavesTier = [l_wavesTier0, l_wavesTier1, l_wavesTier2, l_wavesTier3, l_wavesTier4, l_wavesTier5, l_wavesTier6, l_wavesTier7, l_wavesTier8, l_wavesTier9, l_wavesTier10]

