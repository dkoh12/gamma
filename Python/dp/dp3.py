from pprint import pprint
from itertools import permutations

'''
/*=====================================
=            Pattern Match            =
=====================================*/
'''
def isPattern(pattern, string, d):
	if len(pattern) == 1:
		# if we find a new pattern, or an old pattern matches what we already have in our dic
		if pattern not in d or d[pattern[0]] == string:
			# print("####")

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

		# print(d)
		ret = isPattern(pattern[1:], string[i:], d)

		if ret:
			return True
		if pattern[0] in d:
			del d[pattern[0]]

	return False

def patternmatch():
	pattern = "abba"
	string = "redbluebluered"
	print("pattern match")
	print(isPattern(pattern, string, {}))


# /*=====  End of Pattern Match  ======*/


'''
/*======================================
=            Stacking Boxes            =
======================================*/
'''
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

	return max(count)

def executeBoxHeight():
	box = [[3, 1, 2], [4, 8, 7], [22, 5, 8], [9, 3, 6]]
	# box = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
	print("box height")
	print(boxHeight(box))


#/*=====  End of Stacking Boxes  ======*/



'''
/*===========================================
=            boolean parenthesis            =
===========================================*/
'''

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

		# print("G", g)

		while(j < n):

			# print("T")
			# pprint( T)
			# print("F")
			# pprint( F)


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


	# print("T")
	# pprint(T)
	# print("F")
	# pprint(F)

	return T[0][n-1]


def executeBooleanParen():
	symbol = "TTFT"
	operator = "|&^"
	print("Boolean Parenthesis")
	print(boolean_paren(symbol, operator))


#/*=====  End of boolean parenthesis  ======*/

'''
/*===================================
=            Optimal BST            =
===================================*/
http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/



'''

def getSum(freq, i, j):
	s = 0
	for k in range(i, j+1):
		s += freq[k]
	return s

def optimalBST(keys, freq):
	n = len(keys)

	M = [[float('inf')] * n for i in range(n)]

	for i in range(n):
		M[i][i] = freq[i]

	# chain length
	for L in range(2, n+1):
		# i = row
		for i in range(0, n-L+1):
			# j = col
			for j in range(i+L-1, n):
				for r in range(i, j+1):
					temp = getSum(freq, i, j)

					if (r > i):
						temp += M[i][r-1]

					# we must have this condition because we don't want r < 0;
					# and get index out of bounds
					if (r < j):
						temp += M[r+1][j]

					if temp < M[i][j]:
						M[i][j] = temp

	pprint(M)

	return M[0][n-1]



def executeOptimalBST():
	# make sure keys are sorted. and that corresponding freq are too
	keys = [10,12,20, 22]
	freq = [34, 8, 50, 27]

	print("optimal BST")
	print(optimalBST(keys, freq))

# /*=====  End of Optimal BST  ======*/

'''
/*=============================================
=            Matrix Multiplication            =
=============================================*/

find minimum number of multiplications
http://www.geeksforgeeks.org/?p=15553

time: O(n^3)
space: O(n^2)


>> [1,2,3,4]
3 matrices: 1x2, 2x3, 3x4

M[1][2] = M[1][1] + M[2][2] + 1*2*3   => multiply matrix 1x2 and 2x3
M[2][3] = M[2][2] + M[3][3] + 2*3*$   => multiply matrix 2x3 and 3x4


multiply matrix 2x3 and 3x4 => 2x4. Then multiply this 1x2 and 2x4
A = M[1][1] + M[2][3] + 1*2*4. 

multiply matrix 1x2 and 2x3 => 1x3. Then multiply this 1x3 and 3x4
B = M[1][2] + M[3][3] + 1*3*4. 

M[1][3] = min(A, B)

  0 1 2 3
0 0 -------
1   0 6 18
2     0 24
3       0


In order to get M[1][3]



'''
def matrixMultiply(arr):
	n = len(arr)
	M = [[float('inf')] * n for i in range(n)]

	for i in range(n):
		M[i][i] = 0

	# L = chain length
	for L in range(2, n):
		# i = row
		for i in range(1, n-L+1):
			# j = col
			j = i + L - 1

			for k in range(i, j):

				# see above
				q = M[i][k] + M[k+1][j] + arr[i-1]*arr[k]*arr[j]

				if q < M[i][j]:
					M[i][j] = q

	return M[1][n-1]



