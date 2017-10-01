def binarySearch(lst, value, low, high):

	if low > high:
		return -1
	mid = (low + high) // 2
	if lst[mid] == value:
		return mid
	elif lst[mid] < value:
		return binarySearch(lst, value, mid+1, high)
	else:
		return binarySearch(lst, value, low, mid)

def selectionSort(lst):
	for i in range(len(lst)):
		small = i 
		for j in range(i+1, len(lst)):
			if lst[j] < lst[small]:
				small = j

		lst[i], lst[small] = lst[small], lst[i]

	return lst

def insertionSort(lst):
	for i in range(1, len(lst)):
		j = i-1
		while(j >= 0 and lst[j] > lst[i]):
			lst[i], lst[j] = lst[j], lst[i]
			j-=1

	return lst



def bubbleSort(lst):
	for i in range(len(lst)):
		for j in range(1, len(lst)):
			if lst[j-1] > lst[j]:
				lst[j-1], lst[j] = lst[j], lst[j-1]
	return lst


'''
merge() works for merging 2 list
but a heap data structure is able to merge k lists in O(k log n)

'''
def mergeSort(lst):
	if len(lst) <= 1:
		return lst
	mid = len(lst)//2
	left = lst[:mid]
	right = lst[mid:]

	mergeSort(left)
	mergeSort(right)

	i, j, k = 0, 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			lst[k] = left[i]
			i+=1
		else:
			lst[k] = right[j]
			j+=1
		k+=1

	while i < len(left):
		lst[k] = left[i]
		i+=1
		k+=1

	while j < len(right):
		lst[k] = right[j]
		j+=1
		k+=1

	return lst

def quickSort(lst):
	if len(lst) <= 1:
		return lst
	left = []
	equal = []
	right = []
	pivot = lst[0]

	for val in lst:
		if val < pivot:
			left.append(val)
		elif val == pivot:
			equal.append(val)
		else:
			right.append(val)
	return quickSort(left) + equal + quickSort(right)

def quicksort2(lst):
	if not lst:
		return []

	pivots = [x for x in lst if x == lst[0]]
	left = quicksort2([x for x in lst if x < lst[0]])
	right = quicksort2([x for x in lst if x > lst[0]])

	return left+pivots+right


'''
Given a nearly sorted list find k largest integers

http://www.geeksforgeeks.org/nearly-sorted-algorithm/

Put k elements in min heap. Then for rest of elements you traverse heap
O(k) + O((n-k)log k)


'''
import heapq

def k_largest(lst, k):
	print(lst)

	# One line 
	# print(heapq.nlargest(k, lst))
	
	# Same thing but multiple lines
	# heap = []

	# for i in lst:
	# 	if len(heap) < k:
	# 		heapq.heappush(heap, i)
	# 	else:
	# 		if i > heap[0]:
	# 			heapq.heappop(heap)
	# 			heapq.heappush(heap, i)

	# arr = []
	# while len(heap) > 0:
	# 	arr.append(heapq.heappop(heap))

	# print(arr)

	# done using insertion sort
	arr = insertionSort(lst)
	print(arr[len(arr)-k:])



if __name__=="__main__":
	# lst = [5, 7, 3, 8, 4, 2]
	# print(insertionSort(lst))
	# print(bubbleSort(lst))
	# print(mergeSort(lst))
	# print(quickSort(lst))
	# print(quicksort2(lst))

	lst = [1, 3, 5, 8, 2, 10, 4, 12, 16]
	k_largest(lst, 3)


