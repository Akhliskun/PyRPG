import pygame
import random

from settings import *




# Game Loop
running = True
while running:
    '''
    Loop Logic:
        - Sets the tick rate at which the loop runs
        - Look for events (such as movement, attack, closing the game, etc)
        - Update the game logic
        - Draw everything
        - Double buffer
    '''
    # keep this running at the FPS defined above.
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw / Render
    screen.fill(BLACK)


    #####################
    # Double  buffering, this is a performance trick.
    # This always needs to happens after everything that we need to draw!
    #####################
    pygame.display.flip()
    print(int(clock.get_fps()))


# Closing everything.
pygame.quit()
