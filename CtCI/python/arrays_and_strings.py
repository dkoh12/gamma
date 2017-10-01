def isUnique(s):
	d = {}
	for i in s:
		if i in d:
			return False
		else:
			d[i] = 1
	return True

from collections import Counter

def isPermutation(a, b):
	A = Counter(a)
	B = Counter(b)

	if A == B:
		return True
	else:
		return False

def urlify(s, num):
	output = ""
	count = 0
	for i in s:
		count+=1
		if count > num:
			break
		if i == " ":
			output += "%20"
		else:
			output += i
	return output

def isPalindrome(s):
	l = ''.join(s.lower().split())
	c = Counter(l)
	odd = [i for (i,j) in c.items() if j%2 != 0]
	
	if len(odd) == 1 or len(odd) == 0:
		return True
	else:
		return False

def oneaway(a, b):
	A = Counter(a)
	B = Counter(b)

	s = A-B

	print(s)
	return len(s) < 2

def stringCompression(s):
	output = ""
	count = 0
	index = 0
	for i in s:
		index += 1
		if output == "":
			output += i
		if output[-1] != i:
			output += str(count)
			count = 0
			output += i
		
		count+=1

		if index == len(s):
			output += str(count)

	if len(output) >= len(s):
		return s
	else:
		return output

def zeroOut(arr):
	zeros = []
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if arr[i][j] == 0:
				zeros.append((i,j))

	for elem in zeros:
		i, j = elem
		arr[i] = len(arr[i]) * [0]
		for y in range(len(arr)):
			arr[y][j] = 0

	return arr


class myStack:

	def __init__(self):
		self.lst = []
		print(">> created a new stack")

	def print(self):
		print(self.lst)

	def add(self, item):
		if self.isEmpty():
			self.lst.append((item, item))
		else:
			minimum = self.lst[-1][1]
			minimum = min(minimum, item)
			self.lst.append((item, minimum))

	def remove(self):
		i = self.lst.pop()
		print("%d removed" % i[0])

	def peek(self):
		if self.isEmpty():
			raise IndexError
		print(self.lst[-1][0])

	def isEmpty(self):
		return len(self.lst) == 0

	def min(self):
		if self.isEmpty():
			raise IndexError
		print("min is %d" % self.lst[-1][1])

	def len(self):
		return len(self.lst)

class myQueue:

	def __init__(self):
		self.lst = []
		print(">> created a new queue")

	def print(self):
		print(self.lst)

	def add(self, item):
		self.lst.append(item)

	def remove(self):
		if self.isEmpty():
			raise IndexError
		i = self.lst[0]
		self.lst = self.lst[1:]
		print("%d removed" % i)

	def peek(self):
		if self.isEmpty():
			raise IndexError
		print(self.lst[0])

	def isEmpty(self):
		return len(self.lst) == 0

	def len(self):
		return len(self.lst)

# a set of stacks. Once a stack has hit a threshold, create another stack. 
# but add and remove should only work on one stack. 
class SetOfStacks:

	def __init__(self, threshold):
		self.lst = []
		self.index = 0
		self.threshold = threshold

	def len(self):
		return len(self.lst)

	def print(self, index):
		return self.lst[index].print()

	def add(self, item):
		if len(self.lst) == 0:
			s = myStack()
			self.lst = [s]
			self.lst[0].add(item)
		else:
			if self.lst[self.index].len() == self.threshold:
				s = myStack()
				self.lst.append(s)
				self.index += 1
				self.lst[self.index].add(item)
			else:
				self.lst[self.index].add(item)

	def remove(self, index=None):
		if index == None:
			index = self.index
		if self.lst[index].len() == 0:
			self.lst[index].remove()
			self.index -= 1
			self.lst[index].remove()
		else:
			self.lst[index].remove()

	# pops from a specific stack
	def removeAt(self, index):
		self.lst[index].remove()



# Make a Queue using 2 stacks
# enqueue
# 1. push x to stack1
# dequeue
# 1. if both stacks are empty, error
# 2. if stack2 is empty, while stack1 is not empty, push everything from stack1 to stack2
# 3. pop element from stack2 and return it

class Queue_with_stacks:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self, x):
		self.stack1.append(x)

	def dequeue(self):
		if len(self.stack1) == 0 and len(self.stack2) == 0:
			return "Queue is empty"
		if len(self.stack2) == 0:
			while len(self.stack1) != 0:
				x = self.stack1.pop()
				self.stack2.append(x)

		return self.stack2.pop()


def test():
	assert isUnique("hello") == False
	assert isUnique("abcdef") == True

	assert isPermutation("hello", "lolhe") == True
	assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"

	assert isPalindrome("Tact Coa") == True

	assert oneaway("pale", "ale") == True
	assert oneaway("pale", "pales") == True
	assert oneaway("pale", "bake") == False

	assert stringCompression("aabcccccaaa") == "a2b1c5a3"
	assert stringCompression("abcca") == "abcca"


	print("All tests passing")

if __name__=="__main__":
	test()

	# mat = [[1, 2, 3, 0], [4, 5, 6, 0], [7,5,3,2], [7, 0, 9, 8]]
	# print(zeroOut(mat))

	# s = myStack()
	# s.add(5)
	# s.add(7)
	# s.add(4)
	# s.min()
	# s.print()
	# s.remove()
	# s.remove()	
	# s.peek()
	# s.min()
	# s.print()

	# q = myQueue()
	# q.add(2)
	# q.add(3)
	# q.add(6)
	# q.print()
	# q.remove()
	# q.peek()
	# q.print()


	# def printSS():
	# 	for i in range(S.len()):
	# 		S.print(i)

	# S = SetOfStacks(3)
	# S.add(4)
	# S.add(5)
	# S.add(6)
	# S.add(7)
	# S.add(8)
	# printSS()
	# S.remove()
	# printSS()
	# S.removeAt(0)
	# S.removeAt(0)
	# printSS()

	qs = Queue_with_stacks()
	qs.enqueue(1)
	qs.enqueue(2)
	qs.enqueue(3)

	print(qs.dequeue())
	print(qs.dequeue())
	print(qs.dequeue())





