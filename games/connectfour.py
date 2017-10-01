
from pprint import pprint
import random
from copy import deepcopy

BOARDHEIGHT = 6
BOARDWIDTH = 7

def getBoard():
	return [[" "] * BOARDWIDTH for i in range(BOARDHEIGHT)]


def choosePiece():
	print("Do you want to be X or O?")
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

def playAgain():
	print("Do you want to play again? (yes or no)")
	return input().lower()[0] == "y"

def displayBoard(board):
	print('----' * BOARDWIDTH)
	for i in range(BOARDHEIGHT):
		print("| ", end='')
		for j in range(BOARDWIDTH):
			print(board[i][j], end=' | ')
		print()
		print('----' * BOARDWIDTH)


def fullColumn(board, col):
	return board[0][col] != " "


def isValid(board, col):

	try:
		col = int(col)
	except:
		print("please enter an integer")
		return False

	if (col < 0 or col >= BOARDWIDTH):
		print("Invalid column")
		return False

	if fullColumn(board, col):
		print("column is full")
		return False

	return True

def chooseCol(board):
	print("Choose a column from 0 to 7")
	ans = input()

	# fix this
	while not isValid(board, ans):
		print("Choose a column from 0 to 7")
		ans = input()

	return int(ans)

def placeCol(board, col, turn):
	for i in range(BOARDHEIGHT-1, -1, -1):
		if board[i][col] == " ":
			board[i][col] = turn
			return

def win(board, turn):
	# check horizontal
	for i in range(BOARDHEIGHT):
		for j in range(BOARDWIDTH-3):
			if (board[i][j] == turn and board[i][j+1] == turn and board[i][j+2] == turn and board[i][j+3] == turn):
				return True

	# check vertical
	for i in range(BOARDHEIGHT-3):
		for j in range(BOARDWIDTH):
			if (board[i][j] == turn and board[i+1][j] == turn and board[i+2][j] == turn and board[i+3][j] == turn):
				return True

	# check left diagonal
	for i in range(3, BOARDHEIGHT):
		for j in range(3, BOARDWIDTH):
			if (board[i][j] == turn and board[i-1][j-1] == turn and board[i-2][j-2] == turn and board[i-3][j-3] == turn):
				return True

	# check right diagonal
	for i in range(3, BOARDHEIGHT):
		for j in range(BOARDWIDTH-3):
			if (board[i][j] == turn and board[i-1][j+1] == turn and board[i-2][j+2] == turn and board[i-3][j+3] == turn):
				return True

	return False

def fullBoard(board):
	for i in range(BOARDHEIGHT):
		for j in range(BOARDWIDTH):
			if board[i][j] == " ":
				return False
	return True


def removeCol(board, col):
	for i in range(BOARDHEIGHT):
		if board[i][col] != " ":
			board[i][col] = " "
			break

def getComputerMove(board, turn):
	moves = AIMove(board, turn, 2)

	print("Computer Moves", moves)

	bestMoveScore = max([moves[i] for i in range(BOARDWIDTH) if isValid(board, i)])
	bestMoves = []
	for i in range(len(moves)):
		if moves[i] == bestMoveScore:
			bestMoves.append(i)
	return random.choice(bestMoves)


def AIMove(board, turn, lookahead):
	# print("lookahead!!!", lookahead)
	# displayBoard(board)


	moves = [0] * BOARDWIDTH

	if lookahead == 0:
		return moves

	if turn == 'X':
		player = 'O'
	else:
		player = 'X'

	if fullBoard(board):
		return moves

	for i in range(BOARDWIDTH):
		if isValid(board, i):
			# if your next move can win select that one
			# if I win, mark probability as 1
			placeCol(board, i, turn)
			if win(board, turn):
				removeCol(board, i)
				moves[i] = 1
				break
			else:
				# do player's move and determine best one
				if fullBoard(board):
					moves[i] = 0
				else:
					for j in range(BOARDWIDTH):
						if isValid(board, j):
							placeCol(board, j, player)
							# If I make a move, and opponent can win in next turn mark my move as -1
							if win(board, player):
								removeCol(board, j)
								moves[i] = -1
								break
							else:
								results = AIMove(board, turn, lookahead-1)
								moves[i] += (sum(results) / BOARDWIDTH) / BOARDWIDTH
							removeCol(board, j)

			removeCol(board, i)

	return moves
	


def rotateBoard(board):
	print()
	print("rotate")
	print()

	newboard = board[::-1]
	a = list(zip(*newboard))

	pprint(a)

	# displayBoard(a)




def main():
	print("Welcome to a game of four in a row!")

	while True:
		board = getBoard()

		player, opponent = choosePiece()
		turn = whoGoesFirst(player, opponent)


		while True:
			displayBoard(board)
			rotateBoard(board)

			if turn == player:
				print("player's turn")
				col = chooseCol(board)
				placeCol(board, col, turn)

				if win(board, turn):
					displayBoard(board)
					print("Congrats! player won!")
					break

				turn = opponent
			else:
				print("opponent's turn")
				col = getComputerMove(board, turn)
				# col = chooseCol(board)
				placeCol(board, col, turn)

				if win(board, turn):
					displayBoard(board)
					print("sorry. you lose. computer wins")
					break

				turn = player

			if fullBoard(board):
				print("game tied")
				break

		if not playAgain():
			break


if __name__ == "__main__":
	main()

