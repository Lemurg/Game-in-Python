import pygame

class Button:
    '''Класс для создания кнопок'''
    def __init__(self, x, y, width, height, text, image_path=None, hover_image_path=None):
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = pygame.image.load(hover_image_path) if hover_image_path else self.image
        self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_hovered = False


    def draw(self, screen):
        '''Отрисовывает кнопку на экране'''
        curent_image = self.hover_image if self.is_hovered else self.image
        screen.blit(curent_image, self.rect)
        
        if self.text:
            font = pygame.font.SysFont(None, 36)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    
    def check_hover(self, mouse_pos):
        '''Проверяет, находится ли мышь над кнопкой'''
        self.is_hovered = self.rect.collidepoint(mouse_pos) 


    def handle_event(self, event):
        '''Обрабатывает события мыши'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {'button': self}))