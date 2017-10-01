from pprint import pprint

'''
/*=======================================================
=            Longest Increasing Subsequence             =
=======================================================*/
returns len of longest increasing subsequence
TIME: O(n^2)

The lst[i] < lst[j]+1 is here to prevent
10 9 21 from double updating

so the longest path is either 10 21 or 9 21 but not 10 9 21


'''
def longest_increasing_subsequence(arr):
	if arr == []:
		return 0

	n = len(arr)
	lst = [1] * n

	for i in range(1, n):
		for j in range(0, i):
			if arr[i] > arr[j] and lst[i] < lst[j]+1:
				lst[i] = lst[j]+1

	return max(lst)

#/*=====  End of Longest Increasing Subsequence   ======*/

'''
/*===================================================
=            Longest Bitonic Subsequence            =
===================================================*/
http://www.geeksforgeeks.org/dynamic-programming-set-15-longest-bitonic-subsequence/

bitonic sequence is a sequence where numbers increase then decrease

arr[] = {1, 11, 2, 10, 4, 5, 2, 1}

longest bitonic sequence = {1, 2, 10, 4, 2, 1} => 6

TIME: O(n^2)
Space: O(n)

Idea is do longest increasing subsequence from both the left side and the right side.
sum the two arrays and subtract one (don't overcount) and find the max
'''

def lbs(arr):

	left = [1] * len(arr)
	right = [1] * len(arr)

	for i in range(len(arr)):
		for j in range(i):
			if arr[i] > arr[j] and left[i] < left[j] + 1:
				left[i] = left[j] + 1

	for i in range(len(arr)-1,-1,-1):
		for j in range(i-1,-1,-1):
			if arr[j] > arr[i] and right[j] < right[i] + 1:
				right[j] = right[i] + 1


	total = []
	for i in range(len(arr)):
		total.append(left[i]+right[i]-1)

	# print("left", left)
	# print("right", right)
	# print("total", total)

	return max(total)


def execute_bitonic():
	arr = [1, 11, 2, 10, 4, 5, 2, 1]
	assert lbs(arr) == 6
	print("Longest Bitonic Sequence Tests Passing")

#/*=====  End of Longest Bitonic Subsequence  ======*/

#recursive
def max_sum_no_two_neighbors(lst):
	if len(lst) < 1:
		return 0
	if len(lst) == 1:
		return lst[0]

	return max(lst[0] + max_sum_no_two_neighbors(lst[2:]), max_sum_no_two_neighbors(lst[1:]))

'''
/*============================================================
=            Maximum Sum Subsequence Non-adjacent            =
============================================================*/
https://www.youtube.com/watch?v=UtGtF6nc35g&index=34&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

inclusive: max sum including curr elem
exclusive: max sum not including curr elem

O(n)
'''

def nonAdj(arr):
	if len(arr) == 0:
		return 0

	inclusive = 0
	exclusive = 0
	for i in arr:
		temp = max(exclusive + i, inclusive)
		exclusive = inclusive
		inclusive = temp

	return inclusive


def executeNonAdj():
	arr = [4, 1, 1, 4, 2,1 ]
	assert nonAdj(arr) == 9
	print("Non Adjacent Maximum Sum Tests Passing")

#/*=====  End of Maximum Sum Subsequence Non-adjacent  ======*/


'''
/*===========================================================
=            Longest Increasing Subsequence Path            =
===========================================================*/
basic idea is this
http://www.geeksforgeeks.org/?p=27614

if curr elem is smallest among all ends, start a new list with len of 1
if curr elem is largest among all ends, clone largest active list and extend it by curr
if curr elem is in between, find list with largest end element smaller than curr
clone and extend this list by curr. discard all other lists of same length


list of paths
0
0 1
0 1 3
0 2 6 9 11
0 1 3 7
0 2 6 9 11 15


>> each element of tail[] indicates largest index of an increasing path

index 	0 1 2 3  4 5  6 7  8 9 10 11 12 13 14 15
arr 	0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15
parent	N 0 0 2  0 4  4 6  0 6 8 9  8 9  12 13
tail    0 8 12 14 13 15

0 -> 0
8 -> 0 1
12 -> 0 1 3
14 -> 0 1 3 7
13 -> 0 2 6 9 11
15 -> 0 2 6 9 11 15

'''


