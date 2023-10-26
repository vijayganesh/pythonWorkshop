import pygame
import sys
import ballon as fc
import random
import scoreBoard as sc

pygame.init()

# Set up the display
window_width = 600
window_height = 800
clock = pygame.time.Clock()
FPS = 12
displaySize = (window_width,window_height)
screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("First Games Window")
# Change the background COlor
backgroundColor = pygame.Color("#ff9671")
screen.fill(backgroundColor)
pygame.display.flip()

falling_circles = pygame.sprite.Group()
scoreboard = sc.scoreBoard(font="none",color=(255,255,255),size=24)
speed = 100;
# this should be 1 to have max speed
genTrue = 0


running = True
while running:
    dt = clock.tick(FPS) / speed
    genTrue += 1;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the falling circles
    for circle in falling_circles:
        circle.update()

        # Remove the circle if it hits the bottom boundary
        if circle.rect.top > window_height:
            circle.kill()

    # Create and add new falling circles if needed
    #if len(falling_circles) < 5:
    #    circle = fc.FallingCircle(displaySize[0],displaySize[1],dt)
    #    falling_circles.add(circle)
    if genTrue == speed/2:
        genTrue = 0
        circle = fc.FallingCircle(window_height,window_width,dt)
        falling_circles.add(circle)

    # Clear the screen
    screen.fill(backgroundColor)

    # Draw the falling circles
    falling_circles.draw(screen)

    # Update ScoreBaord
    scoreboard.display(screen)

    # Update the display
    pygame.display.flip()



pygame.quit()
sys.exit()
