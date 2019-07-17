
class Card:
    def __init__(self, colors):
        self.top, self.right, self.bot, self.left = colors

    def rotate(self):
        # top -> right (clockwise)
        self.right, self.bot, self.left, self.top = colors

def solve(cards, board = []):
    for c in cards:
        # place card
        # recurse
        #  if fail, undo, do next
        #  if success, return
    #failed

def rc_to_pos(row, col):
    return 3*row + col

def pos_to_rc(pos):
    row = pos // 3
    col = pos  % 3
    return (row, col)

def place(board, card, pos):
    row, col = pos_to_rc(pos)
    if row > 0:
        # check
    if col > 0:
        # check

