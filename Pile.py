import pygame
import time
import os
import random
from Constant import * 

class Pile:
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0 
        self.gap = 100

        self.top = 0
        self.bottom = 0
        # PILE de base dans mon image va du bas vers le haut
        self.PILE_TOP = pygame.transform.flip(PILE_IMG, False, True)
        self.PILE_BOTTOM = PILE_IMG

        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50,450)
        self.top = self.height - self.PILE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self,win):
        win.blit(self.PILE_TOP, (self.x,self.top))
        win.blit(self.PILE_BOTTOM, (self.x,self.bottom))

    # On créer un masque pour checké les pixel à l'intérieur de nos hitbox pour que les collisions soit on point
    def collide(self,shoe):
        shoe_mask = shoe.mask()
        top_mask = pygame.mask.from_surface(self.PILE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PILE_BOTTOM)

        top_offset = (self.x - shoe.x,self.top - round(shoe.y))
        bottom_offset = (self.x - shoe.x, self.bottom - round(shoe.y))

        b_point = shoe_mask.overlap(bottom_mask,bottom_offset)
        t_point = shoe_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True
        else :
            return False