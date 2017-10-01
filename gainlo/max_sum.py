
# max sum of non-adjacent elements
def max_sum(lst):
	if len(lst) == 0:
		return 0

	return max(lst[0] + max_sum(lst[2:]), max_sum(lst[1:]))

# Memoized O(N) time. O(N) space
mem = [None] * 5
def max_sum_mem(lst, i):
	global mem
	if i == 0:
		return lst[0]
	if i == 1:
		return max(lst[0], lst[1])
	if mem[i]:
		return mem[i]
	mem[i] =  max(max_sum_mem(lst, i-1), max_sum_mem(lst, i-2) + lst[i])
	return mem[i]


def test():
	arr = [1, 0, 3, 9, 2]

	assert max_sum(arr) == 10
	assert max_sum_mem(arr, len(arr)-1) == 10

	print("All tests passed")


if __name__=="__main__":
	test()
