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
from ship import Ship

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

# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Setup the clock for a decent framerate

clock = pygame.time.Clock()

# To write on the screen
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)


# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creates the background variable
bg = Background('img/bg.png', [0,0])

# creates a Ship object and locates it at the center of the screen
ship=Ship( 56, 95, _a=270)

#Color of the ship in the RGB format
sColor = (0, 255, 125)

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
    # Draw the ship on the screen
    screen.blit(s.sprite,s.rect)# (s.corx, s.cory))


def printInfo(s):
    # Computes the distance
    d = int(s.distance(goal.center))
    # Score is the difference between the close it is to the goal
    # and the traveled distance
    score = 2 * (1215 - d) - s.distTrav
    aliveShips = 0
    if s.alive:
        aliveShips+=1
    # Creates the text
    distance_text = my_font.render('{:04d} Distance'.format(d), False, (0, 0, 0))
    score_text    = my_font.render('{:04d} Score'.format(score), False, (0, 0, 0))
    alive_text    = my_font.render('{:04d} Alive ships'.format(aliveShips), False, (0, 0, 0))
    # Adds it to the screen
    screen.blit(distance_text, (783,32))
    screen.blit(score_text, (783, 64))
    screen.blit(alive_text, (783, 96))



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

    # Draw a solid blue circle in the center
    drawShip(ship)

    # Adds the information box
    pygame.draw.rect(screen,( 220, 220, 220), textBox)

    printInfo(ship)

    # Flip the display (Shows the updates)
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)



# Done! Time to quit.
pygame.quit()
