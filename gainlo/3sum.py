# http://blog.gainlo.co/

# given a sorted array find 2 numbers that sum up to S
# if sorted then takes O(N) time. 
# if not sorted takes O(N log N) time
def two_sum(arr, s):
	i = 0
	j = len(arr) - 1
	while i != j:
		if arr[i] + arr[j] > s:
			j -= 1
		elif arr[i] + arr[j] < s:
			i += 1
		else:
			return (arr[i], arr[j])

	return False

def two_sum_closest(arr, s):
	i = 0
	j = len(arr) - 1
	while i != j:
		if arr[i] + arr[j] > s:
			if j-1 == i:
				break
			j -= 1
		elif arr[i] + arr[j] < s:
			if i+1 == j:
				break
			i += 1
		else:
			return (arr[i], arr[j])

	return (arr[i] + arr[j], [arr[i], arr[j]])

#determine if 3 integers in an array sum to 0
# takes O(N^2) with O(1) space
def three_sum(arr):
	for index, i in enumerate(arr):
		temp = arr[0:index] + arr[index+1:]
		val = two_sum(temp, -i)
		if val:
			return (i, val[0], val[1])

	return False

# find 3 integers in array whose sum is closest to 0
def three_sum_closest(arr):
	d = dict()
	for index, i in enumerate(arr):
		temp = arr[0:index] + arr[index+1:]
		val, nums = two_sum_closest(temp, -i)
		nums.append(i)
		d[val+i] = nums

	return min([(abs(i), j) for i, j in d.items()])


# determine if 3 integers in an array sum to 0. integers can be used multiple times
def three_sum_multiple(arr):
	for i in arr:
		if i == 0:
			return (0, 0, 0)
		val = two_sum(arr, -i)
		if val:
			return (i, val[0], val[1])
	return False

def test():
	r2 = [1, 8, -6, 4, -10, -1, -17]
	r2.sort()
	arr = [4, 3, -1, 2, -2, 10]
	arr.sort()

	assert two_sum(arr, 5) == (2, 3)
	assert three_sum(arr) == (-2, -1, 3)
	assert three_sum_multiple(arr) == (-2, -2, 4)
	assert three_sum_closest(r2) == (1, [-6, -1, 8])

	print("All tests passing")

if __name__=="__main__":
	test()