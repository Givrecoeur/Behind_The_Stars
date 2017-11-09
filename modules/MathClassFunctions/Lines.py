# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:11:27 2016

@author: Benoît
"""

import math
import numpy
import matplotlib.pylab as py
import Points


class Line():
    
    def __init__(self, point1, point2):
        
        self.dir, self.ori = self.create_line_2p(point1, point2)
        self.angle = self.lign_angle_direction()
        
        
    def create_line_2p(self, point1, point2):
        """return the line which pass throught two given points"""
        if point1 == point2:
            return None, None
    
        if point1.x == point2.x:
            return None, point1.x
        
        a = (point2.y - point1.y) / (point2.x - point1.x)
        
        return a, point1.y - a*point1.x
        
        
    def lign_angle_direction(self):
        """return the angle relativ to the horizontal of a line"""
        
        if self.dir == None:
            return math.pi / 2
            
        return math.atan(self.dir)
        
        
    def intersection(self, other):
        """return the intersection of two lines, if it exists"""
        
        if self.dir == other.dir or other.ori == None or self.ori == None:
            return Points.Point(None, None)
            
        if self.dir == None:
            return Points.Point(self.ori, other.dir*self.ori + other.ori)
            
        if other.dir == None:
            return Points.Point(other.ori, self.dir*other.ori + self.ori)
            
            
        x = (other.ori - self.ori) / (self.dir - other.dir)
            
        return Points.Point(x, self.dir * x + self.ori)
            
    
    
    def ortho(self, point):
        """create an orthogonal line which pass by a point"""
        
        if self.dir == None:
            if self.ori == None:
                return None
            return Line(point, Points.Point(point.x + 1, point.y))
        
        if self.dir == 0:
            return Line(point, Points.Point(point.x, point.y + 1))
        
        a = -1/self.dir
        b = point.y - a*point.x
        
        return Line(point, Points.Point(point.x+10, point.x+10*a + b))
        
    
    
    def symLine(self, line):
        """create the symetric of a line by another"""
        
        if self.dir == None:
            if self.ori == None:
                return None 
            point1 = Points.Point(self.ori, -1000)
            point2 = Points.Point(self.ori, 1000)
        
        else:
            point1 = Points.Point(-1000, -1000*self.dir + self.ori)
            point2 = Points.Point(1000, 1000*self.dir, + self.ori)
        
        point1 = point1.axial_sym(line)
        point2 = point2.axial_sym(line)
        
        return Line(point1, point2)
        
        
    def parallelLine(self, point):
        """create a line parallel to a given one which pass by a point"""
        
        ori = point.y - self.dir * point.x
        
        point2 = Points.Point(point.x + 1000, self.dir * point.x + 1000 + ori)
        
        return Line(point, point2)
        
        
        
class Segment(Line):
    
    def __init__(self, point1, point2):
        self.dir, self.ori = self.create_line_2p(point1, point2)
        self.angle = self.lign_angle_direction()
        self.ends = [point1, point2]
        
        
    def in_seg_x(self, point):
        """say if a point is in the x interval of a segment"""
        
        if point.x < self.ends[0].x and point.x > self.ends[1].x :
            return True
        if point.x > self.ends[0].x and point.x < self.ends[1].x :
            return True
        return False
        
               
    def intersection_with_line(self, line):
        
        inter = self.intersection(line)
        if inter != Points.Point(None, None):
            if self.in_seg_x(inter):
                return inter
        return Points.Point(None, None)
                
    
    def intersection_with_segment(self, other):
        
        inter = self.intersection(other)
        
        if inter != Points.Point(None, None):
            if self.in_seg_x(inter) and other.in_seg_x(inter):
                return inter
        return Points.Point(None, None)

            
    def display(self):
        
        if self.dir != None:
                
            x = numpy.linspace(self.ends[0].x, self.ends[1].x, 50)
            y = self.dir * x + self.ori
            py.plot(x, y)
        
        else:
            
            x = numpy.linspace(self.ends[0].x, self.ends[1].x, 50)
            y = numpy.linspace(self.ends[0].y, self.ends[1].y, 50)
            py.plot(x, y)
               
    
    def end_display(seglist):
        
        for seg in seglist:
            
            seg.display()
            
        py.show()
            
        
    def reflexions(seglist, halfline):
        
        l_inter = [1]
        l_segment = []

        while l_inter != []:
            l_inter = []
            
            for seg in seglist:
                test = seg.intersection_with_segment(halfline)
                if test != Points.Point(None, None):
                    l_inter.append(test)
            
            l_dist = []
            for inter in l_inter:
                l_dist.append(inter.dist(halfline.departure))
            
            num = l_dist.index(max(l_dist))
            segment, halfline = seglist[num].reflect_halfline(halfline, l_inter[num])
            
            l_segment.append(segment)
        
        l_segment.append(Segment(halfline.departure, halfline.end))
        Segment.end_display(l_segment)        
        

        
        
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        