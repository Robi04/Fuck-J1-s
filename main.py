import pygame
import time
import os
import random
import pygame_menu
import os
import time


from db import * 
from Shoe import *
from Base import *
from Pile import *
from Constant import *

def draw_window(window,shoe,piles,base,score):
    #draw on the window
    window.blit(BG_IMG, (0,0))
    for pile in piles:
        pile.draw(window)
    text = STAT_FONT.render("Score: " + str(score),1,(255,255,100))
    window.blit(text,(WINDOW_WIDTH - 10 - text.get_width(),10))
    base.draw(window)
    shoe.draw(window)
    pygame.display.update()

def start_the_game():
    print(DIFFICULTY[0][0])
    diff_distance = [['Easy',800],['Medium',700],['Hard',520]]
    for i in diff_distance:
        if i[0]==DIFFICULTY[0][0]:
            val_dif = i[1]
    start_time = time.time()
    score = 0
    jump_count = 0
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    window.blit(BG_IMG, (0,0))
    clock = pygame.time.Clock()
    shoe = Shoe()
    base = Base()
    piles = [Pile(val_dif)]
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoe.jump()
                    jump_count += 1 

        spawn_pile = False
        to_remove = []
        for pile in piles:
            if pile.collide(shoe) or base.collide(shoe) or shoe.y < -50:
                run = False
                print(f"{PLAYER_NAME}, Your score is {score}")
                print("--- %s seconds ---" % (time.time() - start_time))
                print(f"Nombre de saut {jump_count}")
                insertScore(PLAYER_NAME,score,jump_count,time.time() - start_time,DIFFICULTY[0][0])
                display_menu()

            # Si pile + la largeur dépasse de l'écran à gauche on rajoute un nouveau pile à gauche de l'écran 
            if pile.x + pile.PILE_TOP.get_width() < 0 :
                to_remove.append(pile)            
            if not pile.passed and pile.x < shoe.x:
                pile.passed = True
                spawn_pile = True
                
            pile.move()

        if spawn_pile:
            score += 1
            piles.append(Pile(val_dif))

        for r in to_remove:
            piles.remove(r)

        shoe.move()
        base.move()
        draw_window(window,shoe,piles,base,score)

