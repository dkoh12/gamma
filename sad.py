
def isPattern(pattern, string, d):
	if len(pattern) == 1:
		# if we find a new pattern, or an old pattern matches what we already have in our dic
		if pattern not in d or d[pattern[0]] == string:
			print("####")

			return len(d.values()) == len(set(d.values()))

		return False


	nextPatternLen = len(string) - len(pattern) + 1

	for i in range(1, nextPatternLen+1):
		matchPattern = string[:i]

		# optimization.
		# if the pattern is already in our dict but it doesn't match skip it
		if pattern[0] in d and d[pattern[0]] != matchPattern:
			continue

		d[pattern[0]] = matchPattern

		print(d)
		ret = isPattern(pattern[1:], string[i:], d)

		if ret:
			return True
		if pattern[0] in d:
			del d[pattern[0]]

	return False


from pprint import pprint



def check(board, row, col):

	#check left row
	for i in range(col):
		if(board[row][i]):
			return False

	#check left upper diagonal
	i = 1
	while(row-i >= 0 and col-i >= 0):
		if board[row-i][col-i]:
			return False
		i+=1

	#check left lower diagonal
	i=1
	j=1
	while(row+i < len(board) and col-j >= 0):
		if board[row+i][col-j]:
			return False
		i+=1
		j+=1

	return True


def solution(board, n, col):
	if col >= n:
		return True

	for row in range(n): #row
		if(check(board, row, col)):
			board[row][col] = 1

			if(solution(board, n, col+1)):
				return True

			board[row][col] = 0

	return False


def nqueens(n):
	board = [[0] * n for i in range(n)]

	if(not solution(board, n, 0)):
		print("there is no solution")

	pprint(board)


from itertools import permutations

def boxHeight(arr):
	newarr = []
	for i in arr:
		newarr.extend(permutations(i))

	newarr.sort()

	count = [i[0] for i in newarr]

	for i in range(1, len(newarr)):
		for j in range(i):
			# next box must be smaller than current box
			# however we sorted it backwards such that elements to the right are greater
			# than elements on left
			if (newarr[i][2] >= newarr[j][2] and
				newarr[i][1] >= newarr[j][1] and
				count[i] < count[j] + newarr[i][0]):

				count[i] = count[j] + newarr[i][0]

	print(max(count))



'''
basic idea is this
http://www.geeksforgeeks.org/?p=27614

if curr elem is smallest among all ends, start a new list with len of 1
if curr elem is largest among all ends, clone largest active list and extend it by curr
if curr elem is in between, find list with largest end element smaller than curr
clone and extend this list by curr. discard all other lists of same length

'''

def binarysearch(arr, tail, i):
	low = 0
	high = len(tail) -1

	while high > low:
		mid = (high-low)//2 + low

		# print("mid", mid)
		# print(arr[tail[mid]], arr[i])

		if arr[tail[mid]] > arr[i]:
			high = mid
		else:
			low = mid+1

	# print("low", low, "high", high)

	return high

# O(n log n)
def lispath(arr):

	tail = []

	parent = [None] * len(arr)

	for i in range(len(arr)):
		if not tail or arr[i] > arr[tail[-1]]:
			if len(tail) > 0:
				parent[i] = tail[-1]

			tail.append(i)

		else:
			# print("i", i, "arr[i]", arr[i])

			replace_index = binarysearch(arr, tail, i)

			tail[replace_index] = i

			if replace_index != 0:
				parent[i] = tail[replace_index-1]

			# print("replace_index", replace_index)

	# 	print("arr", arr)
	# 	print("tail", tail)


	# print("###")
	# print("arr", arr)
	# print("tail", tail)
	# print("parent", parent)

	curr = tail[-1]
	path = []

	while curr is not None:
		path.append(arr[curr])
		curr = parent[curr]

	path.reverse()

	return path


# http://www.geeksforgeeks.org/dynamic-programming-set-37-boolean-parenthesization-problem/
def boolean_paren(symbol, operator):
	n = len(symbol)
	F = [[0]*n for i in range(n)]
	T = [[0]*n for i in range(n)]


	for i in range(n):
		if symbol[i] == 'T':
			F[i][i] = 0
			T[i][i] = 1
		else:
			F[i][i] = 1
			T[i][i] = 0

	for g in range(1, n):

		i=0
		j=g

		print("G", g)

		while(j < n):

			print("T")
			pprint( T)
			print("F")
			pprint( F)


			T[i][j] = 0
			F[i][j] = 0

			for k in range(g):
				s = i + k

				total_is = T[i][s] + F[i][s]
				total_sj = T[s+1][j] + F[s+1][j]

				if operator[s] == '&':
					T[i][j] += T[i][s] * T[s+1][j]
					F[i][j] += total_sj * total_is - T[i][s] * T[s+1][j]

				if operator[s] == '|':
					F[i][j] += F[i][s] * F[s+1][j]
					T[i][j] += total_is * total_sj - F[i][s] * F[s+1][j]

				if operator[s] == '^':
					T[i][j] += F[i][s] * T[s+1][j] + T[i][s] * F[s+1][j]
					F[i][j] += T[i][s] * T[s+1][j] + F[i][s] * F[s+1][j]


			i+=1
			j+=1


	print("T")
	pprint(T)
	print("F")
	pprint(F)

	return T[0][n-1]

if __name__=="__main__":
	pattern = "abba"
	string = "redbluebluered"

	# print(isPattern(pattern, string, {}))

	arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
	print(lispath(arr))

	# [0, 2, 6, 9, 11, 15] << correct answer


	# nqueens(8)

	symbol = "TTFT"
	operator = "|&^"
	print(boolean_paren(symbol, operator))


	box = [[3, 1, 2], [4, 8, 7], [22, 5, 8], [9, 3, 6]]
	# box = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
	# boxHeight(box)




