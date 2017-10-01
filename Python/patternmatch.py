"""
Aho-Corasick Algorithm (formed basis for fgrep)
>>   http://www.geeksforgeeks.org/aho-corasick-algorithm-pattern-searching/

input:
text = "ahishers"
arr[] = {"he", "she", "hers", "his"}

output:
word his appears from 1 to 3
word he appears from 4 to 5
word she appears from 3 to 5
word hers appears from 4 to 7

n = len of text
m = total number of char of all words in arr. (m = arr[0] + arr[1] + ... + arr[n])
k = number of words in arr

linear search alg like KMP takes O(n*k + m)

Aho-Corasick finds it in O(n+m+z) where z = total number of occurances of words in text

"""
import pprint

'''
/*====================================
=            Python Tries            =
====================================*/
'''
# https://reterwebber.wordpress.com/2014/01/22/data-structure-in-python-trie/
def make_trie(*words):
	print(*words)

	root = dict()

	for word in words:
		if type(word) != str:
			raise TypeError("Trie only works on strings")

		current_dict = root 
		for letter in word:
			current_dict = current_dict.setdefault(letter, {}) # if key found, return value, else return default value
		current_dict = current_dict.setdefault('_end_', '_end_')
	
	return root


def in_trie(trie, word):
	if type(word) != str:
		raise TypeError("Trie only works on strings")

	current_dict = trie
	for letter in word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return False
	
	return True

def remove_from_trie(trie, word, depth):
	if word and word[depth] not in trie:
		return False

	if len(word) == depth +1:
		del trie[word[depth]]
		if not trie: # node becomes leaf, indicates its parent
			return True
		return False
	else:
		current_dict = trie

		# recursively climb up to delete
		if remove_from_trie(current_dict[word[depth]], word, depth+1):
			if current_dict:
				del current_dict[word[depth]]
			return not current_dict

	return False


#/*=====  End of Python Tries  ======*/

'''
/*==============================================
=            phone number to string            =
==============================================*/
'''
digit_map = {
	'2': 'abc',
	'3': 'def',
	'4': 'ghi',
	'5': 'jkl',
	'6': 'mno',
	'7': 'pqrs',
	'8': 'tuv',
	'9': 'wxyz'
}

# https://stackoverflow.com/questions/2344496/how-can-i-print-out-all-possible-letter-combinations-a-given-phone-number-can-re
# maps phone number to a list of all possible strings
def word_numbers(number):
	s = str(number)
	ret = ['']
	for char in s:
		letters = digit_map.get(char, '')
		ret = [prefix+letter for prefix in ret for letter in letters]
	return ret


# /*=====  End of phone number to string  ======*/




def easy_trie_test():
    trie = make_trie('hello', 'abc', 'baz', 'bar', 'barz')
    print(trie)
    print()

    assert in_trie(trie, 'hello')
    assert in_trie(trie, 'bar')
    assert not in_trie(trie, 'bab')
    assert not in_trie(trie, 'zzz')
 
    remove_from_trie(trie, 'abc', 0)
    print("remove 'abc'")
    print(trie)
    print()

    remove_from_trie(trie, 'hello', 0)
    print("remove 'hello'")
    print(trie)
    print()

    remove_from_trie(trie, 'bar', 0)
    print("remove 'bar'")
    print(trie)
    print()

 
    print(in_trie(trie, 1))

    print("all tests passed")

# balanced BST = O(M log N) where M = max str len, N = # of keys in tree
# using trie we can search key in O(M) time. memory = O(key_len * N)
# http://pythonfiddle.com/python-trie-implementation/

class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()
    
    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key
    
    def __getitem__(self, key):
        return self.children[key]

class Trie:
    def __init__(self):
        self.head = Node()
    
    def __getitem__(self, key):
        return self.head.children[key]
    
    def add(self, word):
        current_node = self.head
        word_finished = True
        
        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break
        
        # For ever new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1
        
        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.data = word
    
    def has_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')
        
        # Start at the top
        current_node = self.head
        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break
        
        # Still need to check if we just reached a word like 't'
        # that isn't actually a full word in our dictionary
        if exists:
            if current_node.data == None:
                exists = False
        
        return exists
    
    def start_with_prefix(self, prefix):
        """ Returns a list of all words in tree that start with prefix """
        words = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')
        
        # Determine end-of-prefix node
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words
        
        # Get words under prefix
        if top_node == self.head:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]
        
        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.data)
            
            queue = [node for key,node in current_node.children.items()] + queue
        
        return words
    
    def getData(self, word):
        """ This returns the 'data' of the node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))
        
        # Race to the bottom, get data
        current_node = self.head
        for letter in word:
            current_node = current_node[letter]
        
        return current_node.data


def test_trie():
	trie = Trie()
	words = 'hello goodbye help gerald gold tea ted team to too tom stan standard money'
	for word in words.split():
		trie.add(word)
	print("'goodbye' in trie: ", trie.has_word('goodbye'))
	print(trie.start_with_prefix('g'))
	print(trie.start_with_prefix('to'))


def trie_suffix():
	pass



# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
def KMPSearch(pat, txt):
	m = len(pat)
	n = len(txt)

	lps = [0] * m
	j = 0

	computelps(pat, m, lps)

	i=0
	while i < n:
		if pat[j] == txt[i]:
			i+=1
			j+=1

		if j == m:
			print("Found pattern at index " + str(i-j))
			j = lps[j-1]
		elif i < n and pat[j] != txt[i]:
			if j!=0:
				j = lps[j-1]
			else:
				i+=1

def computelps(pat, m, lps):

	i=1
	j = 0

	while i < m:
		if pat[i] == pat[j]:
			j+=1
			lps[i] = j
			i+=1
		else:
			if j != 0:
				j = lps[j-1]
			else:
				lps[i] = 0
				i+=1

txt = "AAAAABAAABA"
pat = "AAABAAA"


# essentially a trie
def aho_corasick(text, patterns):
	print("word is %s" % text)

	prev = 0
	cur = 0

	for i in range(len(text)):
		for j in range(len(patterns)):
			prev = i
			cur = 0

			while(prev != len(text) and text[prev] == patterns[j][cur]):
				prev += 1
				cur += 1

				if (cur == len(patterns[j])):
					print("Word %s appears from %d to %d" % (patterns[j], i, i+cur-1))
					break



## dictionaries
data = {'1':1, '2':2, '3':3}

# method 1
new = {}
for i, j in data.items():
	if i in new:
		new[i].append(j)
	else:
		new[i] = [j]

# method 2
new = {}
for i, j in data.items():
	group = new.setdefault("key", [])
	group.append(j)

# method 3
from collections import defaultdict
# great when default value is static but not if dynamic
new = defaultdict(list)  # or defaultdict(int) or defaultdict(intGen())
for i, j in data.items():
	new[i].append(j)


# itertools.count().next

class intGen:
	def __init__(self):
		self.i = 0

	def __call__(self):
		self.i += 1
		return self.i



if __name__=="__main__":
	trie = make_trie('foo', 'bar', 'baz', 'barz')


	easy_trie_test()
	print()
	test_trie()

	#pprint.pprint(trie)

	#print(in_trie(trie, 'baz'))
	#print(in_trie(trie, 'bart'))

	#KMPSearch(pat, txt)

	a = "ahishers"
	s = ['he', 'she', 'hers', 'his']

	aho_corasick(a, s)









