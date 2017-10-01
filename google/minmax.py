def maxsearch(lst):
	mid = int(len(lst)/2)
	#print(mid, lst[mid], lst)
	if len(lst) == 2:
		return max(lst)
	if lst[mid] > lst[mid-1] and lst[mid] > lst[mid+1]:
		return lst[mid]
	#ascending
	elif lst[mid] > lst[mid-1] and lst[mid] < lst[mid+1]:
		return maxsearch(lst[mid:])
	#descending
	elif lst[mid] < lst[mid-1] and lst[mid] > lst[mid+1]:
		return maxsearch(lst[:mid])

#given list with ascending section and descending section, find min and max
def minmax(lst):
	mmin = lst[0]
	mmax = maxsearch(lst)
	return (mmin, mmax)

# DP longest subsequence problem
# abs(A[i]-A[j]) cannot be greater than abs(i-j)
def num_elem_rule(lst):
	#indexlst = [(e, i) for i, e in enumerate(lst)]
	#indexlst.sort()
	#for e,i in indexlst:

	A = set()
	for i in range(len(lst)):
		for j in range(len(lst)):
			if i != j:
				if not (abs(lst[i]-lst[j]) > abs(i-j)):
					A.add(lst[i])
					A.add(lst[j])
	return len(A)


if __name__=="__main__":
	lst = [2,3,4,5,6,7,10,9,8,7]
	print(minmax(lst))

	newlst = [13,5,4]
	print(num_elem_rule(newlst))