class minHeap():
	def __init__(self):
		self.heapList = [0]
		self.size = 0

	def bubbleUp(self, i):
		while i//2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
			i = i//2

	def insert(self, k):
		self.size += 1
		self.heapList.append(k)
		self.bubbleUp(self.size)

	def bubbleDown(self, i):
		while i*2 <= self.size:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
			i = mc

	# returns index
	def minChild(self, i):
		if i*2+1 > self.size:
			return i*2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i*2
			else:
				return i*2+1

	def delMin(self):
		self.size -= 1
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.size]
		self.heapList.pop()
		self.bubbleDown(1)
		return retval

	def getMin(self):
		return self.heapList[1]

	def buildHeap(self, lst):
		i = len(lst)//2
		self.size = len(lst)
		self.heapList += lst[:]
		while i > 0:
			self.bubbleDown(i)
			i -= 1


class MaxHeap():
	def __init__(self):
		self.size = 0
		self.heapList = [0]

	def bubbleUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] > self.heapList[i//2]:
				self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
			i /= 2

	def insert(self, k):
		self.size += 1
		self.heapList.append(k)
		self.bubbleUp(self.size)

	def bubbleDown(self, i):
		while i * 2 <= self.size:
			mc = self.maxChild(i)
			if self.heapList[i] < self.heapList[mc]:
				self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
			i = mc

	def maxChild(self, i):
		if i*2+1 > self.size:
			return i*2
		else:
			if self.heapList[i*2] > self.heapList[i*2+1]:
				return i*2
			else:
				return i*2+1

	def delMax(self):
		self.size -= 1
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.size]
		self.heapList.pop()
		self.bubbleDown(1)
		return retval

	def getMax(self):
		return self.heapList[1]

	def buildHeap(self, lst):
		i = len(lst) // 2
		self.size = len(lst)
		self.heapList += lst[:]
		while i > 0:
			self.bubbleDown(i)
			i -= 1


if __name__=="__main__":
	mmin = minHeap()
	mmin.buildHeap([6, 8, 9, 35])

	mmax = MaxHeap()
	mmax.buildHeap([0, 5, 2, 7])

	tot = mmax.getMax() + mmin.getMin()
	print(tot/2)



