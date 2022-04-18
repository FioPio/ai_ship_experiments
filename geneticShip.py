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
        # Adds the map
        self.spdMap = np.random.randint(-10, 10, size=(1200, 800, 2))
        # Initializes the object as its parent
        super().__init__( _x, _y, _c, _a )

    def update(self):
        # Adds the proper control data
        if self.alive and not self.succeed:
            self.spd = self.spdMap[self.x-1][self.y-1][0]
            self.a += self.spdMap[self.x-1][self.y-1][1]
        super().update()

    def computeScore(self, g):
        if self.alive and not self.succeed:
            d = int(self.distance(g))
            # Score is the difference between the close it is to the goal
            # and the traveled distance
            self.score = 2 * (1215 - d) - self.distTrav
