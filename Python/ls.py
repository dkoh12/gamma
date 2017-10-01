import os
import os.path

def print_directory_contents(path):
	for child in os.listdir(path):
		childPath = os.path.join(path, child)
		if os.path.isdir(childPath):
			print_directory_contents(childPath)
		else:
			print(childPath)


if __name__=="__main__":
	print_directory_contents("./")