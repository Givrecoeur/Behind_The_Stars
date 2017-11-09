# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 22:42:33 2016

@author: Benoît
"""

import Stars
import matplotlib.pyplot as plt



class World():
    
    def __init__(self, nb_star, world_width, world_height):
        
        self.l_stars, self.l_paths = self.world_generator(nb_star, world_width, world_height)
         
        
    def world_generator(self, star_nb, map_width, map_height):
        """crée un ensemble d'étoiles générées aléatoirementdans un repère map_width
        *map_height et les relie par des chemins, puis verifie sa validité (cf la 
        fonction check_world plus bas)"""
        
        l_stars = []
        l_paths = []
        for k in range (0, star_nb):
            """création des étoiles"""
            l_stars.append(Stars.Star(l_stars, map_width, map_height))
    
        for star in l_stars:
            """création des chemins et setup des étoile """
            l_paths += star.link(l_paths, l_stars, map_height)
        
        for path in l_paths:
            """setup de chemins"""
            path.set_path()
            
        if not self.check_world(l_stars, l_paths):
            return self.world_generator(star_nb, map_width, map_height)
        
        """l_xpoints = [] #TO DELETE : test d'affichage
        l_ypoints = []    
        for star in l_stars:
            l_xpoints.append(star.x)
            l_ypoints.append(star.y)
            
        plt.clf()   
        for path in l_paths:
            path.display()
        
        plt.plot(l_xpoints, l_ypoints, 'ro')
        plt.axis([0,map_width,0,map_height])
        plt.show()"""
        
        return l_stars, l_paths
            
             
    def check_world(self, l_stars, l_paths):
        """permet de verifier que l'ensemble des étoiles est entierement interconnecté 
        par des chemins"""
        
        l_test = [l_stars[0]]
        l_tested = [l_stars[0]]
        while l_test != []:
            l_found = []
            for star in l_test:
                for path in star.paths:
                    if path.ends[1] not in l_tested:
                        l_tested.append(path.ends[1])
                        l_found.append(path.ends[1])
                        
            l_test = l_found
            
        if len(l_tested) != len(l_stars):
            return False
        return True
        
    
    def set_up(self):
        return None
        #TODO