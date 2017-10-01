# 4.5
def checkBST(root):
	return checkBST(root, -float("inf"), float("inf"))


def checkBST(root, mmin, mmax):
	if root == None:
		return True
	elif mmin > mmax:
		return False
	elif mmin > root or root > mmax:
		return False
	return checkBST(root.left, mmin, root.data) and checkBST(root.right, root.data, mmax)




# 4.8
# O(log n)
def isDescendant(node, p): 
	if node == None:
		return False
	if node == p:
		return True
	return isDescendant(node.left, p) or isDescendant(node.right, p)

# at most recurses O(log n). but each times calls isDescendant 2x for O(log n * log n)
def commonAncestor(node, p, q):
	if node.left == None and node.right == None: #1 node tree
		return False
	if isDescendant(node.left, p) and isDescendant(node.left, q):
		return commonAncestor(node.left, p, q)
	elif isDescendant(node.right, p) and isDescendant(node.right, q):
		return commonAncestor(node.right, p, q)		
	else:
		return node




if __name__=="__main__":
	pass

