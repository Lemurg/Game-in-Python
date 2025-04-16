import pygame, sys
from bullet import Bullet

def events(ship, screen, bullets):
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


def update_screen(bg_color, screen, ship, asteroid, bullets):
    screen.fill(bg_color)
    for bullets in bullets.sprites():
        bullets.draw_bullet()
    ship.output()
    asteroid.draw()
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_asteroids(asteroids):
    asteroids.update()