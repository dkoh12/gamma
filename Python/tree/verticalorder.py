



class Node:
	def __init__(self, key):
		self.key = key
		self.right = None
		self.left = None


def getVerticalOrder(root, hd, d):
	if root is None:
		return None

	if hd in d:
		d[hd].append(root.key)
	else:
		d[hd] = [root.key]

	getVerticalOrder(root.left, hd-1, d)
	getVerticalOrder(root.right, hd+1, d)


def printVerticalOrder(root):
	d = {}

	if root is None:
		return None


	getVerticalOrder(root, 0, d)

	for i in sorted(d): # sorts by key
		for j in d[i]:
			print(j, end=' ')
		print()



def executeVerticalOrder():
	root = Node(1);
	root.left = Node(2);
	root.right = Node(3);
	root.left.left = Node(4);
	root.left.right = Node(5);
	root.right.left = Node(6);
	root.right.right = Node(7);
	root.right.left.right = Node(8);
	root.right.right.right = Node(9);
	print("Vertical order traversal is")
	printVerticalOrder(root)


if __name__=="__main__":
	executeVerticalOrder()


