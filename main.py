from flask import Flask, render_template, request, redirect, url_for
import database_handler
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		db = database_handler.Database()
		spisok = db.get_zadachi()
		db.close()

		return render_template('index.html', spisok=spisok)
	else:
		zadacha = request.form.get('zadacha')

		if zadacha:
			db = database_handler.Database()
			db.add_zadacha(zadacha, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
			db.close()

		db = database_handler.Database()
		spisok = db.get_zadachi()
		db.close()

		return render_template('index.html', spisok=spisok)

@app.route('/delete_zadacha/<int:id_zadachi>', methods=['POST'])
def delete_zadacha(id_zadachi):
	db = database_handler.Database()
	db.delete_zadacha(id_zadachi)
	db.close()

	return redirect(url_for('index'))

@app.route('/change_status_zadachi/<int:id_zadachi>', methods=['POST'])
def change_status_zadachi(id_zadachi):
	db = database_handler.Database()
	db.update_status(id_zadachi)
	db.close()
	return redirect(url_for('index'))