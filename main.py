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

# Cell width and height (including the stretching)
CELL_WIDTH = (WINDOW_WIDTH - 10) // BOARD_COLS
CELL_HEIGHT = (WINDOW_HEIGHT - 10) // BOARD_ROWS

def draw_board(screen):
    screen.fill(WHITE)

    # Calculate the board dimensions
    board_width = CELL_WIDTH * BOARD_COLS
    board_height = CELL_HEIGHT * BOARD_ROWS

    # Calculate the offset to center the board
    x_offset = (WINDOW_WIDTH - board_width) // 2
    y_offset = (WINDOW_HEIGHT - board_height) // 2

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            x = x_offset + col * CELL_WIDTH
            y = y_offset + row * CELL_HEIGHT

            # Determine the cell color based on the row
            if row < BOARD_ROWS // 2:
                color = GRAY
            else:
                color = WHITE

            pygame.draw.rect(screen, color, (x, y, CELL_WIDTH, CELL_HEIGHT))
            pygame.draw.rect(screen, BLACK, (x, y, CELL_WIDTH, CELL_HEIGHT), 1)

    # Draw horizontal lines
    for row in range(BOARD_ROWS + 1):
        y = y_offset + row * CELL_HEIGHT
        pygame.draw.line(screen, BLACK, (x_offset, y), (x_offset + board_width, y), 1)

    # Draw vertical lines
    for col in range(BOARD_COLS + 1):
        x = x_offset + col * CELL_WIDTH
        pygame.draw.line(screen, BLACK, (x, y_offset), (x, y_offset + board_height), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Game of Generals")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

