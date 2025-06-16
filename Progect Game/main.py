import pygame, controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scoreboard import Scoreboard

def run():

    WIDTH = 1366
    HEIGHT = 768

    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Космические падальщики')
    pygame.display.set_icon(pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/asteroid.png'))
    pygame.mouse.set_visible(False)
    bg_color = (BLACK)
    ship = Ship(screen)
    bullets = Group()
    asteroid = Group()
    stats = Stats()
    scoreboard = Scoreboard(screen, stats)

    controls.create_asteroid(screen, asteroid)
    
    
    while True:
        controls.events(ship, screen, bullets, asteroid)
        if stats.game_active:
            '''Обновление корабля, экрана, пуль и астероидов'''
            ship.update_ship()
            controls.update_screen(bg_color, screen, stats, scoreboard, ship, asteroid, bullets)
            controls.update_bullets(asteroid, stats, scoreboard, bullets)
            controls.update_asteroids(ship, asteroid, stats, screen, bullets)

    
run()