from config import asteroid
import pygame

class Asteroids(pygame.sprite.Sprite):
    '''Класс для создания астероидов'''
    def __init__(self, screen, speed=0.5):
        super(Asteroids, self).__init__()
        self.screen = screen
        self.image = asteroid
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed = speed


    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    
    def draw(self):
        self.screen.blit(self.image, self.rect)