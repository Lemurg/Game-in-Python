import pygame, controls
from config import HEIGHT, WIDTH, NUMBER_OF_ASTEROIDS
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scoreboard import Scoreboard

def run():
    '''Запуск игры'''
    bg_y = 0
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Космические падальщики')
    pygame.display.set_icon(pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/asteroid.png'))
    pygame.mouse.set_visible(False)
    bg_image = pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/background.jpg')
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
    ship = Ship(screen)
    bullets = Group()
    asteroid = Group()
    stats = Stats()
    scoreboard = Scoreboard(screen, stats)
    controls.create_asteroid(screen, asteroid, NUMBER_OF_ASTEROIDS)
    
    
    while True:
        '''Основной цикл игры'''
        bg_y += 0.1
        controls.events(ship, screen, bullets)
        if stats.game_active:
            '''Обновление корабля, экрана, пуль и астероидов'''
            ship.update_ship()
            controls.update_screen(bg_image, screen, scoreboard, ship, asteroid, bullets, bg_y)
            controls.update_bullets(asteroid, stats, scoreboard, bullets)
            controls.update_asteroids(ship, asteroid, stats, screen, bullets)


if __name__ == '__main__':
    run()