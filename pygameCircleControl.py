import pygame
pygame.init()

# Set up the display
window_width, window_height = 800, 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moving Circle in Pygame")

# Set circle parameters
circle_x = window_width // 2
circle_y = window_height // 2
circle_radius = 20
circle_speed = 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input (if needed)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and circle_x > circle_radius:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT] and circle_x < window_width - circle_radius:
        circle_x += circle_speed
    if keys[pygame.K_UP] and circle_y > circle_radius:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN] and circle_y < window_height - circle_radius:
        circle_y += circle_speed

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the circle
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y), circle_radius)

    # Update display
    pygame.display.flip()

pygame.quit()
