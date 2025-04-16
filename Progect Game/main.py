import pygame, controls
from ship import Ship
from pygame.sprite import Group
from asteroid import Asteroids

def run():

    WIDTH = 1366
    HEIGHT = 768

    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Космические падальщики')
    bg_color = (BLACK)
    ship = Ship(screen)
    bullets = Group()
    asteroid = Asteroids(screen)
    
    while True:
        controls.events(ship, screen, bullets)
        ship.update_ship()
        controls.update_screen(bg_color, screen, ship, asteroid, bullets)
        controls.update_bullets(bullets)
        controls.update_asteroids(asteroid)

    
run()