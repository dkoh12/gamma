'''
/*================================
=            Knapsack            =
================================*/
Top Down

'''

def knapsack(lst, W):
	# @memoized
	def bestValue(i, j):
		if i == 0:
			return 0
		value, weight = lst[i-1]
		if weight > j:
			return bestValue(i-1, j)
		else:
			return max(bestValue(i-1,j), bestValue(i-1, j-weight)+value)

	j = W
	result = []
	for i in range(len(lst), 0, -1):
		if bestValue(i,j) != bestValue(i-1, j):
			result.append(lst[i-1])
			j -= lst[i-1][1]
	result.reverse()
	return bestValue(len(lst), W), result


def executeKnapsack():
	lst = [(4, 12), (2, 1), (6,4), (1,1), (2,2)]
	print("knapsack", knapsack(lst, 15))

#/*=====  End of Knapsack  ======*/


from pprint import pprint
from collections import Counter

# lst of numbers with elements repeated 3 items. find 1 that appears once
def find_elem(lst):
	C = Counter(lst)

	for i in C.items():
		if i[1] == 1:
			return i[0]




# find which element appears once in an array.
# xor all elements until you get the answer. x ^ x = 0
# new number appears = xor to 'ones'
# number repeated (2x) - removed from 'ones' and xor to 'twos'
# number appears 3rd time - removed from both 'ones' and 'twos'
# final answer is in 'ones' since it hold unique elem
def find_elem_no_help(lst):
	ones = 0 # holds xor of all elements which appeared once
	twos = 0 # holds xor of all elements which appeared twice

	for i in range(len(lst)):
		x = lst[i]
		twos |= ones & x
		ones ^= x
		# common 1's between 'ones' and 'twos' are converted to 0
		not_threes = ~(ones & twos)
		ones &= not_threes
		twos &= not_threes

	return ones


def executeFindElement():
	a = [2,1,4,5,1,4,2,2,4,1]
	print("help with 3 pairs", find_elem(a))

	print("no 3 pairs", find_elem_no_help(a))



'''
/*=======================================
=            Find the Number            =
=======================================*/
given list of numbers where every number comes in pairs but one, 
find the one number that doesn't come in pairs

XOR the numbers. All the pairs will cancel each other out.
O(n)

Or you can use a dictionary
'''

def find_nonduplicate(lst):
	ones = 0

	for i in range(len(lst)):
		ones ^= lst[i]

	return ones

def executeNonDuplicates():
	b = [2,3,6,8,4,7,0,4,7,8,6,2,3]
	print("no duplicates", find_nonduplicate(b))


#/*=====  End of Find the Number  ======*/


'''
/*===========================================================================
=            Given 2 lists are they the same Binary Search Tree?            =
===========================================================================*/
'''

import math
def same_bst(A, B):
	if A[0] != B[0] or len(A) != len(B):
		return False
	elif len(A) == 1:
		return True

	A_left = []
	A_right = []

	for i in A:
		if i < A[0]:
			A_left.append(i)
		elif i > A[0]:
			A_right.append(i)

	B_left = []
	B_right = []

	for i in B:
		if i < B[0]:
			B_left.append(i)
		elif i > B[0]:
			B_right.append(i)

	return same_bst(A_left, B_left) and same_bst(A_right, B_right)


#/*=====  End of Given 2 lists are they the same Binary Search Tree?  ======*/

'''
/*==================================================================
=            Find Length of Square that contains all 1s            =
==================================================================*/
find size of square in 2D array of all 1s
O(M * N)
'''
def max_square_with_one(arr):
	mmax = 0

	print("before")
	pprint(arr)

	for i in range(1, len(arr)):
		for j in range(1, len(arr[i])):
			# ignore if not a 1
			if arr[i][j] != 0:
				curr_min = min(arr[i-1][j-1], min(arr[i-1][j], arr[i][j-1])) + 1
				arr[i][j] = curr_min

				if curr_min > mmax:
					mmax = curr_min

	print("after")
	pprint(arr)

	return mmax

