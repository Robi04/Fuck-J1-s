import pygame
import time
import os
import random

pygame.font.init()
pygame.init()
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 800

SHOE_IMG = pygame.transform.scale2x(pygame.image.load("./assets/shoe.png"))
PILE_IMG  = pygame.image.load("./assets/pile.png")
BASE_IMG  = pygame.transform.scale2x(pygame.image.load("./assets/base.png"))
BG_IMG  = pygame.transform.scale2x(pygame.image.load("./assets/bg.png"))
FONT1 = pygame.font.SysFont("comicsans",50)
FONT2 = pygame.font.SysFont("comicsan",35)