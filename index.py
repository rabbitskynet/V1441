# coding=utf-8
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json
from models import *
from js import *

app = Flask(__name__)
sql_debug(True)


@app.route('/')
@db_session
def index():
    title = u'Главная'
    return render_template("model_single.html", current = "main", title=title, menuuser = getuser())

@app.route('/automarks')
@db_session
def get_json():
    automarks = Automark.select()
    return to_json(db, automarks, include=[Automark.models])

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login?<addadv>', methods=['GET'])
@db_session
def show_login_form(addadv=''):
    if request.method == 'POST':
        print request.form['username']
        print request.form['password']
        user = User.get(login=request.form['username'],password = request.form['password'])
        if user:
            setuser(user)
            url = url_for('index')
            return redirect(url)
        else:
            return render_template("login.html", current = "login",status=1, title="Login form", menuuser = getuser())
    else:
        if getuser():
            url = url_for('index')
            return redirect(url)
        if addadv:
            return render_template("login.html", current = "login",status=2, title="Logi2n form", menuuser = getuser())
        else:
            return render_template("login.html", current = "login",status=-1, title="Login form", menuuser = getuser())


@app.route('/addadv', methods=['GET', 'POST'])
@db_session
def add_adv_form():
    if request.method == 'POST':
        print request.form['username']
        print request.form['password']
        user = User.get(login=request.form['username'],password = request.form['password'])
        if user:
            setuser(user)
            return render_template("login.html", current = "login",status=0, title="Login form", menuuser = getuser())
        else:
            return render_template("login.html", current = "login",status=1, title="Login form", menuuser = getuser())
    else:
        if getuser():
            automarks = Automark.select()
            return render_template("addadv.html", current = "addadv",automarks=automarks, title="Add adv form", menuuser = getuser())
        else:
            url = url_for('show_login_form',addadv='1')
            return redirect(url)

@app.route('/get-adv-bymodel/<model>')
@db_session
def get_model_json(model):
    #print model
    advs = select(a for a in Adv if a.car.model.name == model)
    return to_json(db, {'advs': advs})


@app.route('/logout')
@db_session
def logoutuser():
    logout()
    url = url_for('show_login_form')
    return redirect(url)

@app.route('/user/')
@db_session
def get_all_users():
    users= select(u for u in User)
    title = u'Пользователи'
    return render_template("users.html", current = "users",title=title, users=users, menuuser = getuser())

def getuser():
    if 'user' in session.keys():
        if session['user']:
            return User.get(login=session['user'])
        else:
            return ''
    else:
        return ''

def setuser(qUser):
    session['user']=qUser.login

def logout():
    session['user']=''

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(host='0.0.0.0',port=5000)
