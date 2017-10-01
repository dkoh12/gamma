

# # run it >>> time python sample.py 1000000

# import multiprocessing
# import random
# import sys

# rangemin = 1
# rangemax = 9

# def randomGenPar_backend(backinput):
#     return random.randint(rangemin, rangemax)

# def randomeGenPar(num):
#     pool = multiprocessing.Pool()
#     return pool.map(randomGenPar_backend, range(0, num))

# randNum = int(sys.argv[1])

# random.seed(999)
# randomeGenPar(randNum)


'''
Objects are passed by reference. 
Parameter still refers to original list. any modifications will be visible to outside list
it adds foo to the list. 

However variable assignment, elems = ["bar", "baz"]
simply points the local reference elems to a new object
and has no impact on outside list
'''
def modify(elems):
	elems.append("foo")
	elems = ["bar", "baz"]

array = ["qux"]
modify(array)
print(array)


'''
[[0,1], [0,1]]

matrix contains 2 reference to same object.
so change in one row shows up in both
the solution is to append a COPY of row
'''
matrix = []
row = [0,0]
for i in range(2):
	matrix.append(row)
matrix[1][1] = 1
print(matrix)


'''
[1, 2, 4]
CLOSURE
- function that references 1 or more var in its parent's scope

child function widget reference variable values.
Even though factory has returned, widget function still holds
reference to values and can read and write to it

We say widget closes over values because it retains a reference to the values
variable


this technique is valuable because it allows function to have private state
w/o OOP

we use closures to create a generator function
'''
def factory():
	values = []
	def widget(value):
		values.append(value)
		return values
	return widget

worker = factory()
worker(1)
worker(2)
print(worker(4))

'''
this merge is used in merge sort.
This approach works for merging 2 lists.
but doesn't extend well to larger number of lists

However heap data structure is able to merge k lists in O(k log n)
'''
def merge(lst1, lst2):
	i1 = i2 = 0
	out = []
	while i1 < len(lst1) or i2 < len(lst2):
		elem1 = lst1[i1] if i1 < len(lst1) else None
		elem2 = lst2[i2] if i2 < len(lst2) else None

		if elem1 is None or (elem2 is not None and elem2 < elem1):
			out.append(elem2)
			i2 += 1
		else:
			out.append(elem1)
			i1 += 1
	return out

'''
takes a sequence of bytes and interprets them as UTF-8 encoded Unicode to 
produce string of characters


computers store all data as bytes not text. 
to interpret bytes as text (char) we rely on a mapping.
ASCII is one type of mapping. The problem w/ ASCII is that it only supports English

To solve this problem, Unicode was created. 
Unicode supports a lot more. However it takes more than 1 byte to encode each character
To make common text smaller, UTF_8 was created.

It was a way to encode Unicode chars that uses variable-width encoding scheme 
so that common English characters take less memory.

'''
b = bytearray([0xd9, 0x83, 0xd9, 0x84, 0xd8, 0xa8])
message = b.decode('utf-8')
print(message)


'''
rainbow table attacks - hacker leverage pre-computed password hashes
collision attacks - mathematics inherent in birthday problem
timing attacks on string comparison
length extension attacks on leaked state of hash function
'''
def secure_hash_comparison(user_hash, db_hash):
	if len(user_hash) != len(db_hash):
		return False
	for i in range(len(user_hash)):
		if user_hash[i] != db_hash[i]:
			return False
	return True


'''
Binary Search Trees over sorted list?

BSTs are faster for inserting and deleting items.
BSTs have O(log n) worst case time to insert or delete an item

sorted arrays take worst-case O(n) to add or remove an item

additionally B+ trees can be optimized on modern hardware, minimizing cache
misses and disk reads to increase real-world performance

'''
 

DFS, BFS, 
simulated annealing will minimize number of warps w/ high prob?
union-find alg is only approach that can handle network w/ cycles???

topological sort

BFS - shortest path in unweighted graph
dijkstras = BFS but w/ priority queue instead of queue

A* search = extension of dijkstras
also adds a heuristic that estimates how far a given node might be from depth-first


'''
Breadth-first search and depth-first search are the two most basic graph traversal algorithms. 
BFS explores nodes in expanding circles of distance from its start location, 
and thus will find the shortest path between two nodes (or star systems). 
DFS makes no such guarantee (indeed, it often finds pretty crazy, winding paths). 
One advantage of DFS, however, is that it uses much less memory. 
BFS must store a queue of nodes to visit, and this queue can grow to (order) the size of the entire graph. 
If you need to find the shortest path through a graph, but don't want to use linear memory, 
a cool algorithm is iterative deepening search. It's just like depth-first search, 
but takes a parameter that limits how deep to look. If we limit the depth to 5, say, 
it will do a depth-first exploration of all paths up to length 5. Imagine what happens, now, 
if we run the search multiple times, starting with a depth limit of 1, then 2, then 3, etc. 
Because this explores all paths of length N before it explores any of length N+1, 
it is guaranteed to find shortest paths. And because it's using depth-first traversal, it only uses O(log n) memory! 
This sounds really slow, you might think (it seems to be duplicating a lot of searching). 
However, consider the case of a roughly balanced binary tree. Half of all nodes will be found in the leaf level of the tree. 
And these nodes are only explored once. If we calculate the total number of times that nodes are traversed, 
we get N + N/2 + N/4... This sequence sums to 2N. Thus, iterative deepening search still takes linear time.

'''


'''
binary trees,

HTTP,
-> stateless protocol that serves the web.
-> uses cookie

malloc & free

Database & indexes. How are they used and how are they implemented?
-> speeds up look ups in DB
-> structure is sorted according to certain field and contains a ptr to record in DB for fast retrieval

-> w/o index, we need to do full table scan O(n)
-> w/ sorted data index, need to do binary search O(log n)

implementation
-> uses Hash-table / B+ tree for fast lookup
-> B+ tree allows for O(log n) insertion / deletion

disadv
-> needs additional space for index. Requires more time for inserting / deleting
-> data structure to remain sorted after such operations are performed
-> locks could take a long time


Security?
CSRF, XSS, local cache
CSS sprites, HTTP, Bloom Filters


System Design on building used car website / facebook
30 min to build tic-tac-toe w/ AI
30 min debugging webcrawler

'''





