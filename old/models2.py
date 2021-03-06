from decimal import Decimal
from datetime import datetime
from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)


class Advs(db.Entity):
	id = PrimaryKey(int, auto=True)
	user = Required("User")
	name = Required(str)
	year = Required(int)
	price = Required(int)
	comments = Required(LongStr)
	mileage = Optional(Decimal)
	car = Required("Car")
	photos = Set("Photo")


class User(db.Entity):
	_table_ = "Users"
	login = PrimaryKey(str)
	password = Required(str)
	email = Required(LongStr)
	status = Required(str)
	county = Required(str)
	FIO = Optional(LongStr)
	telephone = Required(int)
	city = Required(str)
	messages = Set("Message")
	advss = Set(Advs)
	type = Required(unicode)
	comments = Set("Comment")


class Photo(db.Entity):
	_table_ = "Photos"
	id = PrimaryKey(int, auto=True)
	filename = Required(str)
	advs = Required(Advs)


class Message(db.Entity):
	id = PrimaryKey(int, auto=True)
	userto = Required(str)
	datetime = Required(datetime)
	content = Required(str, 500, lazy=True)
	user = Required(User)


class Car(db.Entity):
	model = Required(str)
	automark = Required(str)
	advss = Set(Advs)
	comments = Set("Comment")
	approved = Required(bool)
	PrimaryKey(model, automark)


class Comment(db.Entity):
	id = PrimaryKey(int, auto=True)
	user = Required(User)
	car = Required(Car)
	content = Required(str, 1000)
	mark = Required(int)


sql_debug(True)

db.generate_mapping(create_tables=True)


@db_session
def populate_database():
	if select(s for s in Student).count() > 0:
		return

	d1 = Department(name="Department of Computer Science")
	d2 = Department(name="Department of Mathematical Sciences")
	d3 = Department(name="Department of Applied Physics")

	c1 = Course(name="Web Design", semester=1, dept=d1,
				lect_hours=30, lab_hours=30, credits=3)
	c2 = Course(name="Data Structures and Algorithms", semester=3, dept=d1,
				lect_hours=40, lab_hours=20, credits=4)

	c3 = Course(name="Linear Algebra", semester=1, dept=d2,
				lect_hours=30, lab_hours=30, credits=4)
	c4 = Course(name="Statistical Methods", semester=2, dept=d2,
				lect_hours=50, lab_hours=25, credits=5)

	c5 = Course(name="Thermodynamics", semester=2, dept=d3,
				lect_hours=25, lab_hours=40, credits=4)
	c6 = Course(name="Quantum Mechanics", semester=3, dept=d3,
				lect_hours=40, lab_hours=30, credits=5)

	g101 = Group(number=101, major='B.E. in Computer Engineering', dept=d1)
	g102 = Group(number=102, major='B.S./M.S. in Computer Science', dept=d1)
	g103 = Group(number=103, major='B.S. in Applied Mathematics and Statistics', dept=d2)
	g104 = Group(number=104, major='B.S./M.S. in Pure Mathematics', dept=d2)
	g105 = Group(number=105, major='B.E in Electronics', dept=d3)
	g106 = Group(number=106, major='B.S./M.S. in Nuclear Engineering', dept=d3)

	s1 = Student(name='John Smith', dob=date(1991, 3, 20), tel='123-456', gpa=3, group=g101,
				 courses=[c1, c2, c4, c6])
	s2 = Student(name='Matthew Reed', dob=date(1990, 11, 26), gpa=3.5, group=g101,
				 courses=[c1, c3, c4, c5])
	s3 = Student(name='Chuan Qin', dob=date(1989, 2, 5), gpa=4, group=g101,
				 courses=[c3, c5, c6])
	s4 = Student(name='Rebecca Lawson', dob=date(1990, 4, 18), tel='234-567', gpa=3.3, group=g102,
				 courses=[c1, c4, c5, c6])
	s5 = Student(name='Maria Ionescu', dob=date(1991, 4, 23), gpa=3.9, group=g102,
				 courses=[c1, c2, c4, c6])
	s6 = Student(name='Oliver Blakey', dob=date(1990, 9, 8), gpa=3.1, group=g102,
				 courses=[c1, c2, c5])
	s7 = Student(name='Jing Xia', dob=date(1988, 12, 30), gpa=3.2, group=g102,
				 courses=[c1, c3, c5, c6])


populate_database()