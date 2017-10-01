# 5.1
def MinN(M, N, i, j):
	M = int(M, 2)
	N = int(N, 2)
	# print(M, bin(M), N, bin(N))
	# print(i, j)

	count = i

	while M > 0:
		bit = M & 1
		N = (bit << count) | N
		M = M >> 1
		count += 1
		# print("M", M, bin(M))
		# print("N", N, bin(N))

	return bin(N)

# 5.6
def conversion(a, b):
	count = 0
	num = a ^ b

	while num > 0:
		if (num & 1) == 1:
			count +=1
		num = num >> 1

	return count

# 5.4 very hacky
def pair(num):
	if num == 1:
		return (1, 1)

	n = num
	count = 0
	large = 0
	small = 0

	while len(bin(n))-2 > 0:
		bit = n & 1

		if bit == 1:
			large = (num & ~(1 << count)) | (1 << (count+1))
			small = (num & ~(1 << count)) | (1 << (count-1))

			# small = ~(num ^ (-1 << count))
			return (small, large)

		count += 1
		n = n >> 1


"""
5L and 3L cups. Make exactly 4L

fill up 5L and pour into 3L 
>> 2L and 3L

throw out the 2L away   or     throw out 3L away
>> 0L and 3L                    0L   and  2L

pour 3L into 5L        or      pour 2L into 3L cup
>> 3L and 0L                    2L   and   0L

fill up 3L           or       fill up 5L cup
>> 3L and 3L                    2L   and  5L

pour 3L into 5L      or       fill up 3L cup
>> 5L and 1L                    3L  and  4L

throw away 5L       
>> 0L and 1L

pour 1L into 5L
>> 1L and 0L

fill up 3L
>> 1L and 3L

pour 3L into 5L and get 4L
>> 4L and 0L

"""




if __name__=="__main__":
	N = "10000000000"
	M = "10011"
	i = 2
	j = 6
	print(MinN(M, N, i, j))


	a = 29
	b = 15
	print(conversion(a, b))


	print(pair(10))

