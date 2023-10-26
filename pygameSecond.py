import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Text in Pygame")

# Choose a font
font = pygame.font.Font(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render text
    text = font.render("Welcome to SJEC ", True, (255, 255, 255))

    # Display text
    screen.blit(text, (300, 250))

    # Update display
    pygame.display.flip()
pygame.quit()
