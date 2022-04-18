#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
          geneticShip.py

This file has the the implementation of the genetic Ship, which implements a
genetic algorithm to move across the provided circuit.
'''
__author__  = 'Ferriol Pey Comas [ferriol73pey@gmail.com]'
__version__ = 'v1.0'
__date__    = '18/04/2022'


import numpy as np
from ship import Ship



class GShip(Ship):
    def __init__( self, _x, _y, _c='B', _a=0 ):
        # Initializes the object as its parent
        Ship.__init__( _x, _y, _c, _a )
        # Adds the map
        self.spdMap = np.random.randint(-5, 5, size=(1200, 800, 2))

    def update(self):
        if s.alive and not s.succeed:
            self.spd = self.spdMap[self.x-1][self.y-1][0]
            self.a += self.spdMap[self.x-1][self.y-1][1]
        Ship.update()
