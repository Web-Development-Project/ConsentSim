from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Grade

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='testing')
        u.set_password('testingpassword')
        self.assertFalse(u.check_password('yellow'))
        self.assertTrue(u.check_password('testingpassword'))
    
    def test_count_grades(self):
        u = User(username='kate', email='kate@email.com')
        g = Grade(grade_number=3, from_user=u)
        db.session.add(u)
        db.session.add(g)
        db.session.commit()
        own = u.grades.count()
        self.assertEqual(own, 1)
    
    def test_get_latest_grade(self):
        u = User(username='kate', email='kate@email.com')
        g = Grade(grade_number=3, from_user=u)
        db.session.add(u)
        db.session.add(g)
        db.session.commit()
        result = Grade.query.filter_by(from_user=u).order_by(Grade.timestamp.desc()).first().grade_number
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main(verbosity=2)