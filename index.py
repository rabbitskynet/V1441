# coding=utf-8
from flask import Flask, render_template, request
import json
from models import *
from js import *

app = Flask(__name__)
sql_debug(True)


@app.route('/')
@db_session
def index():
	automarks = select(c.automark for c  in Car)
	users = select(u for u in User)
	title = u'Главная'
	return render_template("index.html", title=title, automarks=automarks, users=users)

@app.route('/automark/<name>')
@db_session
def get_automark(name):
	cars = select((c.model, count(c)) for c in Car if c.automark == name)
	title = name
	return render_template("automark.html", title=title, name=name, cars=cars)

@app.route('/user/<name>')
@db_session
def get_user(name):
    user = User[name]
    title =  "User: " + name
    return render_template("user.html", title=title, user=user)

@app.route('/update', methods=['POST'])
@db_session
def update():
	ormdata = request.form['ormdata']
	save_changes(db, ormdata)
	return json.dumps({'status': 'ok'})


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=5000)
