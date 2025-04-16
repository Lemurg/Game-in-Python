import pygame, sys

def events(ship):
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: sys.exit() #Выход из игры

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    ship.rect.centerx += 10

                if event.key == pygame.K_a:
                    ship.rect.centerx -= 10
                

            

    