def executeMatrixMultiply():
	arr = [1,2,3,4]
	print("Matrix Multiply")
	print(matrixMultiply(arr))



# /*=====  End of Matrix Multiplication  ======*/


'''
go from top left to bottom right of graph and count number of paths.

time: O(mn)
'''
def numberOfPaths(m, n):
    count = [[0 for x in range(m)] for y in range(n)]
   
    for i in range(m):
        count[i][0] = 1;
   
    for j in range(n):
        count[0][j] = 1;

    for i in range(1, m):
        for j in range(1, n):
        	count[i][j] = count[i-1][j] + count[i][j-1]

    pprint(count)

    return count[m-1][n-1]


# print(numberOfPaths(3, 3))

'''
/*======================================================
=            Maximum Subsquare with Sides X            =
======================================================*/

https://www.youtube.com/watch?v=vi_1eHCsR9A&index=41&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

grid contains tuple of (x,y) where x = horizontal and y = vertical
number of X's seen


'''

def maximumSubsquare(square):
	n = len(square)
	grid = [[(0,0)]*n for i in range(n)]

	for i in range(n):
		for j in range(n):
			if square[i][j] == 'O':
				grid[i][j] = (0,0)

			else:
				grid[i][j] = (1 + grid[i][j-1][0], 1 + grid[i-1][j][1])

	# pprint(grid)

	count = 0
	for i in range(n-1, -1, -1):
		for j in range(n-1, -1, -1):
			x, y = grid[i][j]
			m = min(x, y)

			if m <= count:
				continue

			for k in range(m, count, -1):

				horiz = grid[i-k+1][j][0]
				vert = grid[i][j-k+1][1]

				if horiz >= count and vert >= count:
					count = m

	return count


def executeMaximumSubsquare():
	square = [['O', 'O', 'O', 'O', 'X'],
			  ['X', 'O', 'X', 'X', 'X'],
			  ['X', 'O', 'X', 'O', 'X'],
			  ['X', 'X', 'X', 'X', 'X'],
			  ['O', 'O', 'X', 'X', 'X']]


	print(maximumSubsquare(square))

#/*=====  End of Maximum Subsquare with Sides X  ======*/

'''
/*==========================================
=            Sum Query 2D array            =
==========================================*/

https://leetcode.com/problems/range-sum-query-2d-immutable/#/description

Give the sum of elements in a subsquare in constant time.

'''

def getNewBoard(board, r, c):
	row = r+1
	col = c+1

	newboard = [[0]*(row) for i in range(col)]

	# initialize first row
	for i in range(1, col):
		newboard[1][i] = board[0][i-1] + newboard[1][i-1]

	#initialize first col
	for i in range(2, row):
		newboard[i][1] = board[i-1][0] + newboard[i-1][1]

	for i in range(2, row):
		for j in range(2, col):
			newboard[i][j] = newboard[i-1][j] + newboard[i][j-1] + board[i-1][j-1] - newboard[i-1][j-1]

	return newboard

def sumQuery(board, start, end):
	r1, c1 = start
	r2, c2 = end

	r1+=1
	c1+=1
	r2+=1
	c2+=1

	return board[r2][c2] - board[r2][c1-1] - board[r1-1][c2] + board[r1-1][c1-1]


def executeSumQuery():
	board = [[2, 0, -3, 4],
			 [6, 3, 2, -1],
			 [5, 4, 7, 3],
			 [2, -6, 8, 1]]
	row = 4
	col = 4

	newboard = getNewBoard(board, row, col)

	start = [1,1]
	end = [3,2]

	print(sumQuery(newboard, start, end))


#/*=====  End of Sum Query 2D array  ======*/
'''
/*===========================================================================
=            Count Number of Binary Trees from Preorder Sequence            =
===========================================================================*/
https://www.youtube.com/watch?v=RUB5ZPfKcnY&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=42


This is also the solution for 
Count Number of Binary Search Trees given n keys 

'''

def numBinaryTree(length):
	if length == 0:
		return 0

	arr = [1, 1]

	for i in range(2, length+1):
		total =0
		for j in range(0, i):
			total += arr[j] * arr[i-j-1]
		arr.append(total)

	print(arr)
	return arr[length]