def executeMaxSquare():
	arr = [[0, 1, 1, 0, 1],
			[1, 1, 0, 1, 0],
			[0, 1, 1, 1, 0],
			[1, 1, 1, 1, 0],
			[1, 1, 1, 1, 1],
			[0, 0, 0, 0, 0]]

	print("max square", max_square_with_one(arr))

# /*=====  End of Find Length of Square that contains all 1s  ======*/



'''
/*=================================
=            Min Jumps            =
=================================*/
minimum number of jumps it takes to reach the end where each element tells how far you 
can jump from that spot

'''
def minjumps(lst, index, count):
	if index == len(lst)-1:
		return count
	else:
		e = lst[index]
		count+=1
		x = float('inf')
		for i in range(1, e+1):
			x = min(x, minjumps(lst, index+i, count))
		return x

def executeMinJump():
	c = [2,3,1,1,4]
	print("min jump",  minjumps(c, 0, 0))

# /*=====  End of Min Jumps  ======*/



# recursive
def choose_coins(lst):
	if len(lst) < 1:
		return -1

	if len(lst) == 1:
		return lst[0]

	# I go
	A = lst[0] + min(choose_coins(lst[2:]), choose_coins(lst[1:-1]))
	B = lst[-1] + min(choose_coins(lst[:-2]), choose_coins(lst[1:-1]))

	return max(A, B)

'''
/*=============================================================
=            Strategy Game Pick from Ends of array            =
=============================================================*/
given a list of coins, you and your opponent take turns taking a coin from either end
want to have more value than your opponent to win the game

https://www.youtube.com/watch?v=WxpIHvsu1RI&index=32&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr
'''


# DP
def chooseMax(lst):
	n = len(lst)
	arr = [[(0, 0)] * n for i in range(n)]

	# initialize diagonals
	for i in range(n):
		arr[i][i] = (lst[i], 0)


	for l in range(2, n+1):
		for i in range(n-l+1):
			j = l + i - 1

			firstA = arr[i+1][j][0]
			firstB = arr[i][j-1][0]

			A = lst[i] + arr[i+1][j][1]
			B = lst[j] + arr[i][j-1][1]

			if (A > B):
				first = A
				second = firstA
			else:
				first = B
				second = firstB

			arr[i][j] = (first, second)

	# pprint(arr)

	return arr[0][n-1]


def executeChooseCoin():
	c = [3, 1, 5, 6, 2, 9, 3]
	first, second = chooseMax(c)
	print("maximum sum first player to go can get")
	print(first)
	print("maximum sum second player to go can get")
	print(second)

# /*=====  End of Strategy Game Pick from Ends of array  ======*/

'''
/*============================================
=            Interleaving Strings            =
============================================*/
https://www.youtube.com/watch?v=ih2OZ9-M3OM&index=31&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

O(M * N)
'''
def interleave(a, b, word):
	arr = [[""] * (len(a)+1) for i in range(len(b)+1)]
	arr[0][0] = True

	# initialize first row
	for i in range(len(a)):
		if a[i] == word[i]:
			arr[0][i+1] = True
		else:
			arr[0][i+1] = False

	# initialize first column
	for i in range(len(b)):
		if b[i] == word[i]:
			arr[i+1][0] = True
		else:
			arr[i+1][0] = False

	for i in range(len(b)):
		for j in range(len(a)):
			# if top is equal, check against side
			if word[i+j+1] == a[j]:
				if arr[i+1][j]:
					arr[i+1][j+1] = True
				else:
					arr[i+1][j+1] = False

			# if side is equal, check against top
			elif word[i+j+1] == b[i]:
				if arr[i][j+1]:
					arr[i+1][j+1] = True
				else:
					arr[i+1][j+1] = False

			else:
				arr[i+1][j+1] = False

	# pprint(arr)
	return arr[len(b)][len(a)]


def executeInterleave():
	one = "aab"
	two = "axy"
	s1 = "aaxaby"
	s2 = "abaaxy"

	assert interleave(one, two, s1) == True
	assert interleave(one, two, s2) == False
	print("All tests passing")

#/*=====  End of Interleaving Strings  ======*/


