import pygame
from pygame.locals import *
from time import *

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Rocket in space')

player_x = 200
player_y = 200

#load the image 
player = pygame.image.load('rocket.png')
background = pygame.image.load('background.png')
keys = [False,False,False,False]

while player < 600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.update()

    #events loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0]=True
            if event.key == K_DOWN:
                keys[1]=True 
            if event.key == K_LEFT:
                keys[2]=True
            if event.key == K_RIGHT:
                keys[3]=True

        
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0]=False
            if event.key == K_DOWN:
                keys[1]=False
            if event.key == K_LEFT:
                keys[2]=False
            if event.key == K_RIGHT:
                keys[3]=False

    if keys[0]:
        if player_y > 0 :
            player_y -=7

    elif keys[1]:
        if player_y < 550:
            player_y +=7

    elif keys[2]:
        if player_y > 0:
            player_y -=7

    elif keys[1]:
        if player_y < 600:
            player_y +=7
print('Game over')
