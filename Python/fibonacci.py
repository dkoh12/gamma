'''
/*=================================
=            fibonacci            =
=================================*/

Numbers without consecutive 1s in binary representation is also a fibonacci sequence


that is n = length of binary str
n=1 -> 2 (0, 1)
n=2 -> 3 (00, 01, 10)
n=3 -> 5 (000, 001, 010, 100, 101)
n=4 -> 8 
'''

def fib(n):
	if n == 1 or n == 2:
		return 1

	return fib(n-1) + fib(n-2)


def fib2(n):
	# [1, 0] will be equal to fib(n)
	# [0, 1] will return 1 higher fibonacci number

	position = [1, 0]

	for i in range(n):
		position[i%2] = sum(position)

	return position[i%2]


'''
/*==============================
=            stairs            =
==============================*/
you can take 1, 2, or 3 steps at a time.
In how many different ways can you get across n tiles ?


stairs problem is also a fibonacci problem

# of ways to reach N = 
# of ways to reach N-1 +
# of ways to reach N-2 +
# of ways to reach N-3 +

'''
def stairs(n):

	position = [0,0,1]
	for i in range(n):
		position[i%3] = sum(position)
		print(position)

	return position[i%3]


#/*=====  End of stairs  ======*/


#/*=====  End of fibonacci  ======*/


'''
/*=====================================================
=            Number of ways to make Change            =
=====================================================*/
number of different ways to make change: n given list of coins: coins
coins can be used repeatedly
'''

def make_change(coins, n):
	arr = [0] * (n+1)
	arr[0] = 1

	for i in coins:
		print("coin: ", i)
		for j in range(i, n+1):
			arr[j] += arr[j-i]
		print(arr)


	return arr[n]


#/*=====  End of Number of ways to make Change  ======*/



def test():
	assert fib(5) == 5
	assert fib(8) == 21

	assert fib2(5) == 5
	assert fib2(8) == 21

	assert stairs(4) == 7

	# n = 10
	# coins = [2, 5, 3, 6]
	# assert make_change(coins, n) == 5

	assert make_change([1, 5, 10, 25], 25) == 13

	print("passing all tests")

if __name__=="__main__":
	test()

