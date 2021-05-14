from flask import Blueprint
from flask.templating import render_template

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/createacc', methods=['GET', 'POST'])
def createacc():
    return render_template("createacc.html")

@auth.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return render_template("feedback.html")

@auth.route('/')
def index():
    return render_template("index.html")

@auth.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template("quiz.html")

@auth.route('/resetPw', methods=['GET', 'POST'])
def resetpw():
    return render_template("resetpw.html")

@auth.route('/statistics')
def statistics():
    return render_template("statistics.html")

@auth.route('/tutorial')
def tutorial():
    return render_template("tutorial.html")