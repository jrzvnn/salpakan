class Piece:
    def __init__(self, rank, player):
        self.rank = rank
        self.player = player

    def capture(self, target_piece):
        if self.rank == "Spy" and target_piece.rank == "Private":
            return True
        return RANKS[self.rank] > RANKS[target_piece.rank]


RANKS =  {
    "Five Star General": 12,
    "Four Star General": 11,
    "Three Star General": 10,
    "Two Star General": 9,
    "One Star General": 8,
    "Colonel": 7,
    "Lt. Colonel": 6,
    "Major": 5,
    "Captain": 4,
    "1st Lieutenant": 3,
    "2nd Lieutenant": 2,
    "Sergeant": 1,
    "Private": 0,

}
