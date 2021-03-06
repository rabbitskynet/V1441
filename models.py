# coding=utf-8
from decimal import Decimal
from datetime import datetime
from pony.orm import *

db = Database("sqlite", "database.sqlite", create_db=True)


class Adv(db.Entity):
	_table_ = "Advs"
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
	advs = Set(Adv)
	type = Required(int)
	comments = Set("Comment")


class Photo(db.Entity):
	_table_ = "Photos"
	id = PrimaryKey(int, auto=True)
	filename = Required(str)
	adv = Required(Adv)


class Message(db.Entity):
	_table_ = "Messages"
	id = PrimaryKey(int, auto=True)
	userto = Required(str)
	datetime = Required(datetime)
	content = Required(str, 500, lazy=True)
	user = Required(User)


class Car(db.Entity):
	id = PrimaryKey(int, auto=True)
	_table_ = "Cars"
	model = Required("Model")
	advs = Set(Adv)
	comments = Set("Comment")
	approved = Required(bool)
	transmission = Optional(str)
	color = Optional(str)
	motor_power = Optional(float)
	body_type = Optional(str)
	motor_type = Optional(str)
	rudder = Optional(str)

class Automark(db.Entity):
	_table_ = "Automarks"
	name = PrimaryKey(str)
	description = Required(str)
	models = Set("Model")
	
class Model(db.Entity):
	_table_ = "Models"
	automark = Required("Automark")
	name = PrimaryKey(str)
	cars = Set(Car)


class Comment(db.Entity):
	_table_ = "Comments"
	id = PrimaryKey(int, auto=True)
	user = Required(User)
	car = Required(Car)
	content = Required(str, 1000)
	mark = Required(int)


sql_debug(True)
db.generate_mapping(create_tables=True)


@db_session
def populate_database():
	if select(s for s in User).count() > 0:
		return
	u1 = User(login="jonnny", password="123456",
			  email="joyiee@google.com", status="Confirmed",
			  county="USA", FIO="Endrue Jonatan Ferhemshtein",
			  telephone=3345144, city="New York",
			  type=0)
	u2 = User(login="dummy34", password="654321",
			  email="mich47@google.com", status="Confirmed",
			  county="Germany", FIO="Michael fon Aubershazen",
			  telephone=35745685, city="Berlin",
			  type=0)
	u3 = User(login="betty4", password="123321",
			  email="jonny@google.com", status="NotConfirmed",
			  county="GB", FIO="ser John Brown",
			  telephone=73542622, city="London",
			  type=0)
	m1 = Automark(name = "KIA", description = u"Kia Motors Corporation — корейская автомобилестроительная компания, второй автопроизводитель в Южной Корее и седьмой в мире.")
	m2 = Automark(name = "Ford", description = u"Ford — американская автомобилестроительная компания, производитель автомобилей под марками «Ford».")
	m3 = Automark(name = "Chevrolet", description = u"Chevrolet, — марка автомобилей, производимых и реализуемых одноимённым экономически самостоятельным подразделением корпорации General Motors.")
	
	md1 = Model(automark=m1, name="Ceed")
	md2 = Model(automark=m1, name="Cerato")
	md3 = Model(automark=m2, name="Focus")
	md4 = Model(automark=m3, name="Cruze")

	c1 = Car(model=md1, approved=False,
			 transmission="mechanic", color="red",
			 motor_power=1.2, body_type="hatchback",
			 motor_type="diesel", rudder="left")
	c2 = Car(model=md2,  approved=True,
			 transmission="automate", color="blue",
			 motor_power=4.4, body_type="sedan",
			 motor_type="gasoline", rudder="right")
	c3 = Car(model=md3,  approved=True,
			 transmission="mechanic", color="green",
			 motor_power=2.4, body_type="hatchback",
			 motor_type="diesel", rudder="left")
	c4 = Car(model=md4,  approved=False,
			transmission="mechanic", color="black",
			motor_power=3.4, body_type="wagon",
			motor_type="gasoline", rudder="left")
	c5 = Car(model=md1, approved=True,
			transmission="mechanic", color="black",
			 motor_power=1.4, body_type="hatchback",
			 motor_type="diesel", rudder="left")
	Com1 = Comment(id=1, user=u1,
				   car=c1, content=u"Машина отличная мне понравилась всем советуюю на пять  сплюсом",  
				   mark=5)
	Com2 = Comment(id=2, user=u1,
				   car=c2, content=u"Эта модедь мне не очень понравилась эта модель на любителя",
				   mark=2)
				   
	a1 = Adv(user=u1, name=u"Тачка ОГОНЬ",
			year=2000, price=150000,
			mileage=65000, car=c1, comments=u"Быстрая, мощная, без документов")
	a2 = Adv(user=u2, name=u"Продам ласточку",
			year=1995, price=100000,
			mileage=180000, car=c2, comments=u"Хорошая машина, долго служила")
	a3 = Adv(user=u3, name=u"Продаю супер машину",
			year=2006, price=2000000,
			mileage=32000, car=c3, comments=u"Хорошая машинка, битая немного")
	a4 = Adv(user=u1, name=u"Шевролет",
			year=2012, price=250000,
			mileage=48000, car=c4, comments=u"Хорошая, быстро стартует, немного пороги битые")

	P1 = Photo(filename ="43dbd3af.jpg",adv=a1)
	P2 = Photo(filename ="29ecf6e9.jpg",adv=a2)
	P3 = Photo(filename ="3f0e3d67.jpg",adv=a3)
	P4 = Photo(filename ="aa5ae820.jpg",adv=a4)

    # d2 = Department(name="Department of Mathematical Sciences")
	# d3 = Department(name="Department of Applied Physics")
	#
	# c1 = Course(name="Web Design", semester=1, dept=d1,

