import pygame

class Asteroids(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(Asteroids, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('C:/Users/fjvfh/Documents/GitHub/Game-in-Python/Progect Game/img/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        self.y += 0.1
        self.rect.y = self.y

    
    def draw(self):
        self.screen.blit(self.image, self.rect)