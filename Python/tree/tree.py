
# def maxDuplicateSubtree(root, path, maxsubtree):
# 	if (root is None):
# 		return 0
# 	left = []
# 	right = []
	
# 	maxDuplicateSubtree(root.left, left)
# 	maxDuplicateSubtree(root.right, right)

# 	if (left == right):
# 		resultNode = root

# 	path.append(left)
# 	path.append(right)

# 	path.append(root.val)

#   1
#   /\
#  2  3
# /\
# 4 5 

# preorder (root left right): 1 2 4 5 3
# inorder (left, root, right): 4 2 5 1 3
# postorder (left right root): 4 5 2 3 1
def preorder(root):
	print(root.val)
	preorder(root.left)
	preorder(root.right)

def bst(lst, val, low, high):
	mid = (low+high)//2
	# print("mid", mid)

	# print("low", low, "high", high)
	# print("val", val, "lst[mid]", lst[mid], "mid", mid)

	if low > high:
		return -1
	if lst[mid] == val:
		return mid
	elif lst[mid] > val:
		return bst(lst, val, low, mid)
	else:
		return bst(lst, val, mid+1, high)

def quicksort(lst):
	if lst == []:
		return []

	pivots = [x for x in lst if x == lst[0]]
	left = quicksort([x for x in lst if x < lst[0]])
	right = quicksort([x for x in lst if x > lst[0]])

	return left+pivots+right


def get_hotels(scores, avg_min_score):
	d = {}
	for i in scores:
		if i['hotel_id'] not in d:
			d[i['hotel_id']] = (i['score'], 1)
		else:
			left = d[i['hotel_id']][0] + i['score']
			right = 1+d[i['hotel_id']][1]
			d[i['hotel_id']] = (left, right)

	# dic with key has avg score and value as hotel_id
	dd = {}
	for i, j in d.items():
		val = j[0] / j[1]
		dd[val] = i

	print(dd)
	lst = list(dd.keys())
	# lst.sort()

	lst = quicksort(lst)
	index = bst(lst, avg_min_score, 0, len(lst)-1)

	# print("index", index, "lst[index]", lst[index])

	output = []
	# for i in lst:
	# 	if i >= avg_min_score:
	# 		output.append(dd[i])

	for i in range(index, len(lst)):
		output.append(dd[lst[i]])

	return output



if __name__=='__main__':

	scores = [
		{'hotel_id': 1001, 'score':7},
		{'hotel_id': 1001, 'score':7},
		{'hotel_id': 1001, 'score':7},
		{'hotel_id': 2001, 'score':10},
		{'hotel_id': 3001, 'score':5},
		{'hotel_id': 2001, 'score':5}
		]

	print(get_hotels(scores, 5))
