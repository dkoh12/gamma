# https://www.careercup.com/question?id=5715287577985024

def dummy(str):
	lst = str.split("#")
	tmp = ''.join(lst)
	if len(tmp) != len(lst):
		return "invalid"

	# triangle series : (n+1) choose 2

	count = 0
	level = 1
	level_arr = []
	total = 0
	for i in lst:
		if count < level:
			count += 1
			level_arr.append(i)
		if count == level:
			total += max(list(map(int, level_arr)))
			level_arr = []
			level += 1
			count = 0

	if count != 0:
		return "invalid"

	return total

# https://www.careercup.com/question?id=5765503882625024
# UINT16 withdrawAll() {
# 	UINT16 money, all;

# 	money = MAX_UNIT16;
# 	all = 0;
# 	while (money) {
# 		if (withdraw(money) == 0) {
# 			money /= 2;
# 		} else {
# 			all += money;
# 		}
# 	}
# 	return all;
# }

# Tarjan's SCC
# http://code.activestate.com/recipes/578507-strongly-connected-components-of-a-directed-graph/
vertices = [1,2,3,4,5,6,7,8]
edges = {1:[2], 2:[3, 8], 3:[4, 7], 4:[5], 5:[3,6], 6:[], 7:[4,6], 8:[1,7]}

def strongly_connected_components(vertices, edges):
	identified = set()
	stack = []
	index = {}
	lowlink = {}

	def dfs(v):
		index[v] = len(stack)
		stack.append(v)
		lowlink[v] = index[v]

		for w in edges[v]:
			if w not in index:
				yield from dfs(w)
				lowlink[v] = min(lowlink[v], lowlink[w])
			elif w not in identified:
				lowlink[v] = min(lowlink[v], lowlink[w])

		if lowlink[v] == index[v]:
			scc = set(stack[index[v]:])
			del stack[index[v]:]
			identified.update(scc)
			yield scc

	for v in vertices:
		if v not in index:
			yield from dfs(v)




if __name__=="__main__":
	a = "5#9#6#4#6#8#0#7#1#5"
	b = "5#9#6#4#6#8#0#7#1"
	c = "5#9##4#6#8#0#7#1"

	#print(dummy(a))
	#print(dummy(b))
	#print(dummy(c))

	lst = list(strongly_connected_components(vertices, edges))
	print(lst)

