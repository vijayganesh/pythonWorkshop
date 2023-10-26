import pygame

class Actor(pygame.sprite.Sprite):
    def __init__(self,window_width,window_height):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width // 2
        self.rect.y = window_height - 60
        self.speed = 20
        self.window_width = window_width
        self.window_height = window_height

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < self.window_width:
            self.rect.x += self.speed
