
def empty_strings(lst, word):

	for index, i in enumerate(lst):
		if i == word:
			return index


if __name__=="__main__":
	lst = ["at", "", "", "", "ball", "", "", "", "car"]
	print(empty_strings(lst, "ball"))