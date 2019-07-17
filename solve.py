
class Card:
    def __init__(self, colors):
        self.top, self.right, self.bot, self.left = colors

    def rotate(self):
        # top -> right (clockwise)
        self.right, self.bot, self.left, self.top = colors

