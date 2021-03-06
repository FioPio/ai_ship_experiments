#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Obtained from https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame by Anthony Pham

import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
