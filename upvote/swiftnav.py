
#returns nth fibonacci number
def fib(n):
	if n < 1:
		return "the nth fib number must be at least 1"

	arr = [1, 0]

	for i in range(n):
		arr[i%2] = sum(arr)

	return arr[i%2]


import math

# returns whether n is prime or not
def prime(n):
	if n < 2:
		return False
	if n == 2 or n == 3:
		return True

	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
	return True

# run Fib(n) 
# For testing purposes the function had to return something that is why 
# I let it return whatever string it was supposed to print
def justOneFib(n):
	m = fib(n)
	s = ""

	if m % 5 == 0:
		# print("Fizz", end='')
		s += "Fizz"
		if m % 3 == 0:
			# print("Buzz")
			s += "Buzz"
	elif m % 3 == 0:
		# print("Buzz")
		s += "Buzz"
	else:
		isPrime = prime(m)
		# print("The %dth fibonacci value is " % n, end='')
		if isPrime:
			# print('prime')
			# print("BuzzFizz")
			s += "BuzzFizz"
		else:
			# print('not prime')
			# print("fibonacci value is: ", m)
			s += str(m)

	print(s)
	return s

# returns a range of Fib(1), Fib(2), ... Fib(n)
def multipleFib(n):

	for i in range(1, n+1):
		# print("i ", i)
		justOneFib(i)

# my own test function
def test():

	print("testing fib function")
	assert fib(0) == "the nth fib number must be at least 1"
	assert fib(5) == 5
	assert fib(50) == 12586269025
	assert fib(100) == 354224848179261915075

	print("testing prime function")
	assert prime(0) == False
	assert prime(3) == True
	assert prime(6) == False
	assert prime(fib(100)) == False


	print("testing justOneFib")
	assert justOneFib(4) == "Buzz"
	assert justOneFib(100) == "FizzBuzz"

	print("All tests passing")
	print()

# python unittest
# can add more tests like above in my test(). just shows I know how to unittest
import unittest

class SimplisticTest(unittest.TestCase):

	def test_fib_0(self):
		self.assertEqual(fib(0), "the nth fib number must be at least 1")

	def test_prime_3(self):
		self.assertTrue(prime(3))

	def test_justOneFib(self):
		self.assertEqual(justOneFib(4), "Buzz")


if __name__=="__main__":
	# test() 

	print("Running program")
	multipleFib(5)

	# print()
	# unittest.main()


