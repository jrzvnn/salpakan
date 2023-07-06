class Game:
    def __init__(self):
        self.board = Board()  # Assuming a Board class exists for the game

    def move_piece(self, piece, direction):
        current_position = self.board.get_piece_position(piece)
        new_position = current_position

        if direction == "up":
            new_position = (current_position[0] - 1, current_position[1])
        elif direction == "down":
            new_position = (current_position[0] + 1, current_position[1])
        elif direction == "left":
            new_position = (current_position[0], current_position[1] - 1)
        elif direction == "right":
            new_position = (current_position[0], current_position[1] + 1)

        if self.is_valid_move(new_position):
            target_piece = self.board.get_piece_at_position(new_position)
            if target_piece is None:
                self.board.move_piece(piece, new_position)
            else:
                self.board.overlap_pieces(piece, target_piece)

    def is_valid_move(self, position):
        # Check if the new position is within the board boundaries
        if (
            position[0] >= 0
            and position[0] < self.board.rows
            and position[1] >= 0
            and position[1] < self.board.cols
        ):
            return True
        return False

