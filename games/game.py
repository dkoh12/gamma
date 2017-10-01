'''

This file is only for testing purposes and practicing for TripleByte interviews.
Once you have completed, delete the contents of the file.

'''

from pprint import pprint
import random
import re
import time
import sys


GRIDSIZE = 3
MINES = 10

def getBoard():
	return [[" "] * GRIDSIZE for i in range(GRIDSIZE)]

def displayBoard(board):
	print("   ", end='')
	for i in "012": #"abcdefghi":
		print(" " + i + "  ", end='')
	print()
	print("   ", end='')
	print("----" * GRIDSIZE)

	for i in range(len(board)):
		print(str(i) + " |", end='')
		for j in range(len(board[i])):
			print(" " + str(board[i][j]) + " |", end='')
		print()
		print("   ", end='')
		print("----" * GRIDSIZE)

def playAgain():
	ans = input("Do you want to play again? (yes or no): ")
	return ans.lower()[0] == 'y'



def main():
	print("play tic tac toe!!")

	while True:

		board = getBoard()
		player, computer = choosePiece()

		turn = whoGoesFirst(player, computer)

		while True:


			break

		displayBoard(board)

		if not playAgain():
			break


if __name__ == "__main__":
	main()

