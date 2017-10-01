
import random #know what this does
import copy
import sys #for sys.exit()

BOARD_HEIGHT = 7
BOARD_WIDTH = 7


def enterHumanTile():
	tile = ''
	while not (tile == 'X' or tile == 'O'):
		print("Do you want to be X or O?")
		tile = input().upper()

	if tile == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']


def whoGoesFirst():
	if random.randint(0, 1) == 0:
		# return "computer"
		return "player 1"
	else:
		# return "human"	
		return "player 2"


def drawBoard(board):
	print()
	print(' ', end='')
	for x in range(1, BOARD_WIDTH + 1):
		print(' %s  ' % x, end='')
	print()

	print('+---+' + ('---+' * (BOARD_WIDTH - 1)))

	for y in range(BOARD_HEIGHT):
		# print('|   |' + ('   |' * (BOARD_WIDTH - 1)))

		print('|', end='')
		for x in range(BOARD_WIDTH):
			print(' %s |' % board[x][y], end='')
		print()

		# print('|   |' + ('   |' * (BOARD_WIDTH - 1)))

		print('+---+' + ('---+' * (BOARD_WIDTH -1)))


def getNewBoard():
	board = []
	for x in range(BOARD_WIDTH):
		board.append([' '] * BOARD_HEIGHT)
	return board

def getHumanMove(board):
	while True:
		print("Which column do you want to move on? (1-%s or 'quit' to quit game)" % BOARD_WIDTH)
		move = input()
		if move.lower().startswith('q'):
			sys.exit()
		if not move.isdigit():
			continue
		move = int(move) - 1
		if isValidMove(board, move):
			return move

# def getComputerMove(board):
# 	potentialMoves = getPotentialMoves(board, computer, 2)
# 	bestMoveScore = max([potentialMoves[i] for i in range(BOARD_WIDTH) if isValidMove(board, i)])
# 	bestMoves = []
# 	for i in range(len(potentialMoves)):
# 		if potentialMoves[i] == bestMoveScore:
# 			bestMoves.append(i)
# 	return random.choice(bestMoves)

# def getPotentialMoves(board, player, lookAhead):
# 	if lookAhead == 0:
# 		return [0] * BOARD_WIDTH

# 	potentialMoves = []

# 	if player == 'X':
# 		enemy = 'O'
# 	else:
# 		enemy = 'X'

# 	if isBoardFull(board):
# 		return [0] * BOARD_WIDTH

# 	potentialMoves = [0] * BOARD_WIDTH
# 	for playerMove in range(BOARD_WIDTH):
# 		dupe = copy.deepcopy(board) #what does this do?
# 		if not isValidMove(dupe, playerMove):
# 			continue
# 		makeMove(dupe, player, playerMove)
# 		if isWinner(dupe, player):
# 			potentialMoves[playerMove] = 1
# 			break
# 		else:
# 			if isBoardFull(dupe):
# 				potentialMoves[playerMove] = 0
# 			else:
# 				for enemyMove in range(BOARD_WIDTH):
# 					dupe2 = copy.deepcopy(dupe)
# 					if not isValidMove(dupe2, enemyMove):
# 						continue
# 					makeMove(dupe2, enemy, enemyMove)
# 					if isWinner(dupe2, enemy):
# 						potentialMoves[playerMove] = -1
# 						break
# 					else:
# 						results = getPotentialMoves(dupe2, player, lookAhead -1)
# 						potentialMoves[playerMove] += (sum(results) / BOARD_WIDTH) / BOARD_WIDTH
# 	return potentialMoves

def makeMove(board, player, column):
	for y in range(BOARD_HEIGHT-1, -1, -1): #range backwards
		if board[column][y] == ' ':
			board[column][y] = player
			return

def isValidMove(board, move):
	if move < 0 or move >= BOARD_WIDTH:
		return False

	if board[move][0] != ' ':
		return False

	return True


def isBoardFull(board):
	for y in range(BOARD_HEIGHT):
		for x in range(BOARD_WIDTH):
			if board[x][y] == ' ':
				return False
	return True


def isWinner(board, tile):
	for y in range(BOARD_HEIGHT):
		for x in range(BOARD_WIDTH - 3):
			if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
				return True

	for x in range(BOARD_WIDTH):
		for y in range(BOARD_HEIGHT - 3):
			if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
				return True

	for x in range(BOARD_WIDTH-3):
		for y in range(3, BOARD_HEIGHT):
			if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
				return True

	for x in range(BOARD_WIDTH - 3):
		for y in range(BOARD_HEIGHT - 3):
			if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
				return True


def playAgain():
	print("Do you want to play again? (yes or no)")
	return input().lower().startswith('y')


if __name__=="__main__":
	print("Connect four")
	print()

	while True:
		human, computer = enterHumanTile()
		turn = whoGoesFirst()
		print("The %s player will go first." % (turn))
		mainboard = getNewBoard()

		while True:
			# if turn == "human":
			if turn == "player 1":
				drawBoard(mainboard)
				move = getHumanMove(mainboard)
				makeMove(mainboard, human, move)
				if isWinner(mainboard, human):
					# winner = "human"
					winner = "player 1"
					break
				# turn = "computer"
				turn = "player 2"
			else:
				drawBoard(mainboard)
				# move = getComputerMove(mainboard)
				move = getHumanMove(mainboard)
				makeMove(mainboard, computer, move)
				if isWinner(mainboard, computer):
					# winner = "computer"
					winner = "player 2"
					break
				# turn = "human"
				turn = "player 1"

			if isBoardFull(mainboard):
				winner = "tie"
				break

		drawBoard(mainboard)
		print("Winner is %s" % winner)
		if not playAgain():
			break




