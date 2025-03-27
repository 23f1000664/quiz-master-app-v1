# exam-preparation-site
This is a project that acts as an example preparation site for multiple courses.

=======
1. Create Virtual Environment    python -m venv venv
2. venv activate command:        Set-ExecutionPolicy RemoteSigned -Scope Process
3. Activate Virtual Environment  venv/scripts/activate
4. install requirements        pip install -r requirements.txt
5. run app         python app.py


6. created database schemas for user, admin subject, chapter, quiz, questions, scores
7. tested them by giving few tests in test.py


8. => in routes.py- import app after importing models-database db which is sqlachemy.
9. => in app.py-  Import routes after initializing db