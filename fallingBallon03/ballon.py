import pygame
import random

class FallingCircle(pygame.sprite.Sprite):
    def __init__(self,window_height,window_width,velocity):
        super().__init__()
        self.radius = 20
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, window_width)
        self.rect.y = 0
        self.velocity = velocity

    def update(self):
        self.rect.y += self.velocity  # Adjust the speed at which circles fall
