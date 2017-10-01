
from pprint import pprint
import random


def getBoard():
    return [[" "] * 3 for i in range(3)]


def displayBoard(board):

    print("----" * len(board))
    for i in range(len(board)):
        print("| ", end="")
        for j in range(len(board[i])):
            print(board[i][j], end=" | ")
        print()
        print("----" * len(board))


def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')


def inputPlayerLetter():
    print("would you like to be 'O' or 'X'?")
    ans = input().upper()
    if ans == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst(player, opponent):
    if random.randint(0,1) == 0:
        print("player goes first")
        return player
    else:
        print("opponent goes first")
        return opponent


def isSpaceFree(board, i, j):
    return board[i][j] == " "

def isFilled(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isSpaceFree(board, i, j):
                return False
    return True


def gameWon(board, turn):
    return (board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == turn) or \
    (board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == turn) or \
    (board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == turn) or \
    (board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == turn) or \
    (board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == turn) or \
    (board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == turn) or \
    (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == turn) or \
    (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == turn)


def isValid(board, ans):
    try:
        x, y = map(int, ans.split())
    except:
        print("invalid input")
        return False

    if not (0 <= x <= 2 and 0 <= y <= 2):
        print("That space is not in the board. invalid!")
        return False

    if board[x][y] != ' ':
        print("That space is already occupied!")
        return False

    return True

def enterCoord(board):
    print("please enter a valid coordinate such as '0 0' or '1 1'")
    ans = input()

    while not isValid(board, ans):
        print("please enter a valid coordinate such as '0 0' or '1 1'")
        ans = input()

    x, y = map(int, input().split())
    return x, y


def AIMove(board, turn):
    if turn == 'X':
        player = 'O'
    else:
        player = 'X'

    # check if we can win in next move:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isSpaceFree(board, i, j):
                board[i][j] = turn

                if gameWon(board, turn):
                    return

                board[i][j] = " "


    # check if player can win in next move. If so block it
    for i in range(len(board)):
        for j in range(len(board[i])):
            if isSpaceFree(board, i, j):
                board[i][j] = player

                if gameWon(board, player):
                    board[i][j] = turn
                    return

                board[i][j] = " "

    # try to take one of the corners if free
    for k in [(0,0), (0,2), (2,0), (2,2)]:
        i, j = k
        if isSpaceFree(board, i, j):
            board[i][j] = turn
            return


    # try to take the center if its free
    if isSpaceFree(board, 1, 1):
        board[1][1] = turn
        return


    # try to take one of the sides.
    for k in [(0,1),(1,0), (1,2),(2,1)]:
        i, j = k
        if isSpaceFree(board, i, j):
            board[i][j] = turn
            return


def main():
    print("Welcome to a game of tic tac toe!")

    while True:
        board = getBoard()

        displayBoard(board)

        player, opponent = inputPlayerLetter()
        turn = whoGoesFirst(player, opponent)

        while True:

            if turn == player:
                print("player's turn")
                x, y = enterCoord(board)
                board[x][y] = turn

                if gameWon(board, player):
                    print("Congrats!! Player won!")
                    break
            else:
                print("opponent's turn")
                AIMove(board, turn)

                if gameWon(board, turn):
                    print("Sorry. You lose. Computer won")
                    break

            if isFilled(board):
                print("Game is tied")
                break

            if turn == player:
                turn = opponent
            else:
                turn = player


            displayBoard(board)

        displayBoard(board)

        if not playAgain():
            break


if __name__ == "__main__":
    main()

