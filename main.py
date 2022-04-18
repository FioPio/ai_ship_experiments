#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
           main.py

This file contains the main implementation for the testing world
in which this experiment is going to run.
'''
__author__  = 'Ferriol Pey Comas [ferriol73pey@gmail.com]'
__version__ = 'v1.0'
__date__    = '17/04/2022'

# Using code from: https://realpython.com/pygame-a-primer/#basic-game-design



# Simple pygame program
# Import and initialize the pygame library
import pygame
pygame.init()

# Imports the custom class ship
#from ship import Ship
from geneticShip import GShip as Ship

from background import Background

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

# Number of random ships
N = 100
# Max number of seconds for a simulation
MAX_TIME = 50 # seconds


# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Setup the clock for a decent framerate

clock = pygame.time.Clock()

# To write on the screen
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

aliveShips = 0

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creates the background variable
bg = Background('img/bg.png', [0,0])

# Array containing the ships
ships = []

# Creates and adds the instances
for i in range(N):
    ships.append(Ship( 56, 95, _a=270))

# creates a Ship object and locates it at the center of the screen
ship=Ship( 56, 95, _a=270)

#Color of the ship in the RGB format
sColor = (0, 255, 125)

framerate=30

# Function to draw the ship s in the screen
def drawShip(s):
    if s.alive:
        # Detects if the ship has colided and kills it
        for limit in limits:
            if limit.colliderect(s.rect):
                s.kill()
                break
        if goal.contains(s.rect):
            s.succeeded()
    # Update the ship data
    s.update()
    s.computeScore(goal.center)
    # Draw the ship on the screen
    screen.blit(s.sprite,s.rect)# (s.corx, s.cory))


def printInfo(s):
    # Computes the distance
    d = int(s.distance(goal.center))
    # gets the score
    score = s.score
    # Creates the text
    distance_text = my_font.render('{:04d} Distance'.format(d), False, (0, 0, 0))
    score_text    = my_font.render('{:04d} Score'.format(score), False, (0, 0, 0))
    alive_text    = my_font.render('{:04d} Alive ships'.format(aliveShips), False, (0, 0, 0))
    time_text     = my_font.render('{:04d} s'.format(int(framecount/framerate)), False, (0, 0, 0))
    # Adds it to the screen
    screen.blit(distance_text, (783,32))
    screen.blit(score_text, (783, 64))
    screen.blit(alive_text, (783, 96))
    screen.blit(time_text, (783, 128))



# Defining the wall limits
limits=[]
rect1 = pygame.Rect(0,0,16,177)
limits.append(rect1)

rect2 = pygame.Rect(0,0, 1200,16)
limits.append(rect2)

rect3 = pygame.Rect(0, 176,496, 640 )
limits.append(rect3)

rect4 = pygame.Rect(272, 48, 368, 96 )
limits.append(rect4)

rect5 = pygame.Rect(544, 287, 144, 177 )
limits.append(rect5)

rect6 = pygame.Rect(752, 0, 448, 640 )
limits.append(rect6)

rect7 = pygame.Rect(496, 688, 128, 112 )
limits.append(rect7)

rect8 = pygame.Rect(623, 784, 577, 16 )
limits.append(rect8)

# Defines the goal rectangle
goal = pygame.Rect(1023, 639, 162, 144 )

# A textbox to write on it
textBox = pygame.Rect(767, 16, 416, 224 )

# Run until the user asks to quit
running = True

while running:
    framecount = 0
    aliveShips = N
    #Start a simulation for MAX_TIME
    while int(framecount/framerate)< MAX_TIME and aliveShips>0 and running:
        # Did the user click the window close button?
        for event in pygame.event.get():
             # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.QUIT:
                running = False

        # To control the ship manually
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            running = False
        if keys[K_UP]:
            ship.a+=5
        elif keys[K_DOWN]:
            ship.a-=5
        if keys[K_SPACE]:
            ship.spd=5
        else:
            ship.spd=0

        # Sets the background image
        screen.fill((255, 255, 255))
        screen.blit(bg.image, bg.rect)

        # Draw the limits
        #for limit in limits:
        #    pygame.draw.rect(screen,( 255, 0, 0), limit)
        # Draw the ships
        i = 0
        goodIndex = 0
        mscore = 0
        aliveShips = 0
        for ship in ships:
            drawShip(ship)
            if ship.score>mscore:
                mscore = ship.score
                goodIndex= i
            if ship.alive:
                aliveShips+=1
            i+=1
        #drawShip(ship)


        # Adds the information box
        pygame.draw.rect(screen,( 220, 220, 220), textBox)

        printInfo(ships[goodIndex])
        #printInfo(ship)

        # Flip the display (Shows the updates)
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(framerate)
        framecount+=1



# Done! Time to quit.
pygame.quit()