def seeHighScore():
    #BACKGROUND
    surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    surface.blit(BG_IMG, (0,0))

    #BUTTON BACK TO MENU
    pygame.draw.rect(surface, (0,0,0), (20, 720, 220, 40), 2)
    text_back_menu = SCORE_FONT.render("Go back to menu",1,(0,0,0))
    surface.blit(text_back_menu,(30,730))

    #TITLE HIGHSCORE
    text_title_highscore = STAT_FONT.render("HIGHSCORES",1,(0,0,0))
    surface.blit(text_title_highscore,(60,20))

    #BUTTON Difficulty 1
    pygame.draw.rect(surface, (0,0,0), (20, 100, 100, 40), 2)
    text_easy = SCORE_FONT.render("EASY",1,(200,0,200))
    surface.blit(text_easy,(40,110))

    #BUTTON Difficulty 2
    pygame.draw.rect(surface, (0,0,0), (190, 100, 130, 40), 2)
    text_medium = SCORE_FONT.render("MEDIUM",1,(0,0,0))
    surface.blit(text_medium,(200,110))

    #BUTTON Difficulty 3
    pygame.draw.rect(surface, (0,0,0), (400, 100, 100, 40), 2)
    text_hard = SCORE_FONT.render("HARD",1,(0,0,0))
    surface.blit(text_hard,(420,110))


    #GET THE HIGHEST SCORES FROM THE DATABASE
    scores = getScoresDesc("Easy")
    i=0
    highscore = True

    for row in scores:
        print(row[0])
        text = SCORE_FONT.render("Position " + str(i+1) + " :  " + row[2] + " with " + str(row[1]) + " points",1,(0,0,0))
        surface.blit(text,(60,200 + 50*i))
        i+=1
        print("Name : " + row[2] + " Score : " + str(row[1]))
    pygame.display.flip()
    
    while highscore:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                display_menu()
                highscore = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[0] <= 240 and pygame.mouse.get_pos()[1] >= 720 and pygame.mouse.get_pos()[1] <= 760:
                display_menu()
                highscore = False

            #EASY
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[0] <= 120 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 140:
                #BACKGROUND
                surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
                surface.blit(BG_IMG, (0,0))

                #BUTTON BACK TO MENU
                pygame.draw.rect(surface, (0,0,0), (20, 720, 220, 40), 2)
                text_back_menu = SCORE_FONT.render("Go back to menu",1,(0,0,0))
                surface.blit(text_back_menu,(30,730))

                #TITLE HIGHSCORE
                text_title_highscore = STAT_FONT.render("HIGHSCORES",1,(0,0,0))
                surface.blit(text_title_highscore,(60,20))
                i=0
                scores = getScoresDesc("Easy")
                for row in scores:
                    text = SCORE_FONT.render("Position " + str(i+1) + " :  " + row[2] + " with " + str(row[1]) + " points",1,(0,0,0))
                    surface.blit(text,(60,200 + 50*i))
                    i+=1
                pygame.draw.rect(surface, (0,0,0), (20, 100, 100, 40), 2)
                text_easy = SCORE_FONT.render("EASY",1,(200,0,200))
                surface.blit(text_easy,(40,110))
                
                pygame.draw.rect(surface, (0,0,0), (190, 100, 130, 40), 2)
                text_medium = SCORE_FONT.render("MEDIUM",1,(0,0,0))
                surface.blit(text_medium,(200,110))
                
                pygame.draw.rect(surface, (0,0,0), (400, 100, 100, 40), 2)
                text_hard = SCORE_FONT.render("HARD",1,(0,0,0))
                surface.blit(text_hard,(420,110))
                pygame.display.update()


            # MEDIUM
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 190 and pygame.mouse.get_pos()[0] <= 320 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 140:
                i=0
                #BACKGROUND
                surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
                surface.blit(BG_IMG, (0,0))

                #BUTTON BACK TO MENU
                pygame.draw.rect(surface, (0,0,0), (20, 720, 220, 40), 2)
                text_back_menu = SCORE_FONT.render("Go back to menu",1,(0,0,0))
                surface.blit(text_back_menu,(30,730))

                #TITLE HIGHSCORE
                text_title_highscore = STAT_FONT.render("HIGHSCORES",1,(0,0,0))
                surface.blit(text_title_highscore,(60,20))
                scores = getScoresDesc("Medium")
                for row in scores:
                    text = SCORE_FONT.render("Position " + str(i+1) + " :  " + row[2] + " with " + str(row[1]) + " points",1,(0,0,0))
                    surface.blit(text,(60,200 + 50*i))
                    i+=1

                pygame.draw.rect(surface, (0,0,0), (20, 100, 100, 40), 2)
                text_easy = SCORE_FONT.render("EASY",1,(0,0,0))
                surface.blit(text_easy,(40,110))

                pygame.draw.rect(surface, (0,0,0), (190, 100, 130, 40), 2)        
                text_medium = SCORE_FONT.render("MEDIUM",1,(200,0,200))
                surface.blit(text_medium,(200,110))
                
                pygame.draw.rect(surface, (0,0,0), (400, 100, 100, 40), 2)
                text_hard = SCORE_FONT.render("HARD",1,(0,0,0))
                surface.blit(text_hard,(420,110))
                pygame.display.update()

            #HARD
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 140:
                i=0
                #BACKGROUND
                surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
                surface.blit(BG_IMG, (0,0))

                #BUTTON BACK TO MENU
                pygame.draw.rect(surface, (0,0,0), (20, 720, 220, 40), 2)
                text_back_menu = SCORE_FONT.render("Go back to menu",1,(0,0,0))
                surface.blit(text_back_menu,(30,730))

                #TITLE HIGHSCORE
                text_title_highscore = STAT_FONT.render("HIGHSCORES",1,(0,0,0))
                surface.blit(text_title_highscore,(60,20))
                scores = getScoresDesc("Hard")
                for row in scores:
                    text = SCORE_FONT.render("Position " + str(i+1) + " :  " + row[2] + " with " + str(row[1]) + " points",1,(0,0,0))
                    surface.blit(text,(60,200 + 50*i))
                    i+=1

                pygame.draw.rect(surface, (0,0,0), (20, 100, 100, 40), 2)
                text_easy = SCORE_FONT.render("EASY",1,(0,0,0))
                surface.blit(text_easy,(40,110))
                
                pygame.draw.rect(surface, (0,0,0), (190, 100, 130, 40), 2)                        
                text_medium = SCORE_FONT.render("MEDIUM",1,(0,0,0))
                surface.blit(text_medium,(200,110))

                pygame.draw.rect(surface, (0,0,0), (400, 100, 100, 40), 2)
                text_hard = SCORE_FONT.render("HARD",1,(200,0,200))
                surface.blit(text_hard,(420,110))
                pygame.display.update()        


def player_name(name):
    global PLAYER_NAME
    PLAYER_NAME = name

def set_difficulty(value, difficulty):
    global DIFFICULTY
    DIFFICULTY = value

def display_menu():
    def startGame():
        if test.get_value() == "":
            pass
        else:
            menu.disable()
            start_the_game()
    
    def highScore():
        menu.disable()
        seeHighScore()

    win_menu = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    menu = pygame_menu.Menu('FUCK J1\'S', 550, 800,theme=pygame_menu.themes.THEME_BLUE)
    test=menu.add.text_input('Name :',onchange=player_name,default=" ")
    menu.add.button('Play', startGame)
    menu.add.selector('Difficulty :', [('Hard', 1), ('Medium',2),('Easy', 3)], onchange=set_difficulty, default=1)
    menu.add.button('Top 10', highScore)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(win_menu)

def main():
    display_menu()

main()