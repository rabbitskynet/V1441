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
	return render_template("index.html", automarks=automarks, users=users)

@app.route('/automark/<name>')
@db_session
def get_model(name):
	cars = select(c for c in Car if c.automark == name)
	return render_template("automark.html", name=name, cars=cars)

@app.route('/user/<name>')
@db_session
def get_user(name):
    user = User[name]
    return render_template("user.html", user=user)

#
# @app.route('/adv')
# @db_session
# def get_departments():
# # departments = Department.select().order_by(Department.number)
#     # return to_json(db, departments, include=[Department.groups, Department.courses])
#
# @app.route('/course-students/<name>/<semester>')
# @db_session
# def get_course_students(name, semester):
#     students = Course[name, semester].students
#     return to_json(db, {'students': students})
#
# @app.route('/group-students/<number>')
# @db_session
# def get_group_students(number):
#     students = Group[number].students
#     return to_json(db, {'students': students})

@app.route('/update', methods=['POST'])
@db_session
def update():
	ormdata = request.form['ormdata']
	save_changes(db, ormdata)
	return json.dumps({'status': 'ok'})


if __name__ == '__main__':
	app.debug = True
	app.run()
