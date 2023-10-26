import pygame
import random

class scoreBoard(pygame.sprite.Sprite):
    """docstring for scoreBoard."""

    def __init__(self, font,color,size,lives):
        super(scoreBoard, self).__init__()
        self.font = self.font = pygame.font.Font(None, 36)
        self.size = size
        self.color = color
        self.value = 0
        self.lives = lives
        #initBoard()

    def updatelife(self):
        self.lives -= 1
    def updatepoints(self,points=1):
        self.value += points

    def update(self,values):
        self.value = values[0]
        self.lives = values[1]
        #print(f"The vlaues are {values}")

    def display(self,screen):
        score_text = self.font.render(f"Score: {self.value}", True, (255, 255, 255))
        lives_text = self.font.render(f" :) {self.lives}", True, (255,255,255)) 
        screen.blit(lives_text,(500,10))
        screen.blit(score_text, (10, 10))