'''
/*==============================================
=            Minimum Number of Coins           =
===============================================*/
https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/CoinChangingMinimumCoin.java

time - O(value * coins)
space - O(value * coins)

Get minimum number of coins to form this total
'''
def changeTopDown(value, coins, d):
	if value == 0:
		return 0

	if value in d:
		return d[value]

	mmin = float('inf')
	for i in coins:
		if i > value:
			continue

		val = changeTopDown(value - i, coins, d)

		if val < mmin:
			mmin = val

	if mmin != float('inf'):
		mmin += 1

	d[value] = mmin
	return mmin

# more common
def changeBottomUp(value, coins):
	T = [float('inf') - 1] * (value+1) #count number of ways
	R = [-1] * (value+1) # get path using parent pointers
	T[0] = 0

	for j in range(len(coins)):
		for i in range(coins[j], value+1):
			if T[i] > T[i-coins[j]] + 1:
				T[i] = 1 + T[i-coins[j]]
				R[i] = j

	printCombination(R, coins)
	return T[value]


# just prints coins used for Bottom Up
def printCombination(R, coins):
	if R[len(R)-1] == -1:
		print("No solution is possible")
		return

	start = len(R) - 1
	print("Coins used to form total: ")
	while start!=0:
		j = R[start]
		print(coins[j], end=", ")
		start -= coins[j]
	print()

def minCoinsToMakeChange():
	value = 13
	coins = [7, 3, 2, 6]
	print(changeTopDown(value, coins, {}))
	print(changeBottomUp(value, coins))

#/*=====  End of Minimum Number of Coins ======*/

'''
/*===================================
=            Coin Change            =
===================================*/
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
Number of ways to make change

'''

# O(mn) space
def numberOfWays(value, coins):
	n = len(coins)
	arr = [[0] * (n)  for i in range(value+1)]

	for i in range(n):
		arr[0][i] = 1

	# fill table up in bottom up manner
	for i in range(1, value+1):
		for j in range(n):

			x = y = 0
			# count solutions including coins[j]
			if i - coins[j] >= 0:
				x = arr[i-coins[j]][j]

			# count solutions excluding coins[j]
			if j >= 1:
				y = arr[i][j-1]

			arr[i][j] = x + y

	pprint(arr)

	return arr[value][n-1]

# bottom up
#  O(n) space 
def numberOfWaysSpace(value, coins):
	arr = [0] * (value+1)

	# base case. when value = 0
	arr[0] = 1

	for coin in coins:
		for j in range(coin, value+1):
			arr[j] += arr[j-coin]


	pprint(arr)
	return arr[value]


def coinChange():
	value = 15
	coins = [3,4,6,7,9]
	print(numberOfWays(value, coins))
	print(numberOfWaysSpace(value, coins))

#/*=====  End of Coin Change  ======*/

'''
/*===============================================
=            Weighted Job Scheduling            =
===============================================*/
https://www.youtube.com/watch?v=cr6Ip0J9izc&index=12&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

O(n^2)
'''
def jobSchedule(jobs, weights):
	arr = weights[:]

	for i in range(1, len(jobs)):
		for j in range(i):
			curr = jobs[i]
			compare = jobs[j]

			if curr[0] >= compare[1]:
				arr[i] = max(arr[i], arr[j] + weights[i])

	return max(arr)


def executeJobSchedule():
	jobs = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (7, 9)]
	weights = [5, 6, 5, 4, 11, 2]
	assert jobSchedule(jobs, weights) == 17
	print("weighted job schedule tests passing")


#/*=====  End of Weighted Job Scheduling  ======*/

'''
/*====================================
=            Cutting Rods            =
====================================*/

'''

def cuttingRods(n, rods, profit):
	arr = [[0] * (n+1) for i in range(len(rods))]

	for i in range(len(rods)):
		for j in range(1, n+1):
			if j < rods[i]:
				arr[i][j] = arr[i-1][j]
			else:
				arr[i][j] = max(arr[i-1][j], profit[i] + arr[i][j-rods[i]])

	# pprint(arr)

	i = len(rods)-1
	j = n

	# value returns optimal value
	value = arr[i][j]


	myset = []

	while i > 0 and j > 0:
		if arr[i][j] == arr[i-1][j]:
			i-=1
		else:
			myset.append(rods[i])
			j-=rods[i]

	while j > 0:
		myset.append(rods[0])
		j -= rods[0]

	# set returns the set of rod sizes I should cut to get the optimal value
	return myset


