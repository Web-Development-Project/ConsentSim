from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    grades = db.relationship('Grade', backref='from_user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def own_grade(self):
        own = Grade.query.filter_by(user_id=self.id).order_by(Grade.timestamp.desc())
        return own.get(1)
    
    def count_grades(self):
        return self.grades.count()

    def min_grade(self):
        own = Grade.query.filter_by(user_id=self.id).order_by(Grade.grade_number.asc()).first()
        return own
    
    def max_grade(self):
        own = Grade.query.filter_by(user_id=self.id).order_by(Grade.grade_number.desc()).first()
        return own

    def __repr__(self):
        return '<User {}>'.format(self.username)  

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade_number = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return format(self.grade_number)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
