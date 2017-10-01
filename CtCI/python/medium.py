import math

# count how many trailizing zeros there are of n factorial
def trailing_zeros(n):
	times = math.log(n)//math.log(5)

	total = 0
	for i in range(1, int(times)+1):
		total += n // math.pow(5, i)

	return total


def smallest_difference(a, b):
	return min([abs(x-y) for x in a for y in b])

def contiguous_seq(seq):
	total = 0
	currmax = 0
	for i in seq:
		total += i
		if total > currmax:
			currmax = total
		if total < 0:
			total = 0

	return currmax

# find all pairs of integers w/in array which sum to a specific value
def pairs(lst, num):
	s = dict()
	count = 0
	for i in lst:
		if i not in s:
			s[i] = num - i
			if s[i] in s:
				count += 1	

	return count

import re

# def compute(s):
# 	re.split('+-*/', s)

# 	print(s)
	
# 	return s


def getKey(item):
	return item[0]

def getVal(item):
	return item[1]


def lis(arr):
	if len(arr) == 0:
		return 0

	lst = [1] * len(arr)
	for i in range(1, len(arr)):
		for j in range(0, i):
			if arr[i] > arr[j] and lst[i] < lst[j]+1:
				lst[i] = lst[j]+1
	print(lst)
	return max(lst)

# sample = [2,6,3,4,1,2,9,5,8] 
# arr = [5,2,8,6,3,6,9,7]
# print(lis(sample))
# print(lis(arr))

# sort by 1 tuple value then lis on the other value
def tower(people):
	height = sorted(people, key=getKey) # sort it based on height
	
	weight = [i[1] for i in height]

	# print(height)
	# print(weight)

	return lis(weight)


def appt(lst):
	if len(lst) <= 0:
		return 0

	return max(lst[0] + appt(lst[2:]), appt(lst[1:]))


def find_max(lst):
	# print("findmax\n")

	if len(lst) <= 1:
		return 0

	# print("list", lst)

	m = max(lst)
	i = lst.index(m)

	total = 0

	if i != 0:
		l = max(lst[:i])
		li = lst.index(l)
		# print("i", i, "li", li)

		total += l * (i-li-1)

		for j in range(li+1, i):
			if lst[j] != 0:
				total -= lst[j]
	else:
		li = i

	if i != len(lst):
		r = max(lst[i+1:])
		ri = lst.index(r)
		# print("i", i, "ri", ri)

		total += r * (ri-i-1)

		for j in range(i+1, ri):
			if lst[j] != 0:
				total -= lst[j]
	else:
		ri = len(lst)


	# print("tot", total)

	return total + find_max(lst[:li]) + find_max(lst[ri:])


def histogram(lst):

	while lst[0] == 0:
		lst = lst[1:]

	if len(lst) == 0:
		return 0

	while lst[-1] == 0:
		lst = lst[:-1]

	return find_max(lst)

	# leftside = 0
	# count = 0
	# inbetween = []
	# area = 0
	# for index, i in enumerate(range(lst)):
	# 	if i != 0 and leftside == 0:
	# 		leftside = (index, i)
	# 	if i == 0:
	# 		count += 1
	# 	if i != 0 and leftside[1] != 0 and leftside[0] != i:
	# 		rightside = (index, i)
	# 		if rightside[1] >= leftside[1]:
	# 			area += count * leftside[1]
	# 			count = 0
	# 			leftside = rightside
	# 			rightside = 0
	# 		else:
	# 			inbetween.append((count, (index, i)))
	# 			count = 0

	# 	area += min(leftside, rightside) * 

import itertools

def similarity(ss):
	pairs = ss.keys()

	l = list(itertools.combinations(pairs, 2))

	for i, j in l:
		num = len(ss[i] & ss[j])
		if num == 0:
			continue
		denom = len(ss[i] | ss[j])
		print((i, j), num/denom)


# S is a substring within B. find it
# O(B) where B is length of original string
def substring_match(S, B):
	match = 0 #hash of substring S
	for i in S:
		match += ord(i)

	code = []

	val = -1
	for i in range(len(B)-len(S)+1):
		if val == -1:
			val = 0
			for j in range(len(S)):
				val += ord(B[j])
		else:
			# print(B[i], val)
			# print("minus", B[i-1], ord(B[i-1]))
			# print("plus", B[i+len(S)-1], ord(B[i+len(S)-1]))
			val -= ord(B[i-1])
			val += ord(B[i+len(S)-1])

		code.append((B[i], val))

	# print(code)

	for index, j in enumerate(code):
		if j[1] == match:
			matched = True
			for i in range(index, index+len(S)):
				if B[i] != S[i-index]:
					matched = False
					break
			if matched:
				return index
				break

	return -1


def test():
	assert trailing_zeros(5) == 1
	assert trailing_zeros(25) == 6

	input1 = {1, 3, 15, 11, 2}
	input2 = {23, 127, 235, 19, 8}
	assert smallest_difference(input1, input2) == 3

	seq = [2, -8, 3, -2, 4, -10]
	assert contiguous_seq(seq) == 5

	lst = [1, 4, 6, 8, 15, 2, 7, 3]
	assert pairs(lst, 10) == 3

	# eq = '2*3+5/6*3+15'
	# compute(eq)

	people = [(65, 40), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
	# print(tower(people))

	appointments = [30, 15, 60, 75, 45, 15, 15, 45]
	assert appt(appointments) == 180

	bar = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
	assert histogram(bar) == 26

	ss = dict()
	ss[13] = set([14, 15, 100, 9, 3])
	ss[16] = set([32, 1, 9, 3, 5])
	ss[19] = set([15, 29, 2, 6, 8, 7])
	ss[24] = set([7, 10])
	similarity(ss)

	S = "ear"
	B = "doe are hearing me"
	assert substring_match(S, B) == 9


	print("all tests passing")



if __name__=="__main__":
	test()