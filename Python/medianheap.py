import queue
import sys

class MedianHeap:
	def __init__(self, numbers=None):
		self.median = None
		self.left = queue.PriorityQueue() #max-heap
		self.right = queue.PriorityQueue() #min-heap
		self.diff = 0 #difference in their sizes

		if numbers:
			for n in numbers:
				self.put(n)

	def top(self):
		return self.median

	def put(self, n):
		if not self.median:
			self.median = n
		elif n <= self.median:
			self.left.put(-n)
			self.diff += 1
		else:
			self.right.put(n)
			self.diff -= 1

		if self.diff > 1:
			self.right.put(self.median)
			self.median = -self.left.get()
			self.diff = 0
		elif self.diff < -1:
			self.left.put(-self.median)
			self.median = self.right.get()
			self.diff = 0

	def get(self):
		median = self.median

		if self.diff > 0:
			self.median = -self.left.get()
			self.diff -= 1
		elif self.diff < 0:
			self.median = self.right.get()
			self.diff += 1
		elif not self.left.empty():
			self.median = -self.left.get()
			self.diff -= 1
		elif not self.right.empty():
			self.median = self.right.get()
			self.diff += 1
		else: #median was only element
			self.median = None

		return median



if __name__=="__main__":
	numbers = map(int, [1,2,3,4,5])
	m = MedianHeap(numbers)
	print("Median is ", m.get())
