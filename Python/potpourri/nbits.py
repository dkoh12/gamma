

'''
/*=============================
=            NBits            =
=============================*/
http://algorithms.tutorialhorizon.com/generate-all-strings-of-n-bits/

ie. n = 2
reutrn [0,0],[0,1],[1,0],[1,1]
'''
def NBits(arr, n):
	if n <= 0:
		print(arr)
	else:
		arr[n-1] = 0
		NBits(arr, n-1) # kind of backtracking
		arr[n-1] = 1
		NBits(arr, n-1)	


def executeNBits():
	n = 3
	arr = [0] * n
	NBits(arr, n)


# /*=====  End of NBits  ======*/
'''
/*=====================================================================
=            Smallest Subarray with sum greater than value            =
=====================================================================*/
http://algorithms.tutorialhorizon.com/in-an-array-find-the-smallest-subarray-with-sum-greater-than-the-given-value/

easy way would be to sort it in descending order and take the minimum elements to exceed n

time = O(n).
While less than n, insert the number. Else go back to the start of the array and subtract it

^ I feel like this is not guaranteed to be optimal

'''

def small(lst, n):
	# res = []
	start = 0
	ansEnd = 0
	ansStart = 0
	currsum = 0 
	minlen = len(lst)

	for i in range(len(lst)+1):
		while currsum > n:
			currsum -= lst[start]
			if (i-start <= minlen):
				minlen = i - start
				ansEnd = i
				ansStart = start
			start += 1

		if i < len(lst):
			currsum += lst[i]

	return minlen, lst[ansStart:ansEnd+1]


def executeSmall():
	arr = [10,40,20,70,8] # not optimal
	ans = 97
	print(small(arr, ans))

# /*=====  End of Smallest Subarray with sum greater than value  ======*/

'''
/*==========================================
=            Water in Bar Graph            =
==========================================*/
https://www.youtube.com/watch?v=UzeL2GcLx3Y

time = O(n)

have 2 arrays. 
one array computes biggest value from left side
one array computes biggest value from right side

Then for each element, take the minimum of the 2 arrays and subtract it from the list
'''

def rainfall(lst):
	left = []
	leftmax = -1

	for i in lst:
		if not left:
			left.append(leftmax)
			leftmax = i
		else:
			if i < leftmax:
				left.append(leftmax)
			else:
				left.append(-1)
				leftmax = i

	right = []
	rightmax = -1
	for i in range(len(lst)-1,-1,-1):
		if not right:
			right.append(rightmax)
			rightmax = lst[i]
		else:
			if lst[i] < rightmax:
				right.append(rightmax)
			else:
				right.append(-1)
				rightmax = lst[i]

	right.reverse()

	print(left)
	print(right)

	total = 0
	for i in range(len(left)):
		m = min(left[i], right[i])
		if m != -1:
			total += m - lst[i]


	return total

def executeRainfall():
	# arr = [5, 1, 3, 4]
	arr = [1,6,3,7,4,5,2]
	print(rainfall(arr))

# /*=====  End of Water in Bar Graph  ======*/

'''
/*=============================================
=            Max Area in Histogram            =
=============================================*/
http://www.geeksforgeeks.org/largest-rectangle-under-histogram/
https://www.youtube.com/watch?v=ZmnqCZp9bBs

time = O(n)


USE THIS TO DISPLAY
http://www.pythontutor.com/visualize.html#mode=display

'''
def histogram(lst):
	stack = []
	mmax = 0

	i=0
	while i < len(lst):
		if not stack or lst[stack[-1]] <= lst[i]:
			stack.append(i)
			i += 1

		else:
			p = stack.pop()

			if not stack:
				# lst[p] is smallest number so  we multiply entire width by this number
				area = lst[p] * i
			else:
				area = lst[p] * (i - stack[-1] - 1)

			if mmax < area:
				mmax = area

	# tail case
	while stack:
		p = stack.pop()

		if not stack:
			area = lst[p] * i
		else:
			area = lst[p] * (i- 1 - stack[-1])

		if mmax < area:
			mmax = area

	return mmax


def executeHistogram():
	# lst = [2,1,2,3,1]
	lst = [6, 2, 5, 4, 5, 1, 6]
	print(histogram(lst))


#/*=====  End of Max Area in Histogram  ======*/

'''
/*========================================
=            Max Subarray Sum            =
========================================*/
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

time = O(n)

'''

def maxSubarraySum(arr):
	currmax = 0
	total = 0
	start, end, s = 0, 0, 0

	for i in range(len(arr)):
		total += arr[i]
		if total < 0:
			total = 0
			s = i+1

		if currmax < total:
			currmax = total
			start = s
			end = i+1

	return currmax, arr[start:end]


def executeSubarraySum():
	arr = [-2,-3,4,-1,-2,1,5,-3]
	print(maxSubarraySum(arr))



# /*=====  End of Max Subarray Sum  ======*/

'''
/*=============================================
=            Expression Evaluation            =
=============================================*/
http://www.geeksforgeeks.org/expression-evaluation/

'''


