from flask import render_template #request, session, redirect, url_for
from models import db, User  

from app import app

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    '''if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        user_name = request.form.get("name")
        user_email = request.form.get("email")
        user_pwd = request.form.get("password")
        confirm_pwd =request.form.get("confirm_password")

        user_exists = User.query.filter_by(email= user_email).first()
        if user_exists:
            return render_template('register.html', message = "User already exists. Please log in")

        if user_pwd != confirm_pwd:
            return "Passwords do not match! Try again."
        
        new_user= User(name=user_name, email = user_email, password=user_pwd)
        db.session.add(new_user)
        db.session.commit()
        return "Successfull Registration!"'
        '''
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    return "Dashboard"
