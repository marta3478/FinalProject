import sqlite3

class Database:
	def __init__(self):
		self.connection = sqlite3.connect('zadachi.db')
		self.cursor = self.connection.cursor()

	def close(self):
		self.connection.close()

	def add_zadacha(self, text_zadachi, data_zadachi):
		query = "INSERT INTO zadachi (text_zadachi, data_zadachi, status_zadachi) VALUES (?, ?, 0)"
		args = (text_zadachi, data_zadachi)
		self.cursor.execute(query, args)
		self.connection.commit()

	def update_status(self, id_zadachi):
		query = "UPDATE zadachi SET status_zadachi = 1 WHERE id_zadachi = ?"
		args = (id_zadachi,)
		self.cursor.execute(query, args)
		self.connection.commit()

	def delete_zadacha(self, id_zadachi):
		query = "DELETE FROM zadachi WHERE id_zadachi = ?"
		args = (id_zadachi,)
		self.cursor.execute(query, args)
		self.connection.commit()

	def get_zadachi(self):
		query = "SELECT id_zadachi, text_zadachi, data_zadachi, status_zadachi FROM zadachi"
		self.cursor.execute(query)
		r0 = self.cursor.fetchall()
		result = []

		for row in r0:
			result.append({
				"id_zadachi": 		row[0],
				"text_zadachi": 	row[1],
				"data_zadachi": 	row[2],
				"status_zadachi": 	row[3]
			})

		return result

