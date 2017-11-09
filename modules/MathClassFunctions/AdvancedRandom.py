# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:43:42 2017

@author: Benoît
"""

import random

def select_from_weighted_list(liste, weight):
    """randomly selects an unique element from a list, taking account
    of the weight (int) of each element, provided in another list"""
    
    rand = random.randint(1, sum(weight))
    tot = 0
    for i in range(0, len(liste)):
        tot += weight[i]
        if rand <= tot:
            return liste[i]
        
    
    
    
def add_from_prob_list(liste, probabilities):
    """each element of the list will randomly be or not be added to the output 
    list, relativ to their probability (0<prob<1)"""
    
    out = []
    for i in range(0, len(liste)):
        rand = random.random()
        if rand <= probabilities[i]:
            out.append(liste[i])
    return out
     
    
def multiply_weight(weight1, weight2):
    """this is just the multiplication element to element of two lists""" 
    new_weight = []
    for i in range(0, len(weight1)):
        new_weight.append(weight1[i] * weight2[i])
    return new_weight