# lect_hours=30, lab_hours=30, credits=3)
# c2 = Course(name="Data Structures and Algorithms", semester=3, dept=d1,
#                    lect_hours=40, lab_hours=20, credits=4)
#
# c3 = Course(name="Linear Algebra", semester=1, dept=d2,
#                    lect_hours=30, lab_hours=30, credits=4)
# c4 = Course(name="Statistical Methods", semester=2, dept=d2,
#                    lect_hours=50, lab_hours=25, credits=5)
#
# c5 = Course(name="Thermodynamics", semester=2, dept=d3,
#                    lect_hours=25, lab_hours=40, credits=4)
# c6 = Course(name="Quantum Mechanics", semester=3, dept=d3,
#                    lect_hours=40, lab_hours=30, credits=5)
#
# g101 = Group(number=101, major='B.E. in Computer Engineering', dept=d1)
# g102 = Group(number=102, major='B.S./M.S. in Computer Science', dept=d1)
# g103 = Group(number=103, major='B.S. in Applied Mathematics and Statistics', dept=d2)
# g104 = Group(number=104, major='B.S./M.S. in Pure Mathematics', dept=d2)
# g105 = Group(number=105, major='B.E in Electronics', dept=d3)
# g106 = Group(number=106, major='B.S./M.S. in Nuclear Engineering', dept=d3)
#
# s1 = Student(name='John Smith', dob=date(1991, 3, 20), tel='123-456', gpa=3, group=g101,
#                     courses=[c1, c2, c4, c6])
# s2 = Student(name='Matthew Reed', dob=date(1990, 11, 26), gpa=3.5, group=g101,
#                     courses=[c1, c3, c4, c5])
# s3 = Student(name='Chuan Qin', dob=date(1989, 2, 5), gpa=4, group=g101,
#                     courses=[c3, c5, c6])
# s4 = Student(name='Rebecca Lawson', dob=date(1990, 4, 18), tel='234-567', gpa=3.3, group=g102,
#                     courses=[c1, c4, c5, c6])
# s5 = Student(name='Maria Ionescu', dob=date(1991, 4, 23), gpa=3.9, group=g102,
#                     courses=[c1, c2, c4, c6])
# s6 = Student(name='Oliver Blakey', dob=date(1990, 9, 8), gpa=3.1, group=g102,
#                     courses=[c1, c2, c5])
# s7 = Student(name='Jing Xia', dob=date(1988, 12, 30), gpa=3.2, group=g102,
#                     courses=[c1, c3, c5, c6])


populate_database()
