import pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Circle in Pygame")

# Set circle parameters
circle_x = 400
circle_y = 300
circle_radius = 20
circle_speed = 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update circle position
    circle_x += circle_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), circle_radius)

    # Update display
    pygame.display.flip()

pygame.quit()
