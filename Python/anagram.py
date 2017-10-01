# groups anagrams together by words

from collections import Counter

def isAnagram(w1, w2):
	s1 = Counter(w1)
	s2 = Counter(w2)
	s1.subtract(s2)
	for i in s1.values():
		if i != 0:
			return False
	return True

def group(lst):
	d = dict()
	for i in lst:
		if not d:
			d[i] = [i]
		else:
			flag=True
			for k in d.keys():
				if isAnagram(k, i):
					d[k].append(i)
					flag=False
					break
			if flag:
				d[i] = [i]

	return [i for i in d.values()]
	

if __name__=="__main__":
	print(group(["art", "rat", "bats", "banana", "stab", "tar"]))

#words = ['cat', 'star', 'act', 'god', 'arts', 'dog', 'rats']
#print(sorted(words,key=lambda x:len(x)))