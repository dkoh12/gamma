
# what find_non_decreasing and find_non_increasing is doing is I create a separate 
# array equal to the length of my window. Then for each index I see if the next pointer is 
# bigger/smaller depending on which function than my current pointer. If it satisfies that condition
# I add 1 to the start index of my list. 

# so at the end what I get is a list where each index has a value corresponding to number of valid
# subranges created with that index as the start. I sum them up to get total non_decreasing /increasing
# subranges

# yes I could have used a counter instead of a list to return a number. But a list made it easier to debug.

def find_non_decreasing(window):
	lst = [0] * len(window)

	for start in range(len(window)):
		temp = start
		for curr in range(start+1, len(window)):
			if window[curr] >= window[temp]:
				temp = curr
				lst[start] += 1
			else:
				break

	return sum(lst)


def find_non_increasing(window):
	lst = [0] * len(window)

	for start in range(len(window)):
		temp = start
		for curr in range(start+1, len(window)):
			if window[curr] <= window[temp]:
				temp = curr
				lst[start] += 1
			else:
				break

	return sum(lst)

def window_output(window):
	dec = find_non_decreasing(window)
	inc = find_non_increasing(window)
	print(dec - inc)


from collections import deque

def main():
	# N, K = map(int, "5 3".split())
	# lst = list(map(int, "1 2 3 1 1".split()))

	N, K = map(int, input().split())
	lst = list(map(int, input().split()))

	window = deque()

	for i in range(K):
		window.append(lst[i])
	window_output(window)

	for i in range(K, len(lst)):
		window.append(lst[i])
		window.popleft()
		window_output(window)


def test():
	lst = [1, 2, 3, 1, 1]
	window1 = [1, 2, 3]
	window2 = [2, 3, 1]
	window3 = [3, 1, 1]

	assert find_non_decreasing(window1) == 3
	assert find_non_increasing(window1) == 0

	assert find_non_decreasing(window2) == 1
	assert find_non_increasing(window2) == 1

	assert find_non_decreasing(window3) == 1
	assert find_non_increasing(window3) == 3


	window = [2, 4, 11, 13, 3, 5, 5, 6, 3, 3, 2, 4, 2, 14, 15]

	assert find_non_decreasing(window) == 17
	assert find_non_increasing(window) == 9


	print("All tests passing")


if __name__=="__main__":
	# test()
	main()



