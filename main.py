import pygame
import sys

pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salpakan")

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    pygame.display.flip()  # Update the contents of the entire display
    clock.tick(60)  # Limit the frame rate to 60 FPS
