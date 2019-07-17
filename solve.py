class Card:
    def __init__(self, colors):
        self.top, self.right, self.bot, self.left = colors

    def rotate(self):
        # top -> right (clockwise)
        self.right, self.bot, self.left, self.top = colors

def solve(cards, board = [], pos = 0):
    for c in cards:
        # place card
        if place(board, c, pos):
            if solve(cards, board, pos + 1):
                return True
        # recurse
        #  if fail, undo, do next
        #  if success, return
    #failed
    return False

def place(board, card, pos):
    row, col = pos_to_rc(pos)
    for _ in range(4):
        fits = False
        if row > 0:
            # check
        if col > 0:
            # check

        if fits:
            return True
    return False

def rc_to_pos(row, col):
    return 3*row + col

def pos_to_rc(pos):
    row = pos // 3
    col = pos  % 3
    return (row, col)