def expressionEvaluate(lst):
	values = []
	ops = []

	i=0
	while i < len(lst):
		if lst[i] == ' ':
			i+=1
			continue

		if lst[i] >= '0' and lst[i] <= '9':
			s = ""
			while i < len(lst) and lst[i] >= '0' and lst[i] <= '9':
				s += lst[i]
				i+=1
			values.append(int(s))

		elif lst[i] == '(':
			ops.append(lst[i])
			i+=1

		elif lst[i] == ')':
			while ops[-1] != '(':
				values.append(applyOp(ops.pop(), values.pop(), values.pop()))
			ops.pop()
			i+=1

		elif lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or \
			lst[i] == '/':
			while ops and hasPrecedence(lst[i], ops[-1]):
				values.append(applyOp(ops.pop(), values.pop(), values.pop()))
			ops.append(lst[i])
			i+=1

	while ops:
		values.append(applyOp(ops.pop(), values.pop(), values.pop()))

	return values[-1]


def hasPrecedence(op1, op2):
	if op2 == '(' or op2 == ')':
		return False
	if (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
		return False
	return True

def applyOp(op, b, a):
	if op == '+':
		return a+b
	elif op == '-':
		return a-b
	elif op == '*':
		return a*b
	elif op == '/':
		if b == 0:
			raise ValueError("cannot divide by 0")
		return a/b

	return 0

def executeExpression():
	a = '10 + 2 * 6'
	b = '100 * 2 + 12'
	c = '100 * ( 2 + 12 )'
	d = '100 * ( 2 + 12 ) / 14'
	assert expressionEvaluate(a) == 22 
	assert expressionEvaluate(b) == 212
	assert expressionEvaluate(c) == 1400
	assert expressionEvaluate(d) == 100.0
	print("Execute Expression Tests Passing!!")


# /*=====  End of Expression Evaluation  ======*/

'''
/*==================================
=            Stock Span            =
==================================*/
http://www.geeksforgeeks.org/the-stock-span-problem/

Print out an array where each element corresponds to how many consecutive days this number was the maximum

O(n)
'''

def stockspan(lst):
	res = []
	stack = []

	for i, item in enumerate(lst):
		if not stack:
			stack.append((1, item))
			res.append(1)
			continue

		# if right elem > left elem, always 1
		if item < stack[-1][1]:
			stack.append((1, item))
			res.append(1)
		else:
			count = 1
			# pop it off the stack and increment the counter
			while len(stack) != 0 and item >= stack[-1][1]:
				p = stack.pop()
				count += p[0]

			stack.append((count, item))
			res.append(count)

	return res


def executeStockSpan():
	lst = [10,20,60,55,54,30,45,58, 7,90]
	assert stockspan(lst) == [1,2,3,1,1,1,2,5,1,10]
	print("Stock Span Test Passing")


# /*=====  End of Stock Span  ======*/

'''
/*=========================================
=            Celebrity Problem            =
=========================================*/
http://www.geeksforgeeks.org/the-celebrity-problem/

Problem
-------
You have a room with N people. Everyone knows a celebrity. The celebrity knows no one.
Non-celebrities may/may not know anyone in the room. Give an algorithm to find the celebrity. 



Brute Force O(n^2)
-----------
Have a graph with edges between vertices and indegrees and outdegrees. If celebrity is present, we will ahve
one sink node with outdegree = 0. 

Constructing the graph takes O(N^2) time


Stack O(n)
-----
1) If A knows B, A can't be celebrity. Discard A
2) If A doesn't know B, B can't be celebrity. Discard B
Repeat above steps
3) Ensure remained person is celebrity. Check he doesn't have acquaintance with anyone else

Ensure it by using a stack.

Push all celebrities to a stack. Pop off 2 and discard one person.
Repeat until only 1 remains in stack


Array O(n) (same as stack solution)
------
Make people stand in a row.
Compare A and B
1) If A knows B => A is not celebrity
2) if A doesn't know B => B is not celebrity

If A and B both don't know each other then by rule 2, eliminate both A and B




def findCelebrity(self, n):
    x = 0
    for i in range(n):
        if knows(x, i):
            x = i
    if any(knows(x, i) for i in xrange(x)):
        return -1
    if any(not knows(i, x) for i in xrange(n)):
        return -1
    return x





/*=====  End of Celebrity Problem  ======*/
'''

'''
/*=================================================
=            Reverse Words in a string            =
=================================================*/
http://www.geeksforgeeks.org/reverse-words-in-a-given-string/

'''

def reverse_words(lst):
	lst = lst[::-1]
	lst = list(lst.split(" "))

	for i in range(len(lst)):
		lst[i] = lst[i][::-1]

	return ' '.join(lst)

def execute_reverse():
	s = "The eagle has landed"
	print(reverse_words(s))

#/*=====  End of Reverse Words in a string  ======*/





if __name__=="__main__":
	executeNBits()
	executeSmall()
	executeRainfall()
	executeHistogram()
	executeSubarraySum()
	executeExpression()
	executeStockSpan()
	execute_reverse()





