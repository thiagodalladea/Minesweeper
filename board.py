class Board():
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.makeBoard()

    def makeBoard(self):
        self.board = []
        