def executeNumBT():
	length = 5
	print(numBinaryTree(length))

#/*=====  End of Count Number of Binary Trees from Preorder Sequence  ======*/
'''
/*==================================
=            Subset Sum            =
==================================*/
return whether or not a sum can be made from a subset of elements
'''

def subsetSum(lst, total):
	arr = [[False] * (total+1) for i in range(len(lst))]

	for i in range(len(lst)):
		arr[i][0] = True

	arr[0][lst[0]] = True


	for i in range(1, len(lst)):
		for j in range(1, total+1):
			if lst[i] > j:
				arr[i][j] = arr[i-1][j]
			else:
				arr[i][j] = arr[i-1][j-lst[i]] or arr[i-1][j]


	print(arr)

	# for i in arr:
	# 	print(i)
	
	# this will print true or false
	# the following will print what elements are in the set

	i = len(lst)-1
	j = total
	myset = []


	while i >0 and j>0:
		if arr[i][j]:
			if not arr[i-1][j]:
				n = lst[i]
				myset.append(n)
				j-=n
			i-=1
		else:
			break

	if j!=0 and arr[i][j]:
		myset.append(lst[0])

	return set(myset)

def executeSubsetSum():
	arr = [2, 3, 7, 8, 10]
	total = 16
	print(subsetSum(arr, total))

#/*=====  End of Subset Sum  ======*/

'''
/*========================================================
=            Maximum Size Rectangle of All 1s            =
========================================================*/
https://www.careercup.com/question?id=6299074475065344

getArea() returns the max area given an array.
It turns the array into a histogram with the element as the height and index as the width

'''

def getArea(arr):
	area = 0
	width = 0
	height = float('inf')

	for i in range(len(arr)):
		if arr[i] != 0:
			area = max(area, arr[i])
			height = min(arr[i], height)
			width += 1
		else:
			area = max(area, height*width)
			width = 0
			height = float('inf')

		area = max(area, height * width)

	return area

def getSize(rectangle):
	arr = rectangle[0][:]

	for i in range(1, len(rectangle)):
		for j in range(len(rectangle[0])):
			if rectangle[i][j] == 0:
				arr[j] = 0
			else:
				arr[j] += 1

	print(arr)

	return getArea(arr)

def executeMaximumSize():
	rectangle = [[1, 0, 0, 1, 1, 1],
				[1, 0, 1, 1, 0, 1],
				[0, 1, 1, 1, 1, 1],
				[0, 0, 1, 1, 1, 1]]

	print(getSize(rectangle))


#/*=====  End of Maximum Size Rectangle of All 1s  ======*/

'''
/*=========================================================
=            Maximum Sum Rectangular Submatrix            =
=========================================================*/
https://www.youtube.com/watch?v=yCQN096CwWM&index=15&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

'''
import numpy as np

def maximumSumRectangle(rectangle):

	arr = np.array(rectangle)
	A = arr[:,1:3]

	L = 0
	R = 0
	curr = 0
	mmax = 0
	mLeft = 0
	mRight = 0
	mUp = 0
	mDown = 0


	# for L in range(len(arr[0])):
	# 	for R in range(L+1, len(arr[0])+1):
			
	# 		temp = arr[:, L:R]
	# 		print(sum(temp))

	# 		print(L, R)
	# 		print(temp)
	# 		pass


	print(arr)

	return 0

def executeMaximumSumRectangle():
	rectangle = [[2, 1, -3, -4, 5],
				[0, 6, 3, 4, 1],
				[2, -2, -1, 4, -5],
				[-3, 3, 1, 0, 3]]

	print(maximumSumRectangle(rectangle))

#/*=====  End of Maximum Sum Rectangular Submatrix  ======*/


'''
/*==========================================
=            Text Justification            =
==========================================*/
http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/
https://www.youtube.com/watch?v=RORuwHiblPc&index=18&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

Given each line can hold width characters, balance the text so that you get the smallest empty space

* space that separates words is not considered an empty space

Tushar Roy -> 0
likes to   -> 2
code       -> 6
2^2 + 6^2 = 4 + 36 = 40

Tushar     -> 4
Roy likes  -> 1
to code    -> 3
4^2 + 1^2 + 3^2 = 16+1+9 = 26


time is O(n^2)
space is O(n^2)

'''

