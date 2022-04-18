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
__date__    = '18/04/2022'

import pygame
from math import cos, sin, sqrt
from math import radians as rad
from copy import deepcopy

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
        self.a = _a
        self.setColor(_c)
        self.alive = True
        self.succeed = False
        self.spd=0 # Speed
        self.initialized = False

        self.distTrav = 0 # distance traveled




        # Configures the sprit part
        super(Ship, self).__init__()
        # Updartes the object
        self.update()

    def getSpritePath(self):
        return "img/ship"+self.c+".png"

    def update(self):
        # If the ship is alive update it normally
        if self.alive and not self.succeed:
            # Sets the sprit in the right angle
            if self.initialized:
                cent = deepcopy(self.rect.center)
            self.sprite = pygame.transform.rotate(self.img, self.a)
            # Computes the containing rectangle
            self.rect = self.sprite.get_rect()
            if self.initialized:
                self.rect.center=cent
            else:
                self.initialized=True

            self.y -= int(self.spd * cos(rad(self.a)))
            self.x -= int(self.spd * sin(rad(self.a)))

            self.distTrav+=abs(self.spd)

            #Computes the top left corner to refer the object
            corx = self.x - int(self.rect[2]/2)
            cory = self.y - int(self.rect[3]/2)

            # And updates the rectangle
            self.rect[0]=corx
            self.rect[1]=cory
        elif self.succeed:
            self.sprite = pygame.transform.rotate(self.img, self.fA)

        # If it is dead just show it in red as it died
        else:
            self.sprite = pygame.transform.rotate(self.img, self.fA)

    def setColor(self,_c):
        # Making sure a valid color is indicated
        if _c=='R' or _c == 'B' or _c=='G' or _c=='O':
            self.c = _c
        else:
            self.c = 'B'
        # Loads the image of the sprit
        self.img = pygame.image.load(self.getSpritePath()).convert()
        # Sets which color is set as transparent, in this case black
        self.img.set_colorkey(( 0, 0, 0))

    # Kills the ship
    def kill(self):
        if self.alive:
            # Sets alive to false to indicate it has dead
            self.alive=False
            self.fA = self.a  # Copies the angle in which it dead
            self.setColor('R') # Changes the color of the ship to red
    def succeeded(self):
        if self.alive and not self.succeed:
            # Sets alive to false to indicate it has dead
            self.succeed=True
            self.fA = self.a  # Copies the angle in which it dead
            self.setColor('O') # Changes the color of the ship to red

    def distance(self,p):
        dify = self.y - p[1]
        difx = self.x - p[0]

        return sqrt(( difx * difx) + ( dify * dify ))

    def copy(self):
        return deepcopy(self)
