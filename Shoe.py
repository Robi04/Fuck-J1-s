import pygame
import time
import os
import random
from Constant import * 

class Shoe:
    IMG = SHOE_IMG
    MAX_ROTATION = 25
    ROT_VEL = 10
    ACCELERATION = 3
    # 0 de base puis après puis -10 histoire que la chaussure ne saute pas dès que l'ob lance le jeu 
    velocity = 0
    def __init__(self):
        self.x = 230
        self.y = 360
        self.rota = 0
        self.time = 0
        self.height = self.y
        self.img = self.IMG

    def jump(self):
        # Echelle par du corner en haut à gauche donc il nous faut une vel négative
        self.time = 0
        Shoe.velocity = -10

        # Position ou on débute notre saut pour analyser la descente plus tard 
        self.height = self.y

    def move(self):
        self.time +=1

        # Lois de newton : https://www.youtube.com/watch?v=v_linpA7uXo&ab_channel=CDcodes
        # Nouvelle position = ancienne position + velocité * temps + 1/2 * acceleration * temps^2
        d = Shoe.velocity * self.time + 0.5 * Shoe.ACCELERATION * self.time**2

        # On set une distance entre 2 frames différentes car sinon c'est incontrolable
        # On doit passer par là car on veut une gravité relativemment faible pour le jeu 
        if d >= 15:
            d = 15
    
        self.y = self.y + d

        #si trop de rota à la descente on bloque à notre angle max de chute
        if self.y < self.height + 40:
            if self.rota < self.MAX_ROTATION:
                self.rota = self.MAX_ROTATION
        else : 
            if self.rota > -60:
                self.rota -= self.ROT_VEL
    
    def draw(self,win):
        rotated_image = pygame.transform.rotate(self.img,self.rota)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x,self.y)).center)
        win.blit(rotated_image,new_rect.topleft)

    def mask(self):
        return pygame.mask.from_surface(self.img)