# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:25:26 2017

@author: Benoît
"""

class Event():
    
    def __init__(self, star, allegeance, settlement, infrastructures):
        self.star = star
        self.allegeance = allegeance
        self.settlement = settlement
        self.infrastructures = infrastructures
        
    def display(self):
        print(self.star, self.allegeance, self.settlement, self.infrastructures)
        
        