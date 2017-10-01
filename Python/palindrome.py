#dynamic programmin - longest palindrome subsequence

# O(n^2)
def palindrome_subsequence(arr, i, j):
	"""
	def palindrom_subsequence("BBABCBCAB"):
		return 7 (BABCBAB)
	"""
	if i == j:
		return 1
	if arr[i] != arr[j]:
		return max(palindrome_subsequence(arr, i+1, j), palindrome_subsequence(arr, i, j-1))
	else:
		if j == i + 1:
			return 2
		else:
			return palindrome_subsequence(arr, i+1, j-1) + 2


# O(n^2 * m)
def longest_common_substr(A, B):
	"""
	8 <- "tutorial"
	"""
	if len(A) == 0 or len(B) ==0:
		return 0
	if A == B:
		return len(A)
	if len(A) < len(B):
		return max(longest_common_substr(A, B[1:]), longest_common_substr(A, B[:-1])) 
	else:
		return max(longest_common_substr(A[1:], B), longest_common_substr(A[:-1], B)) 


def power(x,y):
	if y == 1:
		return x
	if y / 2 > 1:
		return power(x, y/2) * power(x, y/2)
	else:
		return power(x, y-1) * x

# return longest palindrome by removing or shuffling characters
from collections import Counter
def longest_palindrome(s):
	c = Counter(s)

	evens = [(i, j) for i, j in c.items() if j%2 == 0]

	odds = [(i, j) for i,j in c.items() if j % 2 == 1]
	max_odd = max(odds)
	# print("max odd", max_odd)

	remove_all_odd = [(i,j-1) for (i,j) in odds if (i,j) != max_odd and j != 1]
	# print("remove all odd", remove_all_odd)

	evens.extend(remove_all_odd)

	left = []
	for i, j in evens:
		j//=2
		left += i*j

	right = left[::-1]
	lst = left + [max_odd[0] * max_odd[1]] + right

	s = ''.join(lst)

	return s



if __name__=='__main__':
	s = "BBABCBCAB"
	print(palindrome_subsequence(s, 0, len(s)-1))


	A = "tutorialhorizon";
	B = "dynamictutorialProgramming"
	#print(longest_common_substr(A, B))

	arr = [1,12,7,0,23,11,52,31,61,69,70,2]
	# print(longest_increasing_subseq(arr, 0, len(arr)-1))

	print(power(3,4))

	s1 = 'aha'
	s2 = 'ttaatta'
	s3 = 'abc'
	s4 = 'gggaaa'
	print(longest_palindrome(s1))
	print(longest_palindrome(s2))
	print(longest_palindrome(s3))
	print(longest_palindrome(s4))



