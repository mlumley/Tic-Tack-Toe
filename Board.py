from Error import InvalidActionError

class Board():
    """
    Represents a square board of size n that players can mark their symbol on
    to play Tic-Tac-Toe
    """
    def __init__(self, size):
        self.board = [['.' for i in range(size)] for j in range(size)]
        self.numMoves = 0

    def printBoard(self):
        """
        Prints the current state of the board to the terminal
        """
        print("Here's the current board:")
        for row in self.board:
            print(' '.join(row))
        print('\n')

    def markBoard(self, player, coordinate):
        """
        Places the player's symbol at the coordinate on the board
        """
        self.validateAction(coordinate)
        self.board[coordinate.x][coordinate.y] = player.symbol
        self.numMoves = self.numMoves + 1

    def validateAction(self, coordinate):
        """
        Validate that the coordinate is a valid position on the board
        and unoccupied
        """
        if coordinate.x < 0 or coordinate.x >= len(self.board) or coordinate.y < 0 or coordinate.y >= len(self.board):
            raise InvalidActionError("Error: Please enter a coord x,y between 1 and " + str(len(self.board)))
        
        elif self.board[coordinate.x][coordinate.y] != '.':
            raise InvalidActionError("Error: There is already a piece at this position. Try again")

    def hasWon(self):
        """
        Check if there is a winner on the board
        """
        won = False

        # Check rows
        for row in self.board:
            if row[1:] == row[:-1] and row[0] != '.':
                won = True
        
        # Check columns
        tBoard = map(list, zip(*self.board))
        for row in tBoard:
            if row[1:] == row[:-1] and row[0] != '.':
                won = True

        # Check diagonals
        diagDown = []
        diagUp = []
        for i in range(0, len(self.board)):
            diagDown.append(self.board[i][i])
            diagUp.append(self.board[i][len(self.board)-i-1])
        if diagDown[1:] == diagDown[:-1] and diagDown[0] != '.' or diagUp[1:] == diagUp[:-1] and diagUp[0] != '.':
            won = True

        return won

    def hasDrawn(self):
        """
        Check if a draw has occured
        """
        return self.numMoves >= len(self.board)**2