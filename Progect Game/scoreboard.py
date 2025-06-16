import pygame.font

class Scoreboard:
    '''Класс для вывода игровой статистики'''
    def __init__(self, screen, stats):
        WHITE = (255, 255, 255)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (WHITE)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.score_high()

    def prep_score(self):
        '''Преобразует текущий счет в графическое изображение'''
        BLACK = (0, 0, 0)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (BLACK))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def score_high(self):
        '''Преобразует рекордный счет в графическое изображение'''
        BLACK = (0, 0, 0)
        high_score_str = str(self.stats.high_score)
        self.score_image_high = self.font.render(high_score_str, True, self.text_color, (BLACK))
        self.score_rect_high = self.score_image_high.get_rect()
        self.score_rect_high.centerx = self.screen_rect.centerx
        self.score_rect_high.top = 20

    def show_score(self):
        '''Выводит счета, жизней на экран'''
        RED = (255, 0, 0)
        self.screen.blit(self.score_image, self.score_rect)
        ships = self.stats.ships_left
        for ship_number in range(ships + 1):
            ship_rect = pygame.Rect(10 + ship_number * 30, 10, 20, 20)
            pygame.draw.rect(self.screen, RED, ship_rect)
        self.screen.blit(self.score_image_high, self.score_rect_high)