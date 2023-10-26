import pygame
import random

class scoreBoard(pygame.sprite.Sprite):
    """docstring for scoreBoard."""

    def __init__(self, font,color,size):
        super(scoreBoard, self).__init__()
        self.font = self.font = pygame.font.Font(None, 36)
        self.size = size
        self.color = color
        self.value = "0"
        #initBoard()

    def update(values):
        self.value = values

    def display(self,screen):
        score_text = self.font.render(f"Score: {self.value}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
