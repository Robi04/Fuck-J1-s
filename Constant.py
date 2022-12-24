import pygame
import neat
import time
import os
import random

pygame.font.init()
pygame.init()
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 800

BIRD_IMG = pygame.transform.scale2x(pygame.image.load("./assets/bird1.png"))
PIPE_IMG  = pygame.image.load("./assets/pipe.png")
BASE_IMG  = pygame.transform.scale2x(pygame.image.load("./assets/base.png"))
BG_IMG  = pygame.transform.scale2x(pygame.image.load("./assets/bg.png"))
STAT_FONT = pygame.font.SysFont("comicsans",50)
SCORE_FONT = pygame.font.SysFont("comicsan",35)