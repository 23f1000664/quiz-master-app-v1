from app import app
from models import db, User, Subject, Chapter, Quiz, Questions, Scores

with app.app_context():
    '''
    #adding a user
    new_user = User(name = "Ram" , email="ram@gmail.com", password= "ramaa", role= "user")
    db.session.add(new_user)
    db.session.commit()
    print(User.query.all())

    # updating name
    Session = db.session()
    user_1 = Session.get(User, 1)
    user_1.name = "rama"
    Session.commit()
    
    # delete user
    Session = db.session()
    user = Session.query(User).filter_by(email="ram@gmail.com").first()
    if user is None:
        print("User not found")
    else:
        print("User found. Deleting user...")
        Session.delete(user)
    Session.commit()
    print("Success!")'
    '''


    '''
    # adding a subject
    #Session = db.session()
    new_subject = Subject(name = "Maths", description = "Mathematics1")
    db.session.add(new_subject)
    db.session.commit()
    

    #update subject details
    Session = db.session()
    subject = Session.get(Subject, 1)
    subject.name = "Math"
    print(subject.name)
    Session.commit()

    #delete subject
    Session = db.session()
    subject = Session.query(Subject).filter_by(name="Math").first()
    if subject is None:
        print("subject not found")
    else:
        print("subject found. Deleting subject...")
        Session.delete(subject)
        Session.commit()
        print("Success!")

    #create quiz
    new_quiz = Quiz(chapter_id="1",dateofquiz=2025-28-04 ,time_duration=15, total_marks=100, passing_marks=40,)
    db.session.add(new_quiz)
    db.session.commit()

    '''

    
