class Card:
    def __init__(self, colors):
        self.top, self.right, self.bot, self.left = colors

    def rotate(self):
        # top -> right (clockwise)
        self.right, self.bot, self.left, self.top = colors

WIDTH  = 3
HEIGHT = 3
EMPTY_BOARD = [None for _ in range(WIDTH*HEIGHT)]

def solve(cards, board = EMPTY_BOARD, pos = 0):
    for i, c in enumerate(cards):
        # place card
        if place(board, c, pos):
            remaining_cards = cards[:i] + cards[i+1:]
            # recurse
            if solve(remaining_cards, board, pos + 1):
                # if success, return
                return True
        # if we're here, we failed, undo, do next
        board[pos] = None

    # None worked, we failed
    return False

def place(board, card, pos):
    row, col = pos_to_rc(pos)
    for _ in range(4):
        fits = True
        if row > 0:
            above = rc_to_pos(row-1, col)
            if above.bot != card.top:
                fits = False
        if col > 0:
            # check
            left = rc_to_pos(row, col-1)
            if left.right != card.left:
                fits = False

        if fits:
            board[pos] = card
            return True
        else:
            card.rotate()

    # None fit, we fail...
    return False

def rc_to_pos(row, col):
    return WIDTH*row + col

def pos_to_rc(pos):
    row = pos // WIDTH
    col = pos  % WIDTH
    return (row, col)

