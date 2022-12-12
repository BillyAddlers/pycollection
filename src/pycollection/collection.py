from random import choice
from typing import Dict


class Collection:
	"""
	A Dictionary with additional utility methods. This is a wrapper around the built-in dict class.
	Compared to a list, Collection can store value with primary key.
	"""
	def __init__(self, coll: Dict = None):
		"""
		Initializes a new Collection.
		@typeParam coll: Dict
		"""
		if coll is None:
			self.coll = {}
		else:
			if isinstance(coll, dict):
				self.coll = coll
			else:
				raise TypeError("Collection must be a dictionary.")

	# Getter and Setter

	# Setter
	def set(self, key, value):
		self.coll[key] = value

	# Getter
	def get(self, key):
		return self.coll[key]

	# Remove a key
	def remove(self, key):
		del self.coll[key]

	# Check whether contains certain key
	def contains(self, key):
		return key in self.coll

	# Check for collection size
	def size(self):
		return len(self.coll)

	# Check whether collection is empty
	def isEmpty(self):
		return self.size() == 0

	# Clear the collection
	def clear(self):
		self.coll = {}

	# Return all keys
	def keys(self):
		return self.coll.keys()

	# Return all values
	def values(self):
		return self.coll.values()

	# Return all items
	def items(self):
		return self.coll.items()

	# Return all keys as a list
	def __iter__(self):
		return iter(self.items())

	# Return a random key
	def randomKey(self):
		return choice(list(self.coll.keys()))

	# Return a random value
	def random(self):
		return choice(list(self.coll.values()))

	# Return a random item
	def randomItem(self):
		return choice(list(self.coll.items()))

	# Array-like
	# Methods that is basically similar to array methods

	def find(self, func):
		"""
		Returns a value that matches the function. \n
		```py
		coll.find(lambda x, y: y == "test")
		```
		where x is the key and y is the value.
		"""
		for key, value in self.coll.items():
			if func(key, value):
				return value

	def findKey(self, func):
		"""
		Returns a key that matches the function. \n
		```py
		coll.findKey(lambda x, y: y == "test")
		```
		where x is the key and y is the value.
		"""
		for key, value in self.coll.items():
			if func(key, value):
				return key

	# Return first value
	def first(self, num=0):
		return list(self.coll.values())[0 + num]

	# Return first key
	def firstKey(self, num=0):
		return list(self.coll.keys())[0 + num]

	# Return last value
	def last(self, num=0):
		return list(self.coll.values())[self.size() - 1 - num]

	# Return last key
	def lastKey(self, num=0):
		return list(self.coll.keys())[self.size() - 1 - num]

	# Returns the value at a given index
	def at(self, index):
		return list(self.coll.values())[index]

	# Returns the key at a given index
	def keyAt(self, index):
		return list(self.coll.keys())[index]

	# Identical to JavaScript's Array.reverse(), but returns a Collection
	def reverse(self):
		entries = self.coll.items().__reversed__()
		self.clear()
		for key, value in entries:
			self.set(key, value)

		return self

	# Remove all items that match the function
	def sweep(self, func):
		for key, value in self.coll.items():
			if func(value, key):
				self.remove(key)

	# Return a new collection with all items that match the function
	def filter(self, func):
		newcoll = Collection()
		for key, value in self.coll.items():
			if func(value, key):
				newcoll.set(key, value)
		return newcoll

	# Returns two collections with one that matches the function and vice-versa
	def partition(self, func):
		coll1 = Collection()
		coll2 = Collection()
		for key, value in self.coll.items():
			if func(value, key):
				coll1.set(key, value)
				self.remove(key)
			else:
				coll2.set(key, value)
				self.remove(key)
		return coll1, coll2

	# Returns a combined collection
	def combine(self, coll):
		if isinstance(coll, Collection):
			coll = coll.coll

			for key, value in coll.items():
				self.set(key, value)

			return self
		else:
			raise TypeError("Parameter must be an instance of Collection.")
