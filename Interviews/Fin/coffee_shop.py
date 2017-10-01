
from collections import deque
import json
from pprint import pprint
import csv
import unittest

brew_time = {"tea" : 3, "latte": 4, "affogato": 7}
profit = {"tea": 2, "latte": 3, "affogato": 5}

DAY = 100 # a day is 100 ticks

#########
# PART 1
#########

def get_data(filename):
	json_data = open(filename)
	data = json.load(json_data)
	json_data.close()

	return data


# organize the two barista FIFO queues to return an output
# more_money parameter if true calculates profit
def get_output(Q1, Q2, more_money=False):
	output = []

	if more_money:
		money = 0

	while not (len(Q1) == 0 and len(Q2) == 0):
		if len(Q1) == 0:
			item = Q2.popleft()
			barista = 2
		elif len(Q2) == 0:
			item = Q1.popleft()
			barista = 1
		elif Q1[0] <= Q2[0]:
			item = Q1.popleft()
			barista = 1
		else:
			item = Q2.popleft()
			barista = 2

		if more_money:
			money += profit[item[2]]
			output.append({"order_id": item[0], "start_time": item[1], "barista_id": barista, "profit": money})
		else:
			output.append({"order_id": item[0], "start_time": item[1], "barista_id": barista})

	return output

# assign the more free barista the next order
def assign_free_barista(order, barista, Q, time, drink, for_money=False):
	if barista > DAY:
		return
	if time >= barista:
		barista = time
	if for_money:
		Q.append((order, barista, drink))
	else:
		Q.append((order, barista))
	barista += brew_time[drink]

	return (barista, Q)


def fifo_solution():
	data = get_data("input.json")

	barista_1 = 0 # barista start times
	barista_2 = 0 
	Q1 = deque() #FIFO queues for Barista 1 and 2 respectively
	Q2 = deque()

	for order in data:
		order_id = order['order_id']
		time = order['order_time']
		drink = order['type']

		# day is over. can make no more drinks
		if barista_1 > DAY and barista_2 > DAY:
			break

		if barista_1 <= barista_2:
			barista_1, Q1 = assign_free_barista(order_id, barista_1, Q1, time, drink)
		else:
			barista_2, Q2 = assign_free_barista(order_id, barista_2, Q2, time, drink)

	output = get_output(Q1, Q2)
	pprint(output)

	outfile = open('output_fifo.json', 'w')
	json.dump(output, outfile, indent=4, sort_keys=True)


#########
# compare code w/ PART 2
#########

# get the total profit in a day using the FIFO solution implemented above
def fifo_solution_for_profit():
	data = get_data("input.json")

	barista_1 = 0 # barista start times
	barista_2 = 0 
	Q1 = deque() #FIFO queues for Barista 1 and 2 respectively
	Q2 = deque()

	for order in data:
		order_id = order['order_id']
		time = order['order_time']
		drink = order['type']

		# day is over. can make no more drinks
		if barista_1 > DAY and barista_2 > DAY:
			break

		# assign the more free barista the next order
		if barista_1 <= barista_2:
			barista_1, Q1 = assign_free_barista(order_id, barista_1, Q1, time, drink, True)
		else:
			barista_2, Q2 = assign_free_barista(order_id, barista_2, Q2, time, drink, True)

	# organize the two barista FIFO queues to return an output
	output = get_output(Q1, Q2, True)
	pprint(output)

	outfile = open('output_fifo_profit.json', 'w')
	json.dump(output, outfile, indent=4, sort_keys=True)



#########
# Thoughts on Scalability
#########

# breaks up the orders into windows of 4 ticks. 
# This tells us how impacted those time slots are to reflect an actual coffee shop
# for example many coffee shops are busy during lunch and dinner but not during awkward
# hours such as from 2-5pm. That is why they have happy hours. 
# by breaking it up into chunks you can see which 'windows' are impacted and can
# use some further scalability assistance
def better_alg():
	data = get_data("input.json")

	window = [] # orders within 'win' time
	win = 4 # ticks alloted to window
	lst = [] # all orders
	count = 0 # counter
	net = 0 #counter

	for order in data:
		order_id = order['order_id']
		time = order['order_time']
		drink = order['type']

		if count == 0:
			count = time
			net = count + win
		if net >= time:
			window.append((order_id, time, drink, brew_time[drink], profit[drink]))
		else:
			lst.append(window)
			count = net
			net += win
			window = []
			window.append((order_id, time, drink, brew_time[drink], profit[drink]))

	pprint(lst)

	f = open("output_better.csv", "w")
	writer = csv.writer(f)
	writer.writerows(lst)



#########
# PART 2
#########


# get the next order from the backlog and prioritize latte over affogato over tea
# as indicated by get_time()
def next_order(tea_backlog, latte_backlog, affogato_backlog, time):

	if time == 1:
		item = latte_backlog.popleft()
	elif time == 2:
		item = affogato_backlog.popleft()
	elif time == 3:
		item = tea_backlog.popleft()
	else:
		item = None

	return item


# Better explanation in README.md
def get_time(tea_backlog, latte_backlog, affogato_backlog, time):

	# some arbitrary large value.
	t_tea = t_latte = t_affogato = 2 * DAY

	if len(latte_backlog) != 0:
		t_latte = latte_backlog[0][1]
	if len(tea_backlog) != 0:
		t_tea = tea_backlog[0][1]
	if len(affogato_backlog) != 0:
		t_affogato = affogato_backlog[0][1]

	if t_latte <= time:
		return 1
	if t_affogato <= time:
		return 2
	if t_tea <= time:
		return 3
	else:
		# returns the next tick where the barista gets an order
		return min(t_tea, t_affogato, t_latte)


