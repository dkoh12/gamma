import itertools

def deck():
	# has 52 cards. 4 suites. 13 ranks.
	suites = ["hearts", "spades", "diamonds", "clubs"]
	ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Ace"]

	deck = itertools.product(suites, ranks)

	return deck


employees = [("Alice", "R", False), ("Bob", "R", True), ("Cat", "M", True), ("Dillon", "D", True)]


# not sure ... 
def dispatchCall():
	respondents = [i for i in employees if i[1] == "R"]
	managers = [i for i in employees if i[1] == "M"]
	directors = [i for i in employees if i[1] == "D"]


	while True:
		for i in respondents:
			if i[2] == True:
				return i
		for i in managers:
			if i[2] == True:
				return i
		for i in directors:
			if i[2] == True:
				return i



class parkingLot:
	def __init__(self, cap=100, price=5):
		self.capacity = cap
		self.filled = 0
		self.price = price

	def open_spaces(self):
		print("There are %d cars parked and %d spaces open" % (self.filled, self.capacity - self.filled))
		return self.capacity - self.filled


class car:
	def __init__(self, time):
		self.time = time

	def park(self, parkingLot):
		if parkingLot.filled == parkingLot.capacity:
			print("parking lot is full")
		else:
			parkingLot.filled += 1

	def pay(self, parkingLot):
		if parkingLot.filled > 0:
			print("paid %d dollars" % (self.time * parkingLot.price))
			print("a car left")
			parkingLot.filled -= 1


if __name__=="__main__":
	#print(list(deck()))

	p = parkingLot()
	c = car(3)

	p.open_spaces()
	c.park(p)
	p.open_spaces()

	print(c.time)
	c.pay(p)

	


