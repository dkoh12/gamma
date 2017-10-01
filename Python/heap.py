# http://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
# http://interactivepython.org/runestone/static/pythonds/index.html

#  median is n/2 th element

class minHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def bubbleUp(self, i):
		while i//2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
			i = i // 2

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize += 1
		self.bubbleUp(self.currentSize)

	def bubbleDown(self, i):
		while (i*2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
			i = mc

	def minChild(self, i):
		if i*2+1 > self.currentSize:
			return i*2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i*2
			else:
				return i*2 + 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self.bubbleDown(1)
		return retval

	def buildHeap(self, lst):
		i = len(lst) // 2
		self.currentSize = len(lst)
		self.heapList = [0] + lst[:]
		while(i > 0):
			self.bubbleDown(i)
			i -= 1


if __name__=="__main__":
	bn = minHeap()
	bn.buildHeap([9,5,6,2,3])

	print(bn.delMin())
	print(bn.delMin())
	print(bn.delMin())
	print(bn.delMin())
	print(bn.delMin())



