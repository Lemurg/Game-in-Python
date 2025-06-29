import pygame

class Bullet(pygame.sprite.Sprite):
    '''Класс для создания пуль корабля'''
    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (139, 195, 74)
        self.speed = 10
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)