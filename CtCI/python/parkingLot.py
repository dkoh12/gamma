from collections import deque
from abc import ABC, abstractmethod
from enum import Enum

calls = deque()

employees = []


class HELP(ABC):
	@abstractmethod
	def foo(self):
		pass

class Employee():
	def __init__(self):
		self.rank = rank
		self.current_call = None

class VehiceSize(Enum):
	Motorcycle = 1
	Compact = 2
	Large = 3

"""
Parking lot 

- has multiple levels
- can park cars, buses, motorcycles
- lot has motorcycle spots, compact spot, and large spot
- motorcycle can park in any spot
- car can park in either a compact spot or large spot
- bus can park in 5 large spots that are consecutive w/in same row.
"""


class Vehicle():
	def __init__(self, name):
		self._parkingSpot = []
		self._name = name
		self._license_plate = None
		self._size 


	def getName(self):
		return self._name

	def getSize(self):
		return self._size

	def parkInSpot(self, spot):
		self._parkingSpot.append(spot)

	# clears array?
	def clear(self):
		for i in range(len(self._parkingSpot)):
			self._parkingSpot[i] = " "


	@abstractmethod
	def canFitInSpot(self, spot):
		pass


	def __str__(self):
		return "Vehicle is a %s" % self.name


class Car(Vehicle):
	def __init__(self, name):
		Vehicle.__init__(self, name)
		self.spots = 1;
		self.size = VehiceSize.Compact

class Bus(Vehicle):
	def __init__(self, name):
		Vehicle.__init__(self, name)
		self.spots = 5
		self.size = VehiceSize.Large

class Motorcycle(Vehicle):
	def __init__(self, name):
		Vehicle.__init__(self, name)
		self.spots = 1
		self.size = VehiceSize.Motorcycle


class parkingSpot():
	def __init__(self, level, row, spot, size):
		self.__vehicle = None
		self.__spot = spot # _ = protected. __ = private
		self.__level = level
		self.__row = row
		self.__size = size

	def getRow(self):
		return self.__row

	def getSpot(self):
		return self.__spot

	def getSize(self):
		return self.__size

	def canFit(self, v):
		return (self.__vehicle == None) and v.canFitInSpot()

	def park(self, v):
		if not canFit(v):
			return False
		self.__vehicle = v
		self.__vehicle.parkInSpot()
		return True

	def remove(self):
		level.spotFreed()
		self.__vehicle = None


class level():
	SPOTS = 10

	def __init__(self, floor, spots):
		self.__floor = floor
		self.__parking_spots = [[" "]] * spots
		self.__available_spots = 0

	def availableSpots(self):
		return self.__available_spots

	def spotFreed(self):
		self.__available_spots += 1

	def parkVehicle(self, v):
		if availableSpots() < v.getSpotsNeeded():
			return False
		n = findAvailableSpots(v)
		if n < 0:
			return False
		return parkStartingAtSpot(n, v)

	def parkStartingAtSpot(self, n, v):
		v.clear()


	def findAvailableSpots(self, v):
		spotsNeeded = v.getSpotsNeeded()
		spotsFound = 0
		lastRow = -1
		for i in range(len(self.__parking_spots)):
			spot = self.__parking_spots[i]
			if lastRow != spot.getRow():
				spotsFound = 0
				lastRow = spot.getRow()
			if spot.canFit(v):
				spotsFound += 1
			else:
				spotsFound = 0
			if spotsFound == spotsNeeded:
				return i - (spotsNeeded - 1)

		return -1
			

class parkingLot():
	def __init__(self, levels=5):
		self.__levels = [[" "]] * levels
	
	def parkVehicle(self, v):
		for i in range(len(self.levels)):
			if self.__levels[i].parkVehicle(v):
				return True

		return False


def main():
	s = parkingSpot(5, 4, 3, 2)
	print(s.getRow())
	# print(s._spot)

	print(s.getSpot())

	# p = parkingLot()
	# v = None


	pass


if __name__=="__main__":
	main()