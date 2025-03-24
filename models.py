from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#Enrollment
user_subject = db.Table('user_subject',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                       db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'), primary_key = True),
                       db.Column('enrolled_on', db.DateTime, default = datetime.now(timezone.utc))
                    )

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(90), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    role = db.Column(db.String(80), nullable=False, default='user')
    

    #def __repr__(self):
     #   return f'<User {self.id} {self.name}>'
    
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80),unique=True, nullable=False)
    description = db.Column(db.String)

    chapters = db.relationship('Chapter', backref='subject', lazy=True)

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String)

    quizzes = db.relationship('Quiz', backref='Chapter', lazy=True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chapter_id =db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    dateofquiz = db.Column(db.Date, nullable=False)
    time_duration = db.Column(db.Time, nullable = False)
    total_marks = db.Column(db.Integer, nullable=True)
    passing_marks = db.Column(db.Integer, nullable=True)
    created_at= db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    created_at= db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    questions = db.relationship('Questions', backref='Quiz', lazy=True)

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quiz_id =db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    ques_statement = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String(255), nullable = False)
    option2 = db.Column(db.String(255), nullable = False)
    option3 = db.Column(db.String(255), nullable = False)
    option4 = db.Column(db.String(255), nullable = False)
    crct_option = db.Column(db.Integer, nullable = False)
    created_at = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))

class Scores(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    quiz_id =db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp_attempted = db.Column(db.DateTime, default = lambda: datetime.now(timezone.utc))
    total_score = db.Column(db.Integer, nullable = False)
    total_attempted = db.Column(db.Integer, nullable = False)
    crct_answers = db.Column(db.Integer, nullable = False)
