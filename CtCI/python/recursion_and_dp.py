# count number of ways child runs up n stairs. 
# can take either 1 step, 2 step, or 3 steps

# f(100) = f(99) + f(98) + f(97)
def stairs(n):
	arr = [0, 0, 1]

	for i in range(n):
		arr[i%3] = sum(arr)

	return arr[i%3]


import itertools

def subset(lst):
	return itertools.chain.from_iterable(itertools.combinations(lst, n) for n in range(len(lst)+1))

def magic_index(lst, left, right):
	mid = (left + right)//2

	if lst[mid] == mid:
		return mid
	elif lst[mid] < mid:
		return magic_index(lst, mid+1, right)
	else:
		return magic_index(lst, left, mid)

def multiply(a, b):
	if a == 0 | b == 0:
		return 0
	elif a == 1:
		return b
	elif b == 1:
		return a

	m = min(a, b)
	if m == b:
		return a + multiply(a, b-1)
	else:
		return a + multiply(b, a-1)

def permutations(s):
	# return list(itertools.chain.from_iterable(itertools.combinations(s, i) for i in range(len(s)+1)))

	lst = list(itertools.permutations(s, len(s)))
	return [''.join(i) for i in lst]


def change(c):
	change = {25: 12, 10: 3, 5: 2, 1: 1}

	# c = n - n%5 # leave out the extra pennies

	q = c // 25 # quarters
	c -= 25 * q

	print("c", c)

	d = c // 10
	c -= 10 * d # dimes

	print("c", c)

	n = c // 5 # nickels
	c -= 5 * n

	print(q, d, n)

	return 12 * q + 3 * d + 2 * n


if __name__=="__main__":
	print(stairs(4))

	lst = {'a', 'b', 'c'}
	print(list(subset(lst)))

	arr = [-1, 0, 1, 2, 4, 7, 9, 10]
	r2 = [-1, 0, 1, 2, 3, 4, 6, 10]
	r3 = [0, 2, 3, 4, 6, 10]
	print(magic_index(arr, 0, len(arr)-1))
	print(magic_index(r2, 0, len(r2)-1))
	print(magic_index(r3, 0, len(r3)-1))

	s = 'Disney'
	# print(permutations(s))

	print(change(99))

