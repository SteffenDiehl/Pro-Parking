import pygame

# Initialize Pygame
pygame.init()

# Set the window size
size = (700, 500)
screen = pygame.display.set_mode(size)

# Load the image
thiscar = pygame.image.load("redcar.png")

# Get the image's rect
thiscar_rect = thiscar.get_rect()

# Initialize the image's position
thiscar_rect.x = 0
thiscar_rect.y = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Erase the previous position of the image
    screen.fill((0, 0, 0))

    # Update the image's position
    thiscar_rect.x += 5
    thiscar_rect.y += 5

    # Blit the image onto the screen
    screen.blit(thiscar, thiscar_rect)

    # Update the display
    pygame.display.flip()

# Exit Pygame
pygame.quit()