def textJustify(lst, width):
	n = len(lst)
	arr = [[0]*n for i in range(n)]

	count = [len(i) for i in lst]

	for i in range(n):
		arr[i][i] = (width - count[i]) ** 2

	for i in range(n):
		for j in range(i+1, n):
			total = 0

			for k in range(i, j+1):
				if total != 0:
					total += 1
				total += count[k]

			if total > width:
				arr[i][j] = float('inf')
			else:
				arr[i][j] = (width-total) ** 2

	cost = [0] * n
	res = [0] * n

	pprint(arr)
	print()
	
	for i in range(n-1,-1,-1):
		cost[i] = arr[i][n-1]
		res[i] = n

		for j in range(n-1, i, -1):

			if arr[i][j-1] == float('inf'):
				continue

			if cost[i] > cost[j] + arr[i][j-1]:
				cost[i] = cost[j] + arr[i][j-1]
				res[i] = j

	
	# print(cost)
	# print(res)

	# printSolution(res, n-1)

	out = []
	curr = res[0]
	temp = []
	for i in range(n):
		if curr != res[i]:
			out.append(temp)
			temp = []
		temp.append(lst[i])
		curr = res[i]

	out.append(temp)

	print(out)

	return res, cost[0]

# def printSolution(res, n):
# 	if res[n] == 1:
# 		k = 1
# 	else:
# 		k = printSolution(res, res[n]-1) + 1
# 	print("Line number %d: From word no. %d to %d ", k, res[n], n)
# 	return k


def executeTextJustify():
	arr = ["Tushar", "Roy", "likes", "to", "code"]
	print(textJustify(arr, 10))
	# textJustify(arr, 10)

# /*=====  End of Text Justification  ======*/


'''
/*==========================================
=            Word Break Problem            =
==========================================*/
https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/BreakMultipleWordsWithNoSpaceIntoSpace.java
https://www.youtube.com/watch?v=WepWFGxiwRs&index=19&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr


'''

# /*=====  End of Word Break Problem  ======*/


'''
/*============================================
=            Palindrome Partition            =
============================================*/
https://www.youtube.com/watch?v=lDYIvtBVmgo&index=27&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
http://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/

time -> O(n^2)
'''

# O(n^3) ???
def palindromePartition(s):
	n = len(s)
	arr = [[0] * n for i in range(n)]


	for l in range(2, n+1):
		for i in range(n-l+1):
			j = i+l-1

			if s[i:j+1] == s[i:j+1][::-1]:
				arr[i][j] = 0

			else:
				arr[i][j] = float('inf')
				for k in range(i, j):
					res = 1 + arr[i][k] + arr[k+1][j]
					arr[i][j] = min(arr[i][j], res)

	pprint(arr)
	return arr[0][n-1]


# O(n^2) ???
def palindromePartitionN(s):
	n = len(s)
	arr = [[False]*n for i in range(n)]

	for i in range(n):
		arr[i][i] = True

	for l in range(2, n+1):
		for i in range(n-l+1):
			j = i+l-1

			if l == 2:
				arr[i][j] = (s[i] == s[j])
			else:
				arr[i][j] = (s[i] == s[j]) and arr[i+1][j-1]

	c = [0] * n

	for i in range(n):
		if arr[0][i]:
			c[i] = 0
		else:
			c[i] = float('inf')
			for j in range(i):
				if arr[j+1][i] and 1 + c[j] < c[i]:
					c[i] = c[j] + 1


	pprint(arr)
	print()

	print(c)

	return c[n-1]


def executePalindromePartition():
	s = "abcbm"
	print(palindromePartition(s))
	print(palindromePartitionN(s))


# /*=====  End of Palindrome Partition  ======*/




if __name__=="__main__":
	# patternmatch()
	# executeBoxHeight()
	# executeBooleanParen()
	# executeOptimalBST()
	# executeMatrixMultiply()

	# executeMaximumSubsquare(s)
	# executeSumQuery()
	# executeNumBT()
	# executeSubsetSum()
	# executeMaximumSize()

	# executeMaximumSumRectangle()
	# executeTextJustify()

	executePalindromePartition()
