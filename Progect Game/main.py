import pygame, controls
from ship import Ship

def run():

    WIDTH = 1366
    HEIGHT = 768

    pygame.init()
    screan = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Космические падальщики')
    bg_color = (0, 0, 0)
    ship = Ship(screan)
    
    while True:
        controls.events(ship)

        screan.fill(bg_color)
        ship.output()
        pygame.display.flip()

    

run()