def emptyStock(tea_backlog, latte_backlog, affogato_backlog):
	return len(tea_backlog) == 0 and len(latte_backlog) == 0 and len(affogato_backlog) == 0


def for_money_logic(barista, Q, bid):
	if barista > DAY:
		print("Barista %d can take no more orders" % bid)
		return

	time = get_time(tea_backlog, latte_backlog, affogato_backlog, barista)
	item = next_order(tea_backlog, latte_backlog, affogato_backlog, time)
	
	# if item is none, that means the barista is idle and has no drink to make at that tick
	# so move the tick to the next time the barista makes a drink
	if item is None:
		barista = time
		print("barista %d new time %d " % barista)
		return

	Q.append((item[0], barista, item[2]))
	barista += brew_time[item[2]]

	return (barista, Q)


def initialize_backlog(data):
	tea_backlog = deque()
	latte_backlog = deque()
	affogato_backlog = deque()

	# Put all orders in the backlogs of the respective drinks
	for order in data:
		order_id = order['order_id']
		time = order['order_time']
		drink = order['type']

		if drink == "tea":
			tea_backlog.append((order_id, time, drink))
		elif drink == "latte":
			latte_backlog.append((order_id, time, drink))
		else:
			affogato_backlog.append((order_id, time, drink))

	return (tea_backlog, latte_backlog, affogato_backlog)


def for_money():
	data = get_data("input.json")

	barista_1 = 0 # barista 1 start time
	barista_2 = 0 # barista 2 start time
	Q1 = deque() #FIFO queues for Barista 1 and 2 respectively
	Q2 = deque()
	tea_backlog, latte_backlog, affogato_backlog = initialize_backlog(data)


	# Day is over cannot take any more orders
	while not (barista_1 > DAY and barista_2 > DAY):

		# Day is not over but no more orders in backlog
		if emptyStock(tea_backlog, latte_backlog, affogato_backlog):
			print("No more orders in backlog")
			break

		if barista_1 <= barista_2:
			# barista_1, Q1 = for_money_logic(barista_1, Q1, 1)

			if barista_1 > DAY:
				print("Barista 1 can take no more orders")
				continue

			time = get_time(tea_backlog, latte_backlog, affogato_backlog, barista_1)
			item = next_order(tea_backlog, latte_backlog, affogato_backlog, time)
			
			# if item is none, that means the barista is idle and has no drink to make at that tick
			# so move the tick to the next time the barista makes a drink
			if item is None:
				barista_1 = time
				print("barista 1 new time %d " % barista_1)
				continue

			Q1.append((item[0], barista_1, item[2]))
			barista_1 += brew_time[item[2]]

		else:
			# barista_2, Q2 = for_money_logic(barista_2, Q2, 2)

			if barista_2 > DAY:
				print("Barista 2 can take no more orders")
				continue

			time = get_time(tea_backlog, latte_backlog, affogato_backlog, barista_2)
			item = next_order(tea_backlog, latte_backlog, affogato_backlog, time)
		
			if item is None:
				barista_2 = time
				print("barista 2 new time %d " % barista_2)
				continue

			Q2.append((item[0], barista_2, item[2]))
			barista_2 += brew_time[item[2]]

	output = get_output(Q1, Q2, True)
	pprint(output)

	outfile = open('output_for_money.json', 'w')
	json.dump(output, outfile, indent=4, sort_keys=True)



# only did unittests for helper functions.
class SimplisticTest(unittest.TestCase):

	def test_empty_stock(self):
		self.assertTrue(emptyStock([], [], []))

	def test_not_empty_stock(self):
		self.assertFalse(emptyStock([], [1, 4, "latte"], []))

	def test_get_time_invalid_time(self):
		self.assertEqual(get_time([], [], [], 100), 200)

	def test_get_time_tea(self):
		self.assertEqual(get_time(deque([(1, 4, "tea")]), deque([]), deque([]), 4), 3)

	def test_get_time_latte(self):
		self.assertEqual(get_time(deque([]), deque([(2, 5, "latte")]), deque([]), 5), 1)

	def test_get_time_affocado(self):
		self.assertEqual(get_time(deque([]), deque([]), deque([(3, 6, "affocado")]), 6), 2)

	def test_get_time_new_set_time(self):
		self.assertEqual(get_time(deque([(1, 14, "tea")]), deque([(2, 15, "latte")]), deque([(3, 16, "affocado")]), 6), 14)

	def test_next_order_is_none(self):
		self.assertEqual(next_order([], [], [], 10), None)

	def test_next_order_is_tea(self):
		self.assertTupleEqual(next_order(deque([(1, 4, "tea")]), deque([]), deque([]), 3), (1, 4, "tea"))

	def test_next_order_is_latte(self):
		self.assertTupleEqual(next_order(deque([]), deque([(2, 5, "latte")]), deque([]), 1), (2, 5, "latte"))

	def test_next_order_is_affocado(self):
		self.assertTupleEqual(next_order(deque([]), deque([]), deque([(3, 6, "affocado")]), 2), (3, 6, "affocado"))


if __name__=="__main__":
	print("Fifo solution")
	fifo_solution()
	print()

	print("Better algorithm")
	better_alg()
	print()

	print("Fifo Solution for profit")
	fifo_solution_for_profit()
	print()

	print("For Money")
	for_money()
	print()

	unittest.main()
