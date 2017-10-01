
from pprint import pprint


digit_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


from itertools import product

#run time is O(4^n) that is upperbound where every digit is 7 or 9.

def out(number):
	num = str(number)
	result = ['']

	for i in num:
		if i in digit_map:
			s = digit_map[i]

			newarr = []
			for y in s:
				for x in result:
					newarr.append(x+y)

			result = newarr

			# result = [x + y for x in result for y in s]

	return result

def boss(number):
	num = str(number)
	result = ['']

	for i in num:
		if i in digit_map:
			s = digit_map[i]
			result = [x + y for x in result for y in s]

	return result


def poss(number):
	letters = (digit_map[i] for i in number)

	for groups in product(*letters):
		yield ''.join(groups)


def combo(num):
	if len(num) == 1:
		return list(digit_map[num])
	else:
		result = combo(num[:-1])

	return [(one + two) for one in result for two in digit_map[num[-1]]]



def hand(number):
	num = str(number)
	result = ['']
	for i in num:
		if i in digit_map:
			s = digit_map[i]
			
			newarr = []
			for y in s:
				for x in result:
					newarr.append(x+y)
			result = new arr

			# result = [x+y for x in result for y in s]

	return result

def subsetSum(lst, val):
	arr = [[False] * (val+1) for i in range(len(lst))]

	for i in range(len(lst)):
		arr[i][0] = True
		arr[i][lst[i]] = True

	for i in range(1, len(lst)):
		for j in range(1, val+1):
			if lst[i] > j:
				arr[i][j] = arr[i-1][j]
			else:
				arr[i][j] = arr[i-1][j] or arr[i][j-lst[i]]


	i = len(lst)-1
	j = val
	set = []
	while i > 0 and j >0:
		if arr[i][j]:
			if not arr[i-1][j]:
				j-=lst[i]
				set.append(lst[i])
			i-=1
		else:
			break

	if arr[i][j] and i == 0:
		set.append(lst[i])

	return set


def main():
	# print(out(123))
	# print(boss(123))
	# print(list(poss("2345")))
	# print(combo('345'))
	
	arr = [3, 5, 7, 8, 10]
	total = 16
	print(subsetSum(arr, total))

main()