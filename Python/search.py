def binary_search(lo, hi, p, item):
	if lo == hi:
		return lo
	elif lo > hi:
		return -1

	mid = (lo + hi) // 2
	if p[mid] == item:
		return mid
	else:
		if p[mid] > item:
			return binary_search(lo, mid, p, item)
		else:
			return binary_search(mid+1, hi, p, item)


def MergeList(A, B):
	for j in B:
		for i in range(len(A)):
			if A[i] == None:
				A[i] = j
				break
			if A[i] > j:
				temp = A[i]
				A[i] = j
				j = temp

	print(A, B)
	return A, B



# http://www.geeksforgeeks.org/the-stock-span-problem/
# Given a list like [10,30,60, 55, 50, 10, 40, 54, 60, 90]
# return [1, 2, 3, 1, 1, 1, 2, 4, 9, 10]

# Stock Span problem. also in DP
def reading(lst):
	values = []
	stack = []
	val_arr = []

	for i in lst:
		if len(stack) == 0:
			stack.append(i)
			val_arr.append(1)
			values.append(1)
			continue

		count = 1
		while len(stack) != 0 and i >= stack[-1]:
			stack.pop()
			v = val_arr.pop()
			count += v

		stack.append(i)
		val_arr.append(count)
		values.append(count)

		if i < stack[-1]:
			stack.append(i)
			val_arr.append(1)
			values.append(1)


	return values



if __name__=="__main__":
	lst = [0, 5, 13, 19, 22, 41, 55, 68, 72, 81, 98]

	# print(binary_search(0, len(lst)-1, lst, 72))


	A = [1, 3, 5, 7, 9, None, None, None, None, None]
	B = [1, 2, 4, 8, 15]

	A, B = MergeList(A, B)
	# print(A)
	# print(B)
	
	arr = [10,30,60, 55, 50, 10, 40, 54, 60, 90]
	print(reading(arr))





