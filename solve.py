class Card:
    def __init__(self, colors, dirs):
        self.top, self.right, self.bot, self.left = colors

        self.top_dir, self.right_dir, self.bot_dir, self.left_dir = dirs

    def rotate(self):
        # top -> right (clockwise)
         self.right, self.bot, self.left, self.top = (
           self.top, self.right, self.bot, self.left)

         self.right_dir, self.bot_dir, self.left_dir, self.top_dir = (
           self.top_dir, self.right_dir, self.bot_dir, self.left_dir)



    def __str__(self):
        colors = [self.top, self.right, self.bot, self.left]
        dirs = [self.top_dir, self.right_dir, self.bot_dir, self.left_dir]
        return " ".join(c+"-"+d for c, d in zip(colors, dirs))

WIDTH  = 3
HEIGHT = 3
EMPTY_BOARD = [None for _ in range(WIDTH*HEIGHT)]


def solve(cards, board = EMPTY_BOARD, pos = 0):
    if len(cards) == 0:
        return True, board

    for i, c in enumerate(cards):
        # place card
        for _ in range(4):
            if place(board, c, pos):
                board[pos] = c
                remaining_cards = cards[:i] + cards[i+1:]
                # recurse
                solved, board = solve(remaining_cards, board, pos + 1)
                if solved:
                    # if success, return
                    return True, board
            c.rotate()

            # if we're here, we failed, undo, do next
            board[pos] = None

    # None worked, we failed
    board[pos] = None
    return False, board

counter = 0
def place(board, card, pos):
    global counter
    counter += 1
    row, col = pos_to_rc(pos)

    fits = True
    if row > 0:
        above_pos = rc_to_pos(row-1, col)
        above = board[above_pos]
        if above.bot     != card.top or \
           above.bot_dir == card.top_dir:
            fits = False
    if col > 0:
        # check
        left_pos = rc_to_pos(row, col-1)
        left = board[left_pos]
        if left.right     != card.left or \
           left.right_dir == card.left_dir:
            fits = False

    return fits

def rc_to_pos(row, col):
    return WIDTH*row + col

def pos_to_rc(pos):
    row = pos // WIDTH
    col = pos  % WIDTH
    return (row, col)

colors = [
        ['bl', 'br', 'bl', 'or'],
        ['br', 'bl', 'br', 'gr'],
        ['or', 'br', 'br', 'bl'],
        ['or', 'or', 'bl', 'gr'],

        ['br', 'or', 'bl', 'br'],
        ['or', 'bl', 'gr', 'or'],
        ['br', 'gr', 'bl', 'gr'],
        ['or', 'gr', 'gr', 'or'],
        ['bl', 'gr', 'gr', 'bl'],
        ]

dirs = [
        ['o',  'i',  'i',  'o'],
        ['i',  'i',  'o',  'o'],
        ['i',  'o',  'o',  'i'],
        ['i',  'o',  'o',  'i'],

        ['i',  'i',  'o',  'o'],
        ['i',  'o',  'o',  'i'],
        ['o',  'o',  'i',  'i'],
        ['i',  'i',  'o',  'o'],
        ['o',  'o',  'i',  'i'],
        ]

cards = [Card(cols, dirs) for cols, dirs in zip(colors, dirs)]
board = EMPTY_BOARD

s, board = solve(cards, board)
print(counter)
print([str(c) for c in board])
