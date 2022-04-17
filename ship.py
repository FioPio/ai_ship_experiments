#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
           ship.py

This file has the the implementation of the class Ship.

                   P1
                   ^
                  /|\
                 / | \
                /  |  \
               /   |   \
              /    |    \
             /     C     \
            /    __|__    \
           /  __/  P3 \__  \
          /__/           \__\
        P2                   P4

The distances are defined as following:
   - D1 is the distance from P1 to C.
   - D2 is the distance from P2 and P4 to C.
   - D3 is the distance from P3 to C.
'''
__author__  = 'Ferriol Pey Comas [ferriol73pey@gmail.com]'
__version__ = 'v1.0'
__date__    = '16/04/2022'

from math import cos, sin

# Parameters of the Ship
D1 = 15   # Distance of the peak
D2 = 11   # Distance to the wings
D3 =  3   # Distance of the tail

Awing = 2.094 # Angle of the wings, aprox 120º



class Ship:
    '''
    This class holds
    ==========
    Parameters
    ==========

    _x :  float
       The x of the center of the Ship.

    _y :  float
       The y of the center of the Ship.

    _a :  float
       The angle holding the rotation of the Ship.
    '''
    def __init__( self, _x, _y, _a=0 ):
        # Saves the data on the construction
        self.x = _x
        self.y = _y
        self.a = _a

    def getPoints( self ):
        '''

        Computes the four points that define the shape
        of the ship.

        =======
	RETURNS
	=======

        points : array of points (array of ints)
           A vector containing the four points that define the shape
           of the body as following: [ P1, P2, P3, P4 ] being each
           point as Px = (x, y).

        '''

        # Computing point p1
        x1 = D1 * sin( self.a )
        y1 = D1 * cos( self.a )

        P1 = (int(self.x + x1), int(self.y + y1))

        # Computing point p2
        x2 = D2 * sin( self.a + Awing )
        y2 = D2 * cos( self.a + Awing )

        P2 = (int(self.x + x2), int(self.y + y2))

        # Computing point p3
        x3 = D3 * sin( self.a )
        y3 = D3 * cos( self.a )

        P3 = (int(self.x - x3),int(self.y - y3))

        # Computing point p4
        x4 = D2 * sin( self.a - Awing )
        y4 = D2 * cos( self.a - Awing )

        P4 = (int(self.x + x4),int(self.y + y4))

        return [ P1, P2, P3, P4 ]
