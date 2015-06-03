# coding=utf-8
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import json
from models import *
from js import *
import sys

app = Flask(__name__)
sql_debug(True)

@app.route('/')
@db_session
def index():
    title = u'Главная'
    return render_template("model_single.html", current = "main", title=title)

@app.route('/automarks')
@db_session
def get_json():
    automarks = Automark.select()
    return to_json(db, automarks, include=[Automark.models])

@app.route('/get-current-user')
@db_session
def get_json_user():
    return to_json(db, getuser())

@app.route('/login', methods=['GET', 'POST'])
@db_session
def show_login_form():
    if request.method == 'POST':
        userfound = User.get(login=request.form['username'],password = request.form['password'])
        if userfound:
            setuser(userfound)
            url = url_for('index')
            return redirect(url)
        else:
            return render_template("login.html", current = "login",status=1, title="Logi2n form")
            redirect(redirect_url())
    else:
        if getuser():
            url = url_for('index')
            return redirect(url)
        else:
			return render_template("login.html", current = "login",status=-1, title="Login form")


@app.route('/addadv', methods=['GET', 'POST'])
@db_session
def add_adv_form():
    if request.method == 'POST':
        user = User.get(login=request.form['username'],password = request.form['password'])
        if user:
            setuser(user)
            return render_template("login.html", current = "login",status=0, title="Login form")
        else:
            return render_template("login.html", current = "login",status=1, title="Login form")
    else:
        if getuser():
            automarks = Automark.select()
            return render_template("addadv.html", current = "addadv",automarks=automarks, title="Add adv form")
        else:
            url = url_for('show_login_form')
            return redirect(url)

@app.route('/get-adv-bymodel/<model>')
@db_session
def get_model_json(model):
    advs = select(a for a in Adv if a.car.model.name == model)
    return to_json(db, {'advs': advs})


@app.route('/logout')
@db_session
def logoutuser():
    logout()
    url = url_for('show_login_form')
    return redirect(url)

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
