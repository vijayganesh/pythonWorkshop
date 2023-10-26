import pygame
import sys
import ballon as fc
import random
import scoreBoard as sc
import actor as ac

pygame.init()

# Set up the display
window_width = 600
window_height = 800
clock = pygame.time.Clock()
FPS = 12
lives = 3
displaySize = (window_width,window_height)
screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("First Games Window")
# Change the background COlor
backgroundColor = pygame.Color("#ff9671")
screen.fill(backgroundColor)
pygame.display.flip()
actor = ac.Actor(window_width,window_height)
falling_circles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(actor)
scoreboard = sc.scoreBoard(font="none",color=(255,255,255),size=24,lives=lives)
speed = 100
# this should be 1 to have max speed
genTrue = 0
scores = 0
#scoreupdate = (scores,lives)
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
            #lives -= 1
            #scoreboard.update([scores,lives])
            scoreboard.updatelife()
            if(scoreboard.lives <= 0):
                running = False

        # Check for collisions with the actor
        if pygame.sprite.collide_rect(circle, actor):
            #running = False  # End the game on collision
            scores += 1
            scoreboard.updatepoints()
            #scoreboard.update([scores,lives])
            circle.kill()
    # Update the actor
    actor.update()

    # Create and add new falling circles if needed
    #
    if genTrue == speed*4:
        genTrue = 0
        circle = fc.FallingCircle(window_height,window_width,dt)
        falling_circles.add(circle)

    # Clear the screen
    screen.fill(backgroundColor)

    # Draw the falling circles
    falling_circles.draw(screen)

    # Update ScoreBaord
    scoreboard.display(screen)

    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()


## Display the Game over message if lives are not available 

if scoreboard.lives <= 0:
    gameExitFont = pygame.font.Font(None,100)
    gameExit = scoreboard.font.render("Game Over  :( ", True, (255, 255, 255))
    gameExitRect = gameExit.get_rect(center=(window_width//2,window_height//2))
    screen.blit(gameExit,gameExitRect)
    pygame.display.flip()
    pygame.time.delay(2000)

pygame.quit()
sys.exit()
