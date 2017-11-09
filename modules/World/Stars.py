# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 20:15:37 2017

@author: Benoît
"""
import Points
import random
import AdvancedRandom as advran
import Pathes
import Events

#=============================================================================#
#used to generate stars
star_types = ["brown dwarf", "red dwarf", "yellow dwarf", "giant red", "giant blue", "supergiant red", "white dwarf", "black dwarf", "neutron", "black hole", "white hole", "void"]; star_types_weight = [10, 35, 50, 12, 25, 10, 10, 5, 15, 5, 1, 22]

allegeance = ["federation", "rebels", "pirates", "abandoned"]; allegeance_weight = [1, 1, 1, 1]
allegeance_starmodifier = {"brown dwarf":[2, 2, 4, 1], "red dwarf":[3, 5, 2, 1], "yellow dwarf":[10, 4, 2, 1], "giant red":[1, 1, 3, 2], "giant blue":[3, 3, 2, 1], "supergiant red":[1, 1, 3, 2], "white dwarf":[2, 1, 1, 2], "black dwarf":[2, 2, 1, 3], "neutron":[2, 1, 0, 4], "black hole":[4, 1, 0, 5], "white hole":[4, 1, 0, 4], "void":[5, 3, 0, 4]}

settlement = ["military", "civil", "scientific", "unused", "destroyed"]; settlement_weight = [3, 4, 1, 1, 1]
settlement_starmodifier = {"brown dwarf":[2, 0, 3, 8, 1], "red dwarf":[2, 2, 2, 1, 1], "yellow dwarf":[2, 3, 2, 1, 1], "giant red":[0, 1, 1, 1, 4], "giant blue":[2, 1, 6, 5, 2], "supergiant red":[0, 1, 3, 1, 8], "white dwarf":[1, 0, 4, 2, 2], "black dwarf":[4, 0, 7, 4, 2], "neutron":[1, 0, 4, 6, 3], "black hole":[1, 0, 6, 4, 2], "white hole":[1, 0, 2, 1, 1], "void":[3, 0, 1, 4, 3]}
settlement_allegeancemodifier = {"federation":[2, 2, 2, 0, 1], "rebels":[1, 1, 1, 0, 1], "pirates":[1, 1, 0, 0, 1], "abandoned":[0, 0, 0, 1, 1]}

infrastructures = ["craft station", "arsenal", "store", "pub", "command center"]; infrastructures_prob = [0.7, 0.5, 0.7, 0.6, 0.3]
infrastructures_allegeancemodifier = {"federation":[1, 1.2, 1, 0.8, 1], "rebels":[1, 1.2, 0.8, 1, 1], "pirates":[0.8, 0.8, 1.1, 1.4, 0.9], "abandoned":[0, 0, 0, 0, 0]}
infrastructures_settlementmodifier = {"military":[1, 2, 0.5, 0.3, 2.2], "civil":[1, 0.4, 1.2, 1.4, 0.3], "scientific":[2, 0.2, 0.2, 0.2, 0.3], "unused":[0, 0, 0, 0, 0], "destroyed":[0, 0, 0, 0, 0]}

events = [None]
#=============================================================================#

class Star(Points.Point):
    
    def __init__(self, l_existing_stars, map_width, map_height):
        self.x = random.betavariate(1.5, 1.5) * map_width
        self.y = random.gauss(0, 1)*0.15*map_height + 0.5 * map_height
        for existing_star in l_existing_stars:
            if self.dist(existing_star) < map_width / 20 or self.x < 0 or self.x > map_width or self.y < 0 or self.y > map_height:
                self.__init__(l_existing_stars, map_width, map_height)
        
        self.paths = []        
        
        self.tier = int(10 * self.x / map_width)
        self.star_type = ""
        self.allegeance = ""
        self.settlement = ""
        self.infrastructures = []
        self.event = None
        self.set_up()
        
        
    def link(self, l_existing_path, l_stars, map_height):
        """relie l'étoile à un nombre aléatoire d'étoiles proches par des objets de type path(segment)"""
        
        l_dist = []
        l_created_path = []        
        
        for star in l_stars:
            dist = self.dist(star)
            if dist != 0: #si on mesure la distance de l'étoile par rapport à elle même on affecte une grande valeur pour l'ecarter
                l_dist.append(dist)
            else:
                l_dist.append(10000)
        
        if self.y >= 0.333 * map_height and self.y <= 0.667 * map_height :
            nb_of_path = random.choice([4,5,5,6,6])
        elif self.y >= 0.167 * map_height and self.y <= 0.833 * map_height :
            nb_of_path = random.choice([2,3,4,4,5])
        else:
            nb_of_path = 1
            
        for k in range(0, nb_of_path):
            pos_min = l_dist.index(min(l_dist))
            test = True
            for path in l_stars[pos_min].paths: #verification de la non-existence du chemin
                if path.ends[1] == self:
                    test = False
                    
            if test == True:
                new_path = Pathes.Path(self, l_stars[pos_min])
                for path in l_existing_path:
                    if new_path.intersection_with_segment(path) != Points.Point(None, None): #verification des intersections
                        test = False
            
            if test == True:
                l_created_path.append(new_path)
                self.paths.append(new_path)
                l_stars[pos_min].paths.append(Pathes.Path(l_stars[pos_min], self))
                
                    
            l_dist[pos_min] += 10000
            
        return l_created_path
        
        
    def set_up(self):
        """génère les differents éléments présents sur l'étoile"""
        
        self.star_type = advran.select_from_weighted_list(star_types, star_types_weight)
        self.allegeance = advran.select_from_weighted_list(allegeance, advran.multiply_weight(allegeance_starmodifier[self.star_type], allegeance_weight))
        self.settlement = advran.select_from_weighted_list(settlement, advran.multiply_weight(settlement_weight, advran.multiply_weight(settlement_starmodifier[self.star_type], settlement_allegeancemodifier[self.allegeance])))
        self.infrastructures = advran.add_from_prob_list(infrastructures, advran.multiply_weight(infrastructures_prob, advran.multiply_weight(infrastructures_settlementmodifier[self.settlement], infrastructures_allegeancemodifier[self.allegeance])))
        self.event = Events.Event(self.star_type, self.allegeance, self.settlement, self.infrastructures)
        
        
        
        
        