def executeCuttingRods():
	rods = [1, 2, 3, 4]
	profit = [2, 5, 7, 8]
	assert cuttingRods(5, rods, profit) == [2, 2, 1]
	print("cutting Rods tests passing")

#/*=====  End of Cutting Rods  ======*/

'''
/*================================
=            Egg Drop            =
================================*/
Minimum number of attempts to figure out which floor egg breaks

The basic logic is this.
when I choose a floor to drop the egg, how many attempts does it take 
for the left of that floor and the right of that floor?

Take the max of those 2 and add 1 for my attempt at the current floor.

time: O(egg * floors^2)
space: O(egg * floors)
'''

def eggDrop(eggs, floors):
	arr = [[0] * (floors+1) for i in range(eggs+1)]

	# need 1 trial for 1 floor.
	for i in range(1, eggs+1):
		arr[i][1] = 1

	# need i trials for 1 egg and i floors
	for i in range(2, floors+1):
		arr[1][i] = i

	for i in range(2, eggs+1):
		for j in range(2, floors+1):
			arr[i][j] = float('inf')

			for r in range(1, j+1):
				# arr[i-1][r-1] == compare elements in row above to the left from left to right
				# arr[i][j-r] == compare elements in same row to the left from right to left
				c = 1 + max(arr[i-1][r-1], arr[i][j-r])

				if c < arr[i][j]:
					arr[i][j] = c

	pprint(arr)

	return arr[eggs][floors]

def executeEggDrop():
	eggs = 2
	floors = 10
	print(eggDrop(eggs, floors))
	print("Egg Drop Tests Passed")

#/*=====  End of Egg Drop  ======*/

'''
/*=======================================
=            Skyline Problem            =
=======================================*/
# https://www.youtube.com/watch?v=GSBLe8cKu0s
# https://briangordon.github.io/2014/08/the-skyline-problem.html

Edge Cases:
0,3,S  <- (if x is same and both are Start, need to sort in decreasing y)
0,2,S  <-
1,2,E
2,3,E

3,3,S  (if x is same and both are End, need to sort in increasing y)
4,2,S
5,2,E  <-
5,3,E  <-

6,2,S  (If x is same, and one is Start and one is End, Start should come first)
7,3,S  <-
7,2,E  <-
8,3,E


time is O(nlogn) <- if priority queue is a tree, then adding and removing from queue is logn
space is O(n)

'''
def skyline(lst):
	arr = []
	output = []

	for i in lst:
		# x, y, start?
		arr.append((i[0], i[2], True)) #start
		arr.append((i[1], i[2], False)) #end

	# Not Completely finished
	# Sort needs to handle edge cases
	arr.sort()

	maxHeight = 0
	q = [0]
	# heapq.heappush(q, 0)

	for i in arr:
		if i[2]: #start
			q.append(i[1])
			# heapq.heappush(q, i[1])
			if max(q) > maxHeight:
				maxHeight = max(q)
				output.append((i[0], maxHeight))

		else: #end
			# heapq.heappop(q)
			q.remove(i[1])
			if max(q) != maxHeight:
				maxHeight = max(q)
				output.append((i[0], maxHeight))


	print(arr)
	print()
	print(output)

def executeSkyLine():
	# x1, x2, height
	lst = [(1,3,3), (2,4,4), (5,8,2), (6,7,4), (8,9,4)]
	print(skyline(lst))

	output = [(1,3), (2,4), (4,0), (5,2), (6,4), (7,2), (8,4), (9,0)]

# /*=====  End of Skyline Problem  ======*/


if __name__=="__main__":
	# executeKnapsack()
	# executeFindElement()
	# executeNonDuplicates()
	# executeMaxSquare()
	# executeMinJump()
	# executeChooseCoin()
	# executeInterleave()
	# minCoinsToMakeChange()
	# coinChange()
	
	# executeJobSchedule()
	# executeCuttingRods()
	# executeEggDrop()
	
	executeSkyLine()




