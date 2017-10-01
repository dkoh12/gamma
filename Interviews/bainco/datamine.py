
import json, sys, unittest

def get_data(filename):
	json_data = open(filename)
	data = json.load(json_data)
	json_data.close()

	return data

# SUPPORTED INSTRUCTIONS

def locate(data, state):
	filtered_data = [data[i] for i in range(len(data)) if data[i]['state'] == state]
	return filtered_data

def find_before(data, year):
	filtered_data = [data[i] for i in range(len(data)) if data[i]['year_founded'] != '' and int(data[i]['year_founded']) <= int(year)]
	return filtered_data

def find_after(data, year):
	filtered_data = [data[i] for i in range(len(data)) if data[i]['year_founded'] != '' and int(data[i]['year_founded']) >= int(year)]
	return filtered_data

def find_between(data, num_employees):
	filtered_data = [data[i] for i in range(len(data)) if data[i]['full_time_employees'] == num_employees]
	return filtered_data

def find_type(data, ctype):
	filtered_data = [data[i] for i in range(len(data)) if data[i]['company_category'] == ctype]
	return filtered_data


valid_instructions = {'locate': locate, 'find_before': find_before, 'find_after': find_after, 
	'find_between': find_between, 'find_type': find_type}


def filter_name(data):
	filtered_data = [data[i]['company_name'] for i in range(len(data))]
	return filtered_data

def main():
	args = sys.argv

	if len(args) == 1:
		print("Please pass in a json file as a command line argument")
		return

	try:
		data = get_data(args[1])
	except:
		print("please enter a valid json file")
		return

	args = args[2:]

	for index, val in enumerate(args):
		if index % 2 == 0:
			if val not in valid_instructions:
				print("please enter a valid instruction as a common line argument")
				return
			data = valid_instructions[val](data, args[index+1])


	names = filter_name(data)

	print("Company Names:")
	print(', '.join(names))
	print()
	print("Number of Companies: %d" % len(names))


# TESTING

def test():
	data = get_data('data.json')

	filtered_CA = locate(data, 'CA')
	assert len(filtered_CA) == 74

	filtered_before_2000 = find_before(data, 2000)
	assert len(filtered_before_2000) == 121

	filtered_after_2002 = find_after(data, 2002)
	assert len(filtered_after_2002) == 187

	filtered_between = find_between(data, '51-200')	
	assert len(filtered_between) == 62

	filtered_type = find_type(data, 'Data/Technology')
	assert len(filtered_type) == 59

	# apply two filters
	two_filters = find_before(filtered_CA, 2000)
	assert len(two_filters) == 15

	print("All tests passing")


class SimplisticTest(unittest.TestCase):
	def __init__(self, testname, filename):
		super(SimplisticTest, self).__init__(testname)
		self.data = get_data(filename)

	def test_locate_CA(self):
		self.assertEqual(len(locate(self.data, 'CA')), 74)

	def test_before_2000(self):
		self.assertEqual(len(find_before(self.data, 2000)), 121)

	def test_after_2002(self):
		self.assertEqual(len(find_after(self.data, 2002)), 187)

	def test_between(self):
		self.assertEqual(len(find_between(self.data, '51-200')), 62)

	def test_type(self):
		self.assertEqual(len(find_type(self.data, 'Data/Technology')), 59)

	def test_two_filter(self):
		self.assertEqual(len(find_before(locate(self.data, 'CA'), 2000)), 15)

if __name__=="__main__":
	# test() # uncomment here to test
	main()

	# uncomment here for unittest
	# minetest = unittest.TestSuite()
	# minetest.addTest(SimplisticTest('test_locate_CA', 'data.json'))
	# unittest.TextTestRunner(verbosity=2).run(minetest)

