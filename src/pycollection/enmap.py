from sqlite3 import connect
from src.pycollection.collection import Collection
import json
from typing import Dict


class Enmap(Collection):
	def __init__(self, db_name="enmap.db"):
		super().__init__()

		self.con = connect(db_name)
		self.cur = self.con.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS enmap (key TEXT PRIMARY KEY, value TEXT)")
		self.con.commit()

		tempdata = self.cur.execute("SELECT * FROM enmap").fetchall()
		for key, value in tempdata:
			self.set(key, value)

	def set(self, key, value):
		value = json.dumps(value)

		self.cur.execute("SELECT COUNT(*) FROM enmap WHERE key = ?", (key,))
		if self.cur.fetchone()[0] == 0:
			self.cur.execute("INSERT INTO enmap VALUES (?, ?)", (key, value))
		else:
			self.cur.execute("UPDATE enmap SET value = ? WHERE key = ?", (value, key))

		self.con.commit()
		super().set(key, value)

	def get(self, key) -> Dict:
		data = json.loads(super().get(key))
		return data

	def remove(self, key):
		self.cur.execute("DELETE FROM enmap WHERE key = ?", (key,))
		self.con.commit()
		super().remove(key)

	def clear(self):
		self.cur.execute("DELETE FROM enmap")
		self.con.commit()
		super().clear()

	def refresh(self):
		tempdata = self.cur.execute("SELECT * FROM enmap").fetchall()
		for key, value in tempdata:
			self.set(key, value)
