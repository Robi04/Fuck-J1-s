import pygame
import neat
import time
import os
import random
import pygame_menu
import os
import time

from db import * 
from Bird import *
from Base import *
from Pipe import *
from Constant import *

def draw_window(window,bird,pipes,base,score):
    #draw on the window
    window.blit(BG_IMG, (0,0))
    for pipe in pipes:
        pipe.draw(window)
    text = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    window.blit(text,(WINDOW_WIDTH - 10 - text.get_width(),10))
    base.draw(window)
    bird.draw(window)
    pygame.display.update()

def start_the_game():
    score = 0
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    window.blit(BG_IMG, (0,0))
    clock = pygame.time.Clock()
    bird = Bird()
    base = Base()
    pipes = [Pipe(650)]
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        spawn_pipe = False
        to_remove = []
        for pipe in pipes:
            if pipe.collide(bird) or base.collide(bird) or bird.y < -50:
                run = False
                print(f"{PLAYER_NAME}, Your score is {score}")
                insertScore(PLAYER_NAME,score)
                display_menu()

            # Si pipe + la largeur dépasse de l'écran à gauche on rajoute un nouveau pipe à gauche de l'écran 
            if pipe.x + pipe.PIPE_TOP.get_width() < 0 :
                to_remove.append(pipe)            
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                spawn_pipe = True
                
            pipe.move()

        if spawn_pipe:
            score += 1
            pipes.append(Pipe(700))

        for r in to_remove:
            pipes.remove(r)

        bird.move()
        base.move()
        draw_window(window,bird,pipes,base,score)

def seeHighScore():
    surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    surface.blit(BG_IMG, (0,0))

    pygame.draw.rect(surface, (0,0,0), (20, 720, 220, 40), 2)
    text = SCORE_FONT.render("Go back to menu",1,(0,0,0))
    surface.blit(text,(30,730))


    scores = getScoresDesc()
    i=0
    highscore = True
    text = STAT_FONT.render("HIGHSCORES",1,(0,0,0))
    surface.blit(text,(60,100))
    for row in scores:
        print(row[0])
        text = SCORE_FONT.render("Position " + str(i+1) + " :  " + row[2] + " with " + str(row[1]) + " points",1,(0,0,0))
        surface.blit(text,(60,200 + 50*i))
        i+=1
        print("Name : " + row[2] + " Score : " + str(row[1]))
    pygame.display.flip()
    
    while highscore:
        print(pygame.mouse.get_pos()[0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_menu()
                highscore = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[0] <= 240 and pygame.mouse.get_pos()[1] >= 720 and pygame.mouse.get_pos()[1] <= 760:
                display_menu()
                highscore = False

def player_name(name):
    global PLAYER_NAME
    PLAYER_NAME = name

def display_menu():
    def startGame():
        menu.disable()
        start_the_game()
    
    def highScore():
        menu.disable()
        seeHighScore()

    win_menu = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    menu = pygame_menu.Menu('Robzy bird', 550, 800,theme=pygame_menu.themes.THEME_BLUE)
    menu.add.text_input('Name :',onchange=player_name,default=" ")
    menu.add.button('Play', startGame)
    menu.add.button('See the highest scores', highScore)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(win_menu)

def main():
    display_menu()

main()