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

import pygame
#from math import cos, sin

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

    _c :  char (Optional)
       The color of the ship, may be 'B' for blue,
       'R' for red and 'G' for green. Default is 'B'.

    _a :  float (Optional)
       The angle holding the rotation of the Ship in
       degrees. Default is 0.
    '''
    def __init__( self, _x, _y, _c='B', _a=0 ):
        # Saves the data on the construction
        self.x = _x
        self.y = _y
        # Making sure a valid color is indicated
        if _c=='R' or _c == 'B' or _c=='G':
            self.c = _c
        else:
            self.c = 'B'
        self.a = _a
        # Configures the sprit part
        super(Ship, self).__init__()
        # Loads the image of the sprit
        self.img = pygame.image.load(self.getSpritePath()).convert()
        # Sets which color is set as transparent, in this case black
        self.img.set_colorkey(( 0, 0, 0))
        # Updartes the object
        self.update()

    def getSpritePath(self):
        return "img/ship"+self.c+".png"

    def update(self):
        # Sets the sprit in the right angle
        self.sprite = pygame.transform.rotate(self.img, self.a)
        # Computes the containing rectangle
        self.rect = self.sprite.get_rect()

        #Computes the top left corner to refer the object
        self.corx = self.x - int(self.rect[2]/2)
        self.cory = self.y - int(self.rect[3]/2)
