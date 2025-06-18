from config import player
import pygame

class Ship():
    '''Инициализация корабля'''
    def __init__(self, screen):
        self.screen = screen
        self.image = player
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx 
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.rect.move_ip(0,-20)
        self.mright = False
        self.mleft = False

    
    def output(self):
        self.screen.blit(self.image, self.rect)

    
    def update_ship(self):
        SPEED = 1.5

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += SPEED

        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= SPEED

        self.rect.centerx = self.center