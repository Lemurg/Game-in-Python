import pygame

'''Конфигурация игры'''
WIDTH = 1366
HEIGHT = 768
NUMBER_OF_ASTEROIDS = 5
RUNNING = True


'''Цвета'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


'''Изображения'''
player = pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/player.png')
asteroid = pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/asteroid.png')
bg_image = pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/background.jpg')


'''Звуки'''
pygame.mixer.init()
bg_sound = pygame.mixer.Sound('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/sounds/background.mp3')
shot_sound = pygame.mixer.Sound('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/sounds/shot.mp3')
hit_sound = pygame.mixer.Sound('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/sounds/hit.mp3')
explosion_sound = pygame.mixer.Sound('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/sounds/explosion.mp3')
asteroid_sound = pygame.mixer.Sound('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/sounds/asteroid.mp3')


'''Функции'''
def print_text(text, x=0, y=0, font_size=48, color=WHITE, center=False, x_add=0, y_add=0):
    '''Выводит текст на экран'''
    if pygame.display.get_surface() is None:
        pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(text, True, color)
    if center:
        x = ((WIDTH - text_surface.get_width()) // 2) + x_add
        y = ((HEIGHT - text_surface.get_height()) // 2) + y_add
    pygame.display.get_surface().blit(text_surface, (x, y))
    pygame.display.flip()
    