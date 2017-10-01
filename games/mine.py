
"""A command line version of Minesweeper"""
import random
import re
import time
from string import ascii_lowercase

GRIDSIZE = 9
MINES = 10

helpmessage = ("Type the column followed by the row (eg. a5). "
                "To put or remove a flag, add 'f' to the cell (eg. a5f).")

def main():

    while True:
        board = [[' '] * GRIDSIZE for i in range(GRIDSIZE)]

        grid = [] #answer key
        flags = []
        starttime = 0

        showgrid(board)
        print(helpmessage + " Type 'help' to show this message again.\n")

        while True:

            result = getMove(flags)

            row, col, flag = result
            currcell = board[row][col]

            if not grid:
                grid, mines = setupgrid(row, col)
            if not starttime:
                starttime = time.time()

            if flag:
                # Add a flag if the cell is empty
                if currcell == ' ':
                    board[row][col] = 'F'
                    flags.append((row, col))
                # Remove the flag if there is one
                elif currcell == 'F':
                    board[row][col] = ' '
                    flags.remove((row, col))
                else:
                    print('Cannot put a flag there')

            # If there is a flag there, show a message
            elif (row, col) in flags:
                print('There is a flag there')
            elif grid[row][col] == 'X':
                print('Game Over\n')
                break
            elif currcell == ' ': #shows cell to current board
                showcells(grid, board, row, col)
            else:
                print("That cell is already shown")

            if set(flags) == set(mines):
                minutes, seconds = divmod(int(time.time() - starttime), 60)
                print('You Win. '
                    'It took you {} minutes and {} seconds.\n'.format(minutes, seconds))
                break
                    
            showgrid(board)

        showgrid(grid)
        if not playagain():
            break

# sets up answer key board
# places mines on the board
def setupgrid(row, col):
    emptygrid = [['0'] * GRIDSIZE for i in range(GRIDSIZE)]

    mines = getmines(emptygrid, row, col)

    for i, j in mines:
        emptygrid[i][j] = 'X'

    grid = getnumbers(emptygrid)

    showgrid(grid)
    print("mines", mines)

    return (grid, mines)

#display current board game
def showgrid(grid):
    horizontal = '   ' + '+---+' + '---+' * (GRIDSIZE-1)

    # Print top column letters
    toplabel = ' ' * 5

    for i in ascii_lowercase[:GRIDSIZE]:
        toplabel += i + '   '

    print(toplabel)
    print(horizontal)

    # Print left row numbers
    for idx, i in enumerate(grid):
        row = '{0:2} |'.format(idx + 1)

        for j in i:
            row += ' ' + j + ' |'

        print(row)
        print(horizontal)
    print()

def getrandomcell():
    a = random.randint(0, GRIDSIZE - 1)
    b = random.randint(0, GRIDSIZE - 1)
    return (a, b)

# get the 8 neighboring cells
# this is used in getMines() to not place a mine in the first cell the user selected
# and getnumbers() to get number of mines near it.
def getneighbors(grid, row, col):
    neighbors = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            else:
                if -1 < row + x < GRIDSIZE and -1 < col + y < GRIDSIZE:
                    neighbors.append((row + x, col + y))

    return neighbors

# places mines
def getmines(grid, row, col):
    mines = []
    neighbors = getneighbors(grid, row, col)

    for i in range(MINES):
        cell = getrandomcell()
        # The very first cell the player selects CANNOT be a mine!
        while cell == (row, col) or cell in neighbors or cell in mines:
            cell = getrandomcell()
        mines.append(cell)

    return mines

# places numbers on answer key board
def getnumbers(grid):
    for rowno, row in enumerate(grid):
        for colno, cell in enumerate(row):
            if cell != 'X':
                # Gets the values of the neighbors
                values = [grid[r][c] for r, c in getneighbors(grid, rowno, colno)]

                # Counts how many are mines and sets a number
                grid[rowno][colno] = str(values.count('X'))

    return grid

# reveals cells from answer key board to the current board
def showcells(grid, board, row, col):
    # Exit function if the cell was already shown
    if board[row][col] != ' ':
        return

    # Show current cell
    board[row][col] = grid[row][col]

    # Get the neighbors if the cell is empty
    if grid[row][col] == '0':
        for r, c in getneighbors(grid, row, col):
            # Repeat function for each neighbor that doesn't have a flag
            if board[r][c] != 'F':
                showcells(grid, board, r, c)


def playagain():
    return input('Play again? (yes or no): ').lower().startswith('y')


def getMove(flags):
    minesleft = MINES - len(flags)

    while True:
        prompt = input("Enter the cell (%d mines left): " % minesleft)

        pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[GRIDSIZE-1])
        validinput = re.match(pattern, prompt)

        if prompt == "help":
            print(helpmessage)
        elif validinput:
            row = int(validinput.group(2)) - 1
            col = ascii_lowercase.index(validinput.group(1))
            flag = bool(validinput.group(3))

            if 0 <= row < GRIDSIZE:
                return (row, col, flag)
        else:
            print("Invalid Cell")

if __name__=="__main__":
    main()
