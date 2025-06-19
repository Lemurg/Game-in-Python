import controls
from config import HEIGHT, NUMBER_OF_ASTEROIDS, RUNNING as running, bg_sound_play, bg_image, bg_sound
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scoreboard import Scoreboard


def run(screen):
    '''Запуск игры'''
    stats = Stats()
    stats.game_active = True
    bg_y = 0

    '''Инициализация звука'''
    bg_sound_play.set_volume(0.2)
    bg_sound_play.play(loops=-1)
    bg_sound.stop()
    
    '''Инициализация корабля, пуль, астероидов, статистики и счётчика'''
    ship = Ship(screen)
    bullets = Group()
    asteroid = Group()
    scoreboard = Scoreboard(screen, stats)

    '''Создание астероидов'''
    controls.create_asteroid(screen, asteroid, NUMBER_OF_ASTEROIDS, stats)
    

    while running:
        '''Цикл игры'''
        bg_y += 0.1
        if bg_y >= HEIGHT:
            bg_y = 0

        controls.events(ship, screen, bullets)
        if stats.game_active:
            '''Обновление корабля, экрана, пуль и астероидов'''
            ship.update_ship()
            controls.update_screen(bg_image, screen, scoreboard, ship, asteroid, bullets, bg_y)
            controls.update_bullets(asteroid, stats, scoreboard, bullets)
            controls.update_asteroids(ship, asteroid, stats, screen, bullets)