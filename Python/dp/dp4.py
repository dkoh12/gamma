'''
/**
 *
 * Only for DP practice. Once you have practiced, delete the solution 
 * and paste it to one of dp1, 2, 3.
 *
 */
'''

from pprint import pprint


def foo(s, width):
	n = len(s)
	# arr = [[0]*n for i in range(n)]

	left = []
	right = []

	i =0 
	while i < len(s):
		window = s[i:width]

		res = []
		for i in window:
			if not res:
				res.append(i)
			if res[-1] > i:
				res.append(i)
			else:
				res.append(res[-1])
		left.extend(res)

	mmin = []
	for i in range(n-w+1):
		mmin.append(min(left[i+width-1], right[i]))

	return mmin



	# return s[start:mmax]

def X(lst):
	total, currmax = 0
	start, end, s = 0,0,0

	for i in range(len(lst)):
		total += lst[i]
		if total < 0:
			total = 0
			s = i+1

		elif total > currmax:
			currmax = total
			start = s
			end = i

	return arr[start:end+1]



def histogram(lst):
	




def main():
	arr = [3, 7, 4, 2, 7, 2, 4, 8, 1, 9, 13, 5]
	print(lis(arr))


main()