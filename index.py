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
    title = u'Главная'
    return render_template("index.html", current = "main",title=title)

@app.route('/automark/')
@db_session
def get_all_automarks():
    automarks = select((ad.car.automark,count(ad)) for ad in Adv )
    title = u'Марки автомобилей'
    return render_template("automarks.html", current = "automark",title=title, automarks=automarks)

@app.route('/automark/<name>')
@db_session
def get_models(name):
    #~ cars = select((c.model, count(c)) for c in Car if c.automark.name == name)
    cars = select((ad.car.model,count(ad)) for ad in Adv if ad.car.automark.name == name)
    title = name
    return render_template("models.html", current = "marks", title=title, cars=cars)


@app.route('/automarknew')
@db_session
def get_automark_new():
    title="Commmon bro"
    return render_template("model_single.html", current = "OnePage", title=title)



@app.route('/automarks')
@db_session
def get_json():
    automarks = Automark.select()
    return to_json(db, automarks, include=[Automark.models])
    
@app.route('/get-adv-bymodel/<model>')
@db_session
def get_model_json(model):
    print model
    advs = select(a for a in Adv if a.car.model.name == model)
    return to_json(db, {'advs': advs})

@app.route('/automark/<mark>/<model>')
@db_session
def get_adv_by_markmodel(mark,model):
    #~ cars = select(c for c in Car if c.automark.name == mark and c.model == model)
    ads = select(ad for ad in Adv if ad.car.automark.name == mark and ad.car.model == model)
    title = mark + "/" + model
    return render_template("model_advs.html", current = "qwe", title=title, ads=ads)

@app.route('/user/')
@db_session
def get_all_users():
    users= select(u for u in User)
    title = u'Пользователи'
    return render_template("users.html", current = "users",title=title, users=users)

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
