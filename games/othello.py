


def greeting():
	print("Welcome to Othello!")
	n = input("Do you want to be white or black? ")
	if n.lower().startswith("w"):
		return ["white", "black"]
	else:
		return ["black", "white"]

# black always goes first
def getTurn():
	return "black"

def getBoard():
	board = [[" " for i in range(8)] for j in range(8)]
	board[4][4] = "O"
	board[3][4] = "X"
	board[4][3] = "X"
	board[3][3] = "O"

	return board

def displayBoard(board):
	print("     ", end="")
	for i in range(8):
		print(str(i+1) + "   ", end="")
	print()
	print("   +---+" + "---+"*7)

	for i in range(len(board)):
		print(" " + str(i+1) + " ", end="|")
		for j in range(len(board[i])):
			print(" " + board[i][j] + " ", end="|")
		print()
		print("   +---+" + "---+"*7)

def getPiece(turn):
	if turn == "black":
		return "X"
	else:
		return "O"

def chooseMove(board, piece):
	while True:
		n = input("Please input valid coordinate in the format 'x y' ")
		try:
			x, y = list(map(int, n.split()))
		except:
			print("invalid input")
			continue

		if isValidMove(board, (x, y), piece):
			return (x-1, y-1)
		

def isValidMove(board, n, piece):
	x, y = n

	if not (1 <= x <= 8 and 1 <= y <= 8):
		print("please make x and y to be within 1 and 8")
		return False
	if board[y-1][x-1] != " ":
		print("that spot is already filled with %s" % board[y-1][x-1])
		return False

	if getNeighbor(board, x-1, y-1, piece):
		return True

	return False

def oppositePiece(piece):
	if piece == "X":
		return "O"
	else:
		return "X"

def getNeighbor(board, x, y, piece):
	neighbors = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			if i == 0 and j == 0:
				continue
			if -1 < i+x < 8 and -1 < j+y < 8:
				tx = x+i
				ty = y+j
				if board[ty][tx] != oppositePiece(piece):
					continue
				outOfBounds = False
				while board[ty][tx] == oppositePiece(piece):
					ty += j
					tx += i
					if not (-1 < tx < 8 and -1 < ty < 8):
						outOfBounds = True
						break
				
				if outOfBounds:
					pass
				elif board[ty][tx] == piece:
					neighbors.append((x, y, i, j))
					

	if len(neighbors) != 0:
		return neighbors
	else:
		print("please enter a coordinate next to your opponents piece")
		return False


# can turn empty squares that is inbetween as the user's piece
def makeMove(board, move, piece):
	x, y = move
	board[y][x] = piece

	neighbors = getNeighbor(board, x, y, piece)

	for k in neighbors:
		x, y, i, j = k
		ty = y + j
		tx = x + i
		while board[ty][tx] != piece:
			board[ty][tx] = piece
			ty += j
			tx += i


def calculateScore(board):
	white = 0
	black = 0

	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == "O":
				white += 1
			if board[i][j] == "X":
				black += 1

	return (white, black)


def isBoardFull(board):
	for y in range(len(board)):
		for x in range(len(board[y])):
			if board[y][x] == " ":
				return False
	return True

def winner(white, black):
	if white > black:
		print("The winner is white")
	elif white < black:
		print("The winner is black")
	else:
		print("It is a tie")

def playAgain():
	return input("Do you want to play again? ").lower().startswith('y')

if __name__=="__main__":

	while True:
		user, computer = greeting()
		turn = getTurn()
		board = getBoard()

		
		while True:
			piece = getPiece(turn)

			# X moves
			if turn == "black":
				print("It is black's turn")
				displayBoard(board)
				move = chooseMove(board, piece)
				makeMove(board, move, piece)


				if isBoardFull(board):
					break

				turn = "white"
			else:
				print("It is white's turn")
				displayBoard(board)
				move = chooseMove(board, piece)
				makeMove(board, move, piece)

				if isBoardFull(board):
					break

				turn = "black"


			white, black = calculateScore(board)
			print("current score is")
			print("white %d" % white)
			print("black %d" % black)

		displayBoard(board)
		white, black = calculateScore(board)
		print("current score is")
		print("white %d" % white)
		print("black %d" % black)
		
		winner(white, black)

		if not playAgain():
			break







