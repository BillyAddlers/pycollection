from random import choice
from typing import Dict


class Collection:
	"""
	A Dictionary with additional utility methods. This is a wrapper around the built-in dict class.
	Compared to a list, Collection can store value with primary key.
	"""

	def __init__(self, coll: Dict = None):
		"""
		Initializes a new Collection. \n
		:param coll: A dictionary to initialize the collection with.
		"""
		if coll is None:
			self.coll = {}
		else:
			if isinstance(coll, dict):
				self.coll = coll
			else:
				raise TypeError("Collection must be a dictionary.")

	# Getter and Setter

	def set(self, key, value):
		"""
		Sets a value to a key. \n
		:param key: The key to set.
		:param value: The value to set.
		:return: The collection.
		"""
		self.coll[key] = value

	def get(self, key):
		"""
		Returns the value of a key. \n
		:param key: The key to get.
		:return: The value of the key.
		"""
		return self.coll[key]

	def remove(self, key):
		"""
		Removes a key from the collection. \n
		:param key: The key to remove.
		:return: The collection.
		"""
		del self.coll[key]

	def contains(self, key):
		"""
		Checks whether the collection contains a certain key. \n
		:param key: The key to check.
		:return: True if the collection contains the key, False if not.
		"""
		return key in self.coll

	def size(self):
		"""
		Returns the size of the collection.
		:return: The size of the collection.
		"""
		return len(self.coll)

	def isEmpty(self):
		"""
		Checks whether the collection is empty.
		:return: True if the collection is empty, False if not.
		"""
		return self.size() == 0

	def clear(self):
		"""
		Removes all entries from the collection.
		:return: The collection.
		"""
		self.coll = {}

	def keys(self):
		"""
		Returns a list of all keys in the collection.
		:return: A list of all keys in the collection.
		"""
		return self.coll.keys()

	# Return all values
	def values(self):
		"""
		Returns a list of all values in the collection.
		:return: A list of all values in the collection.
		"""
		return self.coll.values()

	def items(self):
		"""
		Returns an iterable of key, value pairs for every entry in the map.
		:return: An iterable of key, value pairs.
		"""
		return self.coll.items()

	def entries(self):
		"""
		Returns an iterable of key, value pairs for every entry in the map.
		An alias for Collection.items()
		:return: An iterable of key, value pairs.
		"""
		return self.coll.items()

	def __iter__(self):
		"""
		Returns an iterable of all keys in the collection.
		:return: IterableIterator [K, V].
		"""
		return iter(self.items())

	def randomKey(self):
		"""
		Returns a random key from the collection.
		:return: A random key from the collection.
		"""
		return choice(list(self.coll.keys()))

	def random(self):
		"""
		Returns a random value from the collection.
		:return: A random value from the collection.
		"""
		return choice(list(self.coll.values()))

	def randomItem(self):
		"""
		Returns a random item from the collection.
		:return: A random item from the collection.
		"""
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
		:param func: The function to match.
		:return: The value that matches the function.
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
		:param func: The function to match.
		:return: The key that matches the function.
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

	def partition(self, func):
		"""
		Splits the collection into two collections, one with the items that match the function, and one with the items that don't match the function. \n
		:param func: The function to match.
		:return: A tuple of two collections.
		"""
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

	def combine(self, coll):
		"""
		Combines two collections into one. \n
		```py
		a = Collection()
		coll.combine(a)
		```
		:param coll: The collection to combine.
		:return: The combined collection.
		"""
		if isinstance(coll, Collection):
			coll = coll.coll

			for key, value in coll.items():
				self.set(key, value)

			return self
		else:
			raise TypeError("Parameter must be an instance of Collection.")

	def merge(self, coll, func1=None, func2=None, func3=None):
		if isinstance(coll, Collection):

			return self
		else:
			raise TypeError("Parameter must be an instance of Collection.")

	def concat(self, coll):
		"""
		Concatenates two collections into one. \n
		An alias to Collection.combine() method. \n
		:param coll: The collection to concatenate.
		:return: The concatenated collection.
		"""
		return self.combine(coll)

	def clone(self):
		"""
		Clones the collection.
		:return: The cloned collection.
		"""
		return Collection(self.coll)

	def difference(self, coll):
		"""
		Returns a new collection with all items that are not in the given collection. \n
		:param coll: The collection to compare.
		:return: The new collection.
		"""
		newcoll = Collection()
		for key, value in self.coll.items():
			if not coll.contains(key):
				newcoll.set(key, value)
		return newcoll

	def intersect(self, coll):
		"""
		Returns a new collection with all items that are in the given collection. \n
		:param coll: The collection to compare.
		:return: The new collection.
		"""
		newcoll = Collection()
		for key, value in self.coll.items():
			if coll.contains(key):
				newcoll.set(key, value)
		return newcoll

	def each(self, func):
		"""
		Iterates through each item in the collection. \n
		:param func: The function to execute.
		:return: The collection.
		"""
		for key, value in self.coll.items():
			func(value, key)
		return self

	def forEach(self, func):
		"""
		Iterates through each item in the collection. \n
		An alias to Collection.each() method. \n
		:param func: The function to execute.
		:return: The collection.
		"""
		return self.each(func)

	def every(self, func):
		"""
		Iterates through each item in the collection. \n
		An alias to Collection.each() method. \n
		:param func: The function to execute.
		:return: The collection.
		"""
		return self.each(func)

	def ensure(self, key, value):
		"""
		Ensures that a key exists in the collection. \n
		:param key: The key to check.
		:param value: The value to set if the key does not exist.
		:return: The collection.
		"""
		if not self.contains(key):
			self.set(key, value)
		return self

	def flatMap(self, func):
		"""
		Flattens the collection by one level. \n
		:param func: The function to execute.
		:return: The collection.
		"""
		newcoll = Collection()
		for key, value in self.coll.items():
			newcoll.set(key, func(value, key))
		return newcoll

	def has(self, key):
		"""
		Checks if the collection has a key. \n
		:param key: The key to check.
		:return: True if the key exists, False if not.
		"""
		return self.contains(key)

	def hasAll(self, *keys):
		"""
		Checks if the collection has all keys \n
		:param keys: The keys to check in form of Tuple/Array/List.
		:return: True if all keys exist, False if not.
		"""
		for key in keys:
			if not self.contains(key):
				return False
		return True

	def hasAny(self, *keys):
		"""
		Checks if the collection has any key \n
		:param keys: The keys to check in form of Tuple/Array/List.
		:return: True if any key exists, False if not.
		"""
		for key in keys:
			if self.contains(key):
				return True
		return False
