from config import RUNNING as running, WIDTH, HEIGHT, bg_image, bg_sound_play, bg_sound, start_button, exit_button
from button import Button
from stats import Stats
import pygame, sys, initiate


def main():
    '''Главная функция для запуска игры'''
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Космические падальщики')
    pygame.display.set_icon(pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/asteroid.png'))
    Stats().game_active = False

    '''Инициализация звуков'''
    pygame.mixer.init()
    bg_sound.set_volume(0.02)
    bg_sound.play(loops=-1)
    bg_sound_play.stop()
    

    while running:
        '''Основной цикл'''
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.USEREVENT:
                if event.button == start_button:
                    initiate.run(screen)

                elif event.button == start_button:
                    print('f')

                elif event.button == exit_button:
                    pygame.quit()
                    sys.exit()
            
            start_button.handle_event(event)
            exit_button.handle_event(event)

        start_button.check_hover(pygame.mouse.get_pos())
        exit_button.check_hover(pygame.mouse.get_pos())

        screen.blit(bg_image, (0, 0))
        start_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()