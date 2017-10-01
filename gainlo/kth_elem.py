
def second_highest(lst):
	high1 = -1
	high2 = -1
	for i in lst:
		if i > high1:
			high2 = high1
			high1 = i
		elif i > high2:
			high2 = i

	return high2

