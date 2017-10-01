import os
import sys

def dropbox():
	rootdir = sys.argv[1]

	print("rootdir (absolute) = " + os.path.abspath(rootdir))

	for root, subdirs, files in os.walk(rootdir):
		print("--\nroot = " + root)
		list_file_path = os.path.join(root, "my-directory-list.txt")
		print('list_file_path = '+ list_file_path)

		with open(list_file_path, "wb") as list_file:
			for subdir in subdirs:
				print('\t- subdirectory ' + subdir)

			for filename in files:
				file_path = os.path.join(root, filename)

				print('\t- file %s (full path: %s)' % (filename, file_path))

				with open(file_path, "rb") as f:
					f_content = f.read()
					list_file.write(("The file %s contains:\n" % filename).encode("utf-8"))
					list_file.write(f_content)
					list_file.write(b'\n')

"""
Want to output

New York
-Manhattan
San Francisco Bay Area
-San Francisco
-South Bay
--San Jose

up to 5 levels and alphabetical order.
"""
def order_cities(locations):
	names = [i for i in locations if not i["parent_id"]]

	print(names)
	print()
	for i in names:
		d = {}
		d[i["name"]] = []
		for j in locations:
			if i["id"] == j["parent_id"]:
				d[i["name"]].append({j["name"]:[]})

	print(d)


if __name__=="__main__":
	#dropbox()

	locations = [{"id":1, "name":"San Francisco Bay Area", "parent_id":None},
	{"id":2, "name":"San Jose", "parent_id":3},
	{"id":3, "name":"South Bay", "parent_id":1},
	{"id":4, "name":"San Francisco", "parent_id":1},
	{"id":5, "name":"Manhattan", "parent_id":6},
	{"id":6, "name":"New York", "parent_id":None}]

	order_cities(locations)