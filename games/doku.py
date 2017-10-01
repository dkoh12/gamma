# http://norvig.com/sudoku.html

import random


def cross(A, B):
	return [a+b for a in A for b in B]

digits = '123456789'
col = digits
row = 'abcdefghi'.upper()
squares = cross(row, col)
unit_row = [cross(row, c) for c in col]
unit_col = [cross(r, col) for r in row]
unit_square = [cross(b, a) for a in ["123", "456", "789"] for b in ["ABC", "DEF", "GHI"]]
unitlist = unit_row + unit_col + unit_square

units = dict((s, [u for u in unitlist if s in u]) for s in squares)

# don't quite understand this part
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)

def test():
	
	assert len(squares) == 81
	assert len(unitlist) == 27
	assert all(len(units[s]) == 3 for s in squares)
	assert all(len(peers[s]) == 20 for s in squares)

	assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'], 
	['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'], 
	['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]

	assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 
		'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
		 'A1', 'A3', 'B1', 'B3'])
	print('All tests pass.')


# possible values for each square
def parse_grid(grid):
	values = dict((s, digits) for s in squares)
	for s, d in grid_values(grid).items():
		# print("s, d", s, d)
		if d in digits and not assign(values, s, d):
			return False
	return values

# map grid value to each square
def grid_values(grid):
	chars = [c for c in grid if c in digits or c in '0.']
	assert len(chars) == 81

	return dict(zip(squares, chars))

# constraint propagation
# (1) If a square has only one possible value, then eliminate that value from the square's peers. 
# (2) If a unit has only one possible place for a value, then put the value there.
def assign(values, s, d):
	other_values = values[s].replace(d, '')
	# print("other values", other_values)

	if all(eliminate(values, s, d2) for d2 in other_values):
		return values
	else:
		return False

def eliminate(values, s, d):
	if d not in values[s]:
		return values #return values

	values[s] = values[s].replace(d, '')

	# if square s is reduced to 1 value d2, eliminate d2 from others
	if len(values[s]) == 0:
		return False # contradiction: removed last value
	elif len(values[s]) == 1:
		d2 = values[s]
		if not all(eliminate(values, s2, d2) for s2 in peers[s]):
			return False


	# if unit is reduced to only one place for value d, then put it there
	for u in units[s]:
		dplaces = [s for s in u if d in values[s]]
		if len(dplaces) == 0:
			return False # contradiction. no place for value d
		elif len(dplaces) == 1:
			if not assign(values, dplaces[0], d):
				return False

	return values

# display result of parsed grid values into a grid format
def display(values):
	width = 1 + max(len(values[s]) for s in squares)
	line = '+'.join(['-'*(width*3)]*3)
	for r in row:
		print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in col))
		if r in 'CF':
			print(line)
	print()

# search. this part allows us to solve any sudoku puzzle
def solve(grid):
	return search(parse_grid(grid))

def search(values):
	if values is False:
		return False # failed earlier
	if all(len(values[s]) == 1 for s in squares):
		return values # solved!

	# choose unfilled square s w/ minimum remaining values
	n, s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
	return some(search(assign(values.copy(), s, d)) for d in values[s])


def some(seq):
	for e in seq:
		if e: # returns first element of seq that is true
			return e
	return False


######################
#
# extra stuff to write random tests
#
######################
import time, random

def solve_all(grids, name='', showif=0.0):
    """Attempt to solve a sequence of grids. Report results.
    When showif is a number of seconds, display puzzles that take longer.
    When showif is None, don't display any puzzles."""
    def time_solve(grid):
        start = time.clock()
        values = solve(grid)
        t = time.clock()-start
        ## Display puzzles that take long enough
        if showif is not None and t > showif:
            display(grid_values(grid))
            if values: display(values)
            print '(%.2f seconds)\n' % t
        return (t, solved(values))
    times, results = zip(*[time_solve(grid) for grid in grids])
    N = len(grids)
    if N > 1:
        print "Solved %d of %d %s puzzles (avg %.2f secs (%d Hz), max %.2f secs)." % (
            sum(results), N, name, sum(times)/N, N/sum(times), max(times))

def solved(values):
    "A puzzle is solved if each unit is a permutation of the digits 1 to 9."
    def unitsolved(unit): return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unitsolved(unit) for unit in unitlist)

def from_file(filename, sep='\n'):
    "Parse a file into a list of strings, separated by sep."
    return file(filename).read().strip().split(sep)

def random_puzzle(N=17):
    """Make a random puzzle with N or more assignments. Restart on contradictions.
    Note the resulting puzzle is not guaranteed to be solvable, but empirically
    about 99.8% of them are solvable. Some have multiple solutions."""
    values = dict((s, digits) for s in squares)
    for s in shuffled(squares):
        if not assign(values, s, random.choice(values[s])):
            break
        ds = [values[s] for s in squares if len(values[s]) == 1]
        if len(ds) >= N and len(set(ds)) >= 8:
            return ''.join(values[s] if len(values[s])==1 else '.' for s in squares)
    return random_puzzle(N) ## Give up and make a new puzzle

def shuffled(seq):
    "Return a randomly shuffled copy of the input sequence."
    seq = list(seq)
    random.shuffle(seq)
    return seq


def main():
	test()

	grid = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"

	# g = grid_values(grid)
	# print(g)

	display(parse_grid(grid))
	





if __name__=="__main__":
	main()
