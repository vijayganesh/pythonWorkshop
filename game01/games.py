import pygame
import sys

pygame.init()

# Set up the display
displaySize = (800,600)
screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("First Games Window")
# Change the background COlor
backgroundColor = pygame.Color("#ff9671")
screen.fill(backgroundColor)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic and rendering go here

pygame.quit()
sys.exit()
