import pygame, sys
from bullet import Bullet
from asteroid import Asteroids
from config import HEIGHT, NUMBER_OF_ASTEROIDS
import time
import random


def events(ship, screen, bullets):
    '''Обрабатывает события'''
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: sys.exit() #Выход из игры

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    ship.mright = True

                elif event.key == pygame.K_a:
                    ship.mleft = True

                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, ship)
                    bullets.add(new_bullet)
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    ship.mright = False

                elif event.key == pygame.K_a:
                    ship.mleft = False

                elif event.key == pygame.K_ESCAPE:
                    sys.exit()


def create_asteroid(screen, asteroids, number_of_asteroids):
    '''Создает одну полосу астероидов'''
    for _ in range(number_of_asteroids):  # Количество астероидов
        asteroid = Asteroids(screen)
        asteroid.rect.x = random.randint(0, screen.get_width() - asteroid.rect.width)
        asteroid.rect.y = random.randint(0, screen.get_height() - asteroid.rect.height)
        asteroids.add(asteroid)
    

def update_screen(bg_image, screen, scoreboard, ship, asteroids, bullets):
    '''Обновляет экран и реализует плавную прокрутку фона'''
    screen.fill((0, 0, 0))  # Очистка экрана
    screen.blit(bg_image, (0, 0))
    scoreboard.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    for asteroid in asteroids.sprites():
        asteroid.draw()
    pygame.display.flip()


def update_bullets(asteroids, stats, scoreboard, bullets):
    '''Обновляет пули и проверяет на столкновения с астероидами'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, asteroids, True, True)
    if collisions:
        for asteroid in collisions.values():
            stats.score += 10 * len(asteroid)
            scoreboard.prep_score()
            check_high_score(stats, scoreboard)


def update_asteroids(ship, asteroids, stats, screen, bullets):
    '''Обновляет астероиды и проверяет на столкновения с кораблем'''
    asteroids.update()
    for asteroid in asteroids.copy():
        if asteroid.rect.top >= 768:
            asteroids.remove(asteroid)
    if pygame.sprite.spritecollideany(ship, asteroids):
        ship_kill(stats, ship, bullets, asteroids)
    # Если хотя бы один астероид прошёл первые 100 пикселей сверху, создать новую волну
    if asteroid.rect.top >= 100:
        create_asteroid(screen, asteroids, NUMBER_OF_ASTEROIDS)

    # Если все астероиды ушли вниз или их уничтожили, создать новую волну
    if len(asteroids) == 0:
        create_asteroid(screen, asteroids)


def ship_kill(stats, ship, bullets, asteroids):
    '''Изменяет состояние игры при столкновении корабля с астероидом'''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        bullets.empty()
        asteroids.empty()
        ship.center = ship.screen_rect.centerx
        ship.rect.bottom = ship.screen_rect.bottom
        time.sleep(1)
    else:
        print("Game Over")
        stats.game_active = False
        sys.exit()


def check_high_score(stats, scoreboard):
    '''Проверяет, является ли текущий счет рекордным'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.score_high()
        with open('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/highscore.txt', 'w') as file:
            file.write(str(stats.high_score))