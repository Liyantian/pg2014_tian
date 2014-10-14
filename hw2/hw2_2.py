#Liyan Tian
#10/14/2014
#Homework 2
#Question2:Use the point class described in class
# https://github.com/hetland/pg2014/blob/master/examples/point_example.py
# as a basis. Add a method that rotates the point clockwise by a specified number of radians
#about another optional point, defaulting to the origin.  Tip:  Use operator overloading
#to do math on the point to shift it over.

from math import sqrt
import math

class Point(object):
    """docstring for Point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, p=None):
        if p is None:
            p = Point(0.0, 0.0)
        
        return sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
		
    def rotate(self, r, p=None): 	
        if p is None:
            p = Point(0.0, 0.0)
        x1=self.x-p.x
        y1=self.y-p.y
        x2=x1*math.cos(r)+y1*math.sin(r)
        y2=y1*math.cos(r)-x1*math.sin(r)
        x2=x2+p.x
        y2=y2+p.y
        return Point(x2,y2)
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    
    def __str__(self):
        return '(%f, %f)' % (self.x, self.y)
    
    def __repr__(self):
        return 'Point(%f, %f)' % (self.x, self.y)
    
if __name__ == '__main__':
    p1 = Point(3.0, 4.0)
    p2 = Point(5.0, 8.0)
    
    p3 = p1 + p2
    print p3
    p4=p3.rotate(math.pi/2)
    print p4
    raw_input()