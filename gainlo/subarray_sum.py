
# GOOGLE interview Q
# given unsorted array of nonnegative integers find continuous subarray 
# that sums to a given number
def subarray_cont(lst, s):
	total = 0
	index = 0

	for i in lst:
		
		if total == s:
			return arr
		if total < s:
			total += i
			arr.append(i)
		if total > s:
			total -= i
			arr = arr[1:]

# def subarray_sum(lst, s):
# 	arr = []




def test():
	print("Hi")
	arr = [4, 3, 7, 2, 9]
	s = 6

	r1 = [1, 4, 20, 3, 10, 5]
	print(subarray_cont(r1, 33))

	r2 = [1, 4, 0, 0, 3, 10, 5]
	print(subarray_cont(r2, 7))

	r3 = [1, 4]
	print(subarray_cont(r3, 0))

	# print(subarray_sum(arr, s))

if __name__=="__main__":
	test()