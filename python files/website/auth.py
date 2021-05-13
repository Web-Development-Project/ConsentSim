from flask import Blueprint
from flask.templating import render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/createacc')
def createacc():
    return render_template("createacc.html", boolean=True)

@auth.route('/feedback')
def feedback():
    return render_template("feedback.html")

@auth.route('/index')
def index():
    return render_template("index.html")

@auth.route('/quiz')
def quiz():
    return render_template("quiz.html")

@auth.route('/resetPw')
def resetpw():
    return render_template("resetpw.html")

@auth.route('/statistics')
def statistics():
    return render_template("statistics.html")

@auth.route('/tutorial')
def tutorial():
    return render_template("tutorial.html")