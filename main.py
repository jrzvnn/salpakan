import pygame
import sys

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Board dimensions
BOARD_ROWS = 8
BOARD_COLS = 9

# Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

# Cell width and height (in pixels)
CELL_WIDTH_CM = 4  # Width of each cell in centimeters
CM_TO_PIXEL_RATIO = 37.7952755906  # Conversion ratio from centimeters to pixels
CELL_WIDTH = int(CELL_WIDTH_CM * CM_TO_PIXEL_RATIO)
CELL_HEIGHT = WINDOW_HEIGHT // BOARD_ROWS

# Piece class
class Piece:
    def __init__(self, image, rank, player):
        self.image = image
        self.rect = self.image.get_rect()
        self.rank = rank
        self.player = player
        self.dragging = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_position(self, pos):
        if self.dragging:
            self.rect.center = pos

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Draggable Pieces")

# Load piece images
piece_image_white = pygame.image.load("assets/images/five_star_general_white.png")
piece_image_black = pygame.image.load("assets/images/five_star_general_black.png")

# Create pieces
piece_white = Piece(piece_image_white, "Five Star General", "white")
piece_black = Piece(piece_image_black, "Five Star General", "black")

pieces = [piece_white, piece_black]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for piece in pieces:
            piece.handle_event(event)

    screen.fill(WHITE)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            x = col * CELL_WIDTH + 40  # Adjust the starting x position
            y = row * CELL_HEIGHT + 40  # Adjust the starting y position

            # Determine the cell color based on the row
            if row < BOARD_ROWS // 2:
                color = GRAY
            else:
                color = WHITE

            pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_WIDTH, CELL_HEIGHT), 1)

    for piece in pieces:
        piece.update_position(pygame.mouse.get_pos())
        piece.draw(screen)

        if not piece.dragging:
            # Determine the cell position based on piece position
            col = int((piece.rect.centerx - 40) // CELL_WIDTH)  # Adjust the starting x position
            row = int((piece.rect.centery - 40) // CELL_HEIGHT)  # Adjust the starting y position

            # Calculate the cell coordinates
            cell_x = col * CELL_WIDTH + 40  # Adjust the starting x position
            cell_y = row * CELL_HEIGHT + 40  # Adjust the starting y position

            # Assign the piece to the cell
            piece.rect.center = (cell_x + CELL_WIDTH // 2, cell_y + CELL_HEIGHT // 2)

    pygame.display.flip()

