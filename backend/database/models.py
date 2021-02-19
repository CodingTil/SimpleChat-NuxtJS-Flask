from .db import get_connection
import json

class Message:
	def __init__(self, sender: str, message: str):
		self.sender = sender
		self.message = message

	def save(self) -> int:
		id = hash(self.sender + self.message)
		connection = get_connection()
		cursor = connection.cursor()
		cursor.execute('''
			INSERT INTO MESSAGES (SENDER, MESSAGE) VALUES (?,?)
		''', (self.sender, self.message))
		connection.commit()
		return cursor.lastrowid


def get_messages():
	connection = get_connection()
	cursor = connection.cursor()
	rows = cursor.execute('''
		SELECT * FROM MESSAGES
	''').fetchall()
	connection.commit()
	return json.dumps( [dict(ix) for ix in rows] )