'''
we do a binary search to find the index to replace.
what this is doing is when we find an array of same length delete that array.
Look @ curr elem is in-between
'''
def binarysearch(arr, tail, index):
	low = 0
	high = len(tail) -1

	while high > low:
		mid = (high + low) // 2
		if arr[tail[mid]] < arr[index]:
			low = mid+1
		else:
			high = mid
	return high

# O(n log n)
def lis_path(arr):
	# we use tail[] to update our parent[]
	# When we want to actually get the LIS path, we only care about last index of tail
	tail = [] 

	parent = [None] * len(arr)

	for i in range(len(arr)):
		# handles appending to LIS
		if not tail or arr[i] > arr[tail[-1]]:
			if len(tail) > 0:
				parent[i] = tail[-1]

			tail.append(i)
		else:
			replaced_index = binarysearch(arr, tail, i)
			tail[replaced_index] = i

			if replaced_index != 0:
				parent[i] = tail[replaced_index-1]

	# print("######")

	# print("parent", parent)
	# print("tail", tail)
	# print("arr", arr)

	# printing path

	# WE DONT CARE ABOUT TAIL EXCEPT THE VERY LAST ELEMENT of tail which is largest index!!!
	# then trace parent[] to get elements

	curr = tail[-1]
	path = []
	while curr is not None:
		path.append(arr[curr])
		curr = parent[curr]

	path.reverse()
	return path



def executeLIS():
	sample = [2,6,3,4,1,2,9,5,8] 
	arr = [5,2,8,6,3,6,9,7]
	assert longest_increasing_subsequence(arr) == 4
	assert lis_path(sample) == [2, 3, 4, 5, 8]
	print("Longest Increasing Subsequence Tests passing")


#/*=====  End of Longest Increasing Subsequence Path  ======*/

'''
/*==================================================
=            Longest Common Subsequence            =
==================================================*/
to find len of longest common subsequence you return the index
prints path


aside
-----
to find the longest common substring instead of taking the max of top and left
when the 2 are not equal, just set it to 0. then return the largest number you've found

substrings must be consecutive unlike a subsequence
'''

def lcs(a,b):
	arr = [[0] * (len(a)+1) for j in range(len(b)+1)]

	for i in range(1, len(b)+1):
		for j in range(1, len(a)+1):
			if a[j-1] == b[i-1]:
				arr[i][j] = 1 + arr[i-1][j-1]
			else:
				arr[i][j] = max(arr[i][j-1], arr[i-1][j])

	index = arr[len(b)][len(a)]
	# pprint(arr)

	#UP TO HERE WILL RETURN LENGTH OF LONGEST COMMON SUBSEQUENCE

	c = ""
	i=len(b)
	j=len(a)
	while i >0 and j>0:
		if a[j-1] == b[i-1]:
			c += a[j-1]
			i-=1
			j-=1
		elif arr[i-1][j] > arr[i][j-1]:
			i-=1
		else:
			j-=1

	return c[::-1]


def executeLCS():
	a = "acbaed"
	b = "abcadf"
	assert lcs(a, b) == 'acad'
	print("Longest Common Subsequence Tests Passing")

# /*=====  End of Longest Common Subsequence  ======*/


def longest_palindrome_subsequence(s):

	if len(s) == 1:
		return 1
	if s[0] == s[-1]:
		return 2 + longest_palindrome_subsequence(s[1:-1])
	else:
		return max(longest_palindrome_subsequence(s[1:]), longest_palindrome_subsequence(s[:-1]))

'''
/*=================================================
=            All Palindrome Substrings            =
=================================================*/
https://codereview.stackexchange.com/questions/110079/find-all-distinct-palindromic-sub-strings-for-a-given-string

O(n * m)
where n = len of s, m = number of palindromes

If there are few palindromes, then runtime goes to O(n)
'''

def allpalindrome(s):

	results = set()
	n = len(s)
	for i, ch in enumerate(s):

		# check for longest odd palindrome(s)
		start, end = i-1, i+1
		while start >= 0 and end < n and s[start] == s[end]:
			results.add(s[start:end+1])
			start -= 1
			end += 1

		# check for longest even palindrome(s)
		start, end = i, i+1
		while start >= 0 and end < n and s[start] == s[end]:
			results.add(s[start:end+1])
			start -= 1
			end += 1

	return list(results)


