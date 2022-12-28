from src.pycollection.collection import Collection
from src.pycollection.enmap import Enmap
import unittest

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	coll = Collection()
	coll.set("test", "ASU")
	coll.get("test")
	a = coll.find(lambda x, y: x == "test")
	b = coll.findKey(lambda x, y: x == "ASU")
	coll.concat({"test2": "test2"})
	print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
