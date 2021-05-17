from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EmptyForm
from app.models import User, Grade

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home') 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = ('/index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/index')
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

@app.route('/tutorial')
@login_required
def tutorial():
    return render_template('tutorial.html', title='Tutorial')

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    information = request.data 
    form = EmptyForm()
    if form.validate_on_submit():
        grade = Grade(grade_number=information, from_user=current_user)
        db.session.add(grade)
        db.session.commit()
        flash('Your grade has been saved.')
        return redirect(url_for('quiz'))
    return render_template('quiz.html', title='Quiz', form=form)

@app.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    result = Grade.query.filter_by(from_user=current_user).order_by(Grade.timestamp.desc()).first()
    return render_template('feedback.html', title='Feedback', result=result)

@app.route('/statistics', methods=['GET', 'POST'])
@login_required
def statistics():
    return render_template('statistics.html', title='Statistics')


    