def executeAllPalindrome():
	s = 'abaaa'
	print(allpalindrome(s))
	print("All Palindrome Tests passing")


#/*=====  End of All Palindrome Substrings  ======*/



'''
/*====================================================
=            Longest Palindrome Substring            =
====================================================*/
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/
http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/

time = O(n^2)
space = O(n^2)
'''

def lpsubstr(s):
	arr = [[0] *len(s) for j in range(len(s))]

	for i in range(len(s)):
		arr[i][i] = True

	# check for substrings of length 2
	start = 0
	mmax = 1  #<-- max len is just L

	for l in range(2, len(s)+1):
		for i in range(len(s)-l+1):
			j = i+l-1

			if (l == 2 and s[i] == s[j]):
				arr[i][j] = True
				start = i
				mmax = l

			# if previous was a palindrome and extending the ends is also a palindrome, update
			if(arr[i+1][j-1] and s[i] == s[j]):
				arr[i][j] = True

				if l > mmax:
					start = i
					mmax = l

	pprint(arr)

	print(start, mmax)
	print(s[start:start+mmax])

	return s[start:start+mmax]


def executeLPSubstr():
	# s = "forgeeksskeegfor"
	s = 'abba'

	print(lpsubstr(s))
	# assert lpsubstr(s) == 'geeksskeeg'
	print("Longest Palindrome Substring Passing")


# /*=====  End of Longest Palindrome Substring  ======*/


'''
/*======================================================
=            Longest Palindrome Subsequence            =
======================================================*/
finds longest palindrome subsequence but memoized. 
http://algorithms.tutorialhorizon.com/longest-palindromic-subsequence/


very similar to longest common subsequence.
'''

def lps(s):

	arr = [[0] * len(s) for j in range(len(s))]

	for i in range(len(s)):
		arr[i][i] = 1

	for l in range(2, len(s)+1):
		for i in range(len(s)-l+1):
			j=i+l-1

			if s[j] == s[i] and l == 2:
				arr[i][j] = 2
			elif s[i] == s[j]:
				arr[i][j] = arr[i+1][j-1]+2
			else:
				arr[i][j] = max(arr[i+1][j], arr[i][j-1])

	# for i in range(len(arr)):
	# 	print(arr[i])
	# 	
	# pprint(arr)


	# prints out the sequence. 
	# If square is 2+left diagonal square, then they are in palindrome sequence.
	# Add the sequence via index, sort it, and join it

	i = 0
	j = len(s)-1
	lst = []
	while (i != j):
		
		if arr[i][j] == arr[i+1][j]:
			i += 1
		elif arr[i][j] == arr[i][j-1]:
			j -= 1
		elif arr[i][j] == arr[i+1][j-1] + 2:
			lst.append((i, s[i])) # remember to append the index so you can sort later
			lst.append((j, s[j]))
			i += 1
			j -= 1

	lst.append((i, s[i]))
	lst.sort()

	lst = [i[1] for i in lst]
	seq = ''.join(lst)

	return seq


	# 0 and 5 are in it 



def executeLPS():
	s = "AABCDEBAZ"
	# print(lps(s))
	assert lps(s) == "ABEBA"
	assert len(lps(s)) == 5
	print("Longest Palindrome Sequence Tests passing")


#/*=====  End of Longest Palindrome Subsequence  ======*/


# recursive
def edit_distance(a, b, n, m):

	if m == 0:
		return n
	if n == 0:
		return m

	if a[n-1] == b[m-1]:
		return edit_distance(a, b, n-1, m-1)

	return 1 + min(edit_distance(a, b, n, m-1), edit_distance(a, b, n-1, m), edit_distance(a, b, n-1, m-1))

'''
/*=====================================
=            Edit Distance            =
=====================================*/
https://www.youtube.com/watch?v=We3YDTzNXEk&index=8&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

'''

