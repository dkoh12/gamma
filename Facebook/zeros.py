
def zero(lst):
	# filters disappear after 1 use
	# zero = filter(lambda x: x == 0, lst)
	# z = list(zero)
	# nonzero = filter(lambda x: x!=0, lst)
	# n = list(nonzero)

	zero = [i for i in lst if i == 0]
	nonzero = [i for i in lst if i!= 0]

	return nonzero + zero


def test():
	lst = [1,2,3,8,0,2,2,0,10]

	assert zero(lst) == [1,2,3,8,2,2,10,0,0]

	print("All tests passing")

if __name__=="__main__":
	test()
	



