import pygame, sys, time, random
from bullet import Bullet
from asteroid import Asteroids
from stats import Stats
from config import NUMBER_OF_ASTEROIDS, HEIGHT, BLACK, shot_sound, hit_sound, bg_sound, explosion_sound, asteroid_sound, print_text


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
                    shot_sound.set_volume(0.05)
                    shot_sound.play()

                elif event.key == pygame.K_p:
                    pause_game(Stats, screen)
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    ship.mright = False

                elif event.key == pygame.K_a:
                    ship.mleft = False       

                elif event.key == pygame.K_ESCAPE:
                    sys.exit()


def create_asteroid(screen, asteroids, number_of_asteroids, stats):
    '''Создает одну полосу астероидов'''
    for _ in range(number_of_asteroids):  # Количество астероидов
        asteroid = Asteroids(screen, asteroid_speed(stats))
        asteroid.rect.x = random.randint(0, screen.get_width() - asteroid.rect.width)
        asteroid.rect.y = random.randint(0, 100)
        asteroids.add(asteroid)


def update_screen(bg_image, screen, scoreboard, ship, asteroids, bullets, bg_y):
    '''Обновляет экран и выводит на него корабль, астероиды и пули'''
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, bg_y))
    screen.blit(bg_image, (0, bg_y - HEIGHT))
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
            asteroid_sound.set_volume(0.12)
            asteroid_sound.play()


def update_asteroids(ship, asteroids, stats, screen, bullets):
    '''Обновляет астероиды и проверяет на столкновения с кораблем'''
    asteroids.update()
    for asteroid in asteroids.copy():
        if asteroid.rect.top >= 768:
            asteroids.remove(asteroid)
    if pygame.sprite.spritecollideany(ship, asteroids):
        ship_kill(stats, ship, bullets, asteroids, screen)
    # Если хотя бы один астероид прошёл первые 100 пикселей сверху, создать новую волну
    if asteroid.rect.top >= 100:
        create_asteroid(screen, asteroids, NUMBER_OF_ASTEROIDS, stats)
    # Если все астероиды ушли вниз или их уничтожили, создать новую волну
    if len(asteroids) == 0:
        create_asteroid(screen, asteroids, NUMBER_OF_ASTEROIDS, stats)


def ship_kill(stats, ship, bullets, asteroids, screen):
    '''Изменяет состояние игры при столкновении корабля с астероидом'''
    if stats.ships_left > 0:
        hit_sound.set_volume(0.30)
        hit_sound.play()
        stats.ships_left -= 1
        bullets.empty()
        asteroids.empty()
        ship.center = ship.screen_rect.centerx
        ship.rect.bottom = ship.screen_rect.bottom
        ship.rect.move_ip(0,-20)
        time.sleep(1)
    else:
        screen.fill(BLACK)
        print_text("Game Over", font_size=96, center=True)
        print_text(f"Score: {stats.score}",font_size=48, center=True, y_add=50)
        explosion_sound.set_volume(0.2)
        explosion_sound.play()
        bg_sound.stop()
        stats.game_active = False
        while not stats.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        reset_game(stats, screen, ship, bullets, asteroids)


def check_high_score(stats, scoreboard):
    '''Проверяет, является ли текущий счет рекордным'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.score_high()
        with open('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/highscore.txt', 'w') as file:
            file.write(str(stats.high_score))


def pause_game(stats, screen):
    '''Пауза игры'''
    stats.game_active = False
    screen.fill(BLACK)
    bg_sound.stop()
    print_text("Game Paused, press 'P' to continue", 0, 0, font_size=96, center=True)
    
    while not stats.game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stats.game_active = True
                    bg_sound.play(loops=-1)
                    pygame.display.flip()


def reset_game(stats, screen, ship, bullets, asteroids):
    '''Сбрасывает игру'''
    stats.reset_stats()
    stats.game_active = True
    bullets.empty()
    asteroids.empty()
    ship.center = ship.screen_rect.centerx
    ship.rect.bottom = ship.screen_rect.bottom
    ship.rect.move_ip(0, -20)
    bg_sound.play(loops=-1)
    screen.fill(BLACK)
    print_text("Game Reset", font_size=96, center=True)
    time.sleep(1)


def asteroid_speed(stats, base_speed=0.3, speed_increment=0.1, score_step=500):
    '''Увеличивает скорость астероидов в зависимости от счета'''
    speed = base_speed + (stats.score // score_step) * speed_increment
    return speed