def edit_distance_op(a, b):
	n = len(a)
	m = len(b)

	arr = [[0] * (m+1) for j in range(n+1)] # m x n

	for i in range(n+1):
		arr[i][0] = i
	for j in range(m+1):
		arr[0][j] = j

	for j in range(1, m+1):
		for i in range(1, n+1):
			if a[i-1] == b[j-1]:
				arr[i][j] = arr[i-1][j-1]
			else:
				# remove, insert, replace
				arr[i][j] = 1 + min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) #really the only diff between lcs and edit

	# for i in range(n+1):
	# 	print(arr[i])

	return arr[n][m]


def executeEditDistance():
	x = "exponential"
	y = "polynomial"
	# assert edit_distance(x, y, len(x), len(y)) == 6
	assert edit_distance_op(x, y) == 6
	print("Edit Distance Test passing")


# /*=====  End of Edit Distance  ======*/

'''
/*======================================
=            Sliding Window            =
======================================*/
sliding window min/max DP
http://www.zrzahid.com/sliding-window-minmax/
divide array into blocks with width w.
take left min window (min of window from left side) and right min window 
(min of window from right side) and take overall min
'''

def sliding_window(arr, width):
	# print(arr)

	i =0 
	left_min = []
	right_min = []
	while i < len(arr):
		window = arr[i:i+width]
		lmin_window = [window[0]]
		rmin_window = [window[-1]]

		#print("rmin window", rmin_window)

		for j in range(2, len(window)+1):
			lmin_window.append(min(arr[i:i+j]))
			
			rmin_window.append(min(arr[i+len(window)-j:i+len(window)]))

		left_min.extend(lmin_window)
		right_min.extend(rmin_window[::-1])

		i+=width

	mmin = []
	for i in range(len(arr)-width+1):
		mmin.append(min(left_min[i+width-1], right_min[i]))

	return mmin



def executeSlidingWindow():
	# w = [1, 2, -1, -3, 4, 2, 5, 3]
	w = [2, 1, 3, 4, 6, 3, 8, 9, 10, 12, 56]
	assert sliding_window(w, 4) == [1, 1, 3, 3, 3, 3, 8, 9]
	# print("sliding window", sliding_window(w, 4))



# /*=====  End of Sliding Window  ======*/


#  O(2^n)
# return max value with max weight W
def knapsack(W, wt, val, n):
	if n == 0 or W == 0:
		return 0

	# cannot include weight of nth item if it is more than knapsack
	if wt[n-1] > W:
		return knapsack(W, wt, val, n-1)
	else:
		return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n-1), knapsack(W, wt, val, n-1))


'''
/*================================
=            Knapsack            =
================================*/
https://www.youtube.com/watch?v=8LusJS5-AGo&index=1&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr

O(nW) where n = number of items and W is capacity of knapsack

Bottom Up
'''

# weight and non repeating elem
def dp_knapsack(W, weight, value):
	n = len(value)
	K = [[0]*(W+1) for x in range(n+1)]

	for i in range(n):
		for j in range(1, W+1):

			# max of including the value vs excluding the value
			if j >= weight[i]:
				K[i+1][j] = max(value[i] + K[i][j-weight[i]], K[i][j])
			else:
				K[i+1][j] = K[i][j]

	pprint(K)

	return K[n][W]

# difference is repeated uses 1D array and get rid of else statement
# O(nW) with repeated numbers
def knapsack_repeat(W, weight, value):
	n = len(value)
	K = [0] * (W+1)

	for i in range(1, W+1):
		for j in range(n):
			if i >= weight[j]:
				K[i] = max(K[i-weight[j]] + value[j], K[i])

	pprint(K)

	return K[W]

# Knapsack_repeat should always be greater than or equal to knapsack no repeat
# 
def executeKnapsack():
	value = [1, 4, 5, 7]
	weight = [1, 3, 4, 5]
	W = 10

	assert dp_knapsack(W, weight, value) == 13
	print()
	assert knapsack_repeat(W, weight, value) == 14
	
	print("Knapsack Tests Passing")


#/*=====  End of Knapsack  ======*/






def test():
	print("all tests passing")


if __name__=="__main__":
	# execute_bitonic()
	# executeNonAdj()
	executeKnapsack()
	# executeEditDistance()
	# executeLCS()
	# executeAllPalindrome()
	# executeLPSubstr()
	executeLPS()
	# executeLIS()
	# executeSlidingWindow()
	# test()


