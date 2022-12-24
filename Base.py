import pygame
import neat
import time
import os
import random
from Constant import * 

class Base:
    VEL = 5
    WIDTH = BASE_IMG.get_width()
    IMG = BASE_IMG

    def __init__(self):
        self.y = 730
        self.x1 = 0
        self.x2 = self.WIDTH
    
    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL

        # On va avoir 2 image qui vont s'alterner pour créer un mouvement sans avoir de vide au niveau de la base 
        # Si une image est totalement hors de vision sur la gauche alors on la met à droite mais toujours hors de vu
        # Les 2 vont s'alterner et ne verra rien 
        if self.x1 + self.WIDTH < 0 :
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0 :
            self.x2 = self.x1 + self.WIDTH

    def draw(self,win):
        win.blit(self.IMG,(self.x1,self.y))
        win.blit(self.IMG,(self.x2,self.y))

     # On créer un masque pour checké les pixel à l'intérieur de nos hitbox pour que les collisions soit on point
    def collide(self,bird):
        bird_mask = bird.mask()
        mask = pygame.mask.from_surface(self.IMG)

        offsetx1 = (self.x1 - bird.x,self.y - round(bird.y))
        offsetx2 = (self.x2 - bird.x,self.y - round(bird.y))

        overlapedx1 = bird_mask.overlap(mask,offsetx1)
        overlapedx2 = bird_mask.overlap(mask,offsetx2)

        if overlapedx1 or overlapedx2:
            return True
        else :
            return False