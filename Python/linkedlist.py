def provided_ll():
	from collections import deque

	d = deque([1, 2, 3, 4])
	print(d)

	print(d.pop(), d)
	d.append(5)


class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

	def __str__(self):
		return 'Node ['+str(self.data)+']'


# remove nodes in linked list where value > x

"""
while list != None and list.val > x:
	list = list.next

if list == None:
	return None

head = list

while head.next != None:
	while head.next.val > x:
		head.next = head.next.next

		if head == None or head.next == None:
			break

	if head.next == None:
		break

	head = head.next

return list

"""


# In C  (reverse linked list)

# struct node *prev = NULL;
# struct node *curr = *head;
# struct node *next;
# while (current) {
# 	next = curr->next;
# 	curr->next = prev;
# 	prev = curr;
# 	curr = next;
# }
# head = prev;

class linkedlist:
	def __init__(self, head=None):
		self.head = head
		self.size = 0

	def insert(self, data):
		if self.head == None:
			self.head = node(data)
		else:
			head = self.head
			while head.next:
				head = head.next
			head.next = node(data)
		self.size += 1

	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def addToHead(self, data):
		n = node(data)
		n.next = self.head
		self.head = n
		self.size += 1

	def delete(self):
		head = self.head
		self.head = self.head.next
		head.next = None
		print("deleted " + str(head))

	def __str__(self):
		if self.head != None:
			head = self.head
			out = 'LinkedList [' + str(head.data)
			while head.next:
				head = head.next
				out += ' ' + str(head.data)
			return out + ']'
		return 'LinkedList []'

	def clear(self):
		self.__init__()




if __name__=="__main__":
	L = linkedlist()
	L.insert(3)
	L.insert(4)
	L.insert(5)
	print(L)

	L.addToHead(-1)
	print(L)

	L.delete()
	print(L)

	L.reverse()
	print(L)

	L.clear()
	print(L)



