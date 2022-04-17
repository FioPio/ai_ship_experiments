#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Using code from: https://realpython.com/pygame-a-primer/#basic-game-design

# Simple pygame program
# Import and initialize the pygame library
import pygame
pygame.init()

# Imports the custom class car
from car import Car

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Setup the clock for a decent framerate

clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# creates a Car object and locates it at the center of the screen
car=Car(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))

#Color of the car in the RGB format
cColor = (0, 255, 125)

# Radious of the car representation
cR = 15

# Function to draw the car c in the screen
def drawCar(c):
    #pygame.draw.circle(screen, cColor, (c.x,c.y), cR)
    pygame.draw.polygon(screen, cColor, c.getPoints())

'''
# Get the set of keys pressed and check for user input
pressed_keys = pygame.key.get_pressed()
if pressed_keys[K_UP]:
    self.rect.move_ip(0, -5)
'''

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
            if event.key == K_UP:
                car.a+=0.1
            if event.key == K_DOWN:
                car.x+=5
                car.y+=10

        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    drawCar(car)
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)



# Done! Time to quit.
pygame.quit()
