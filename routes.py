from flask import render_template, request, session, redirect, url_for
from models import *

from app import app

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        user_name = request.form.get("username")
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
        #return "Successfull Registration!"
        return render_template('login.html')
    return render_template('login.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
            if session.get('user_email'):
                return redirect(url_for('dashboard'))
            return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()

        if user:
            session['user_id'] = user.id  # Store user session
            return f"Welcome, {user.name}! Login Successful."
        else:
            return render_template('login.html', message="Invalid email or password!")
    return render_template('login.html')

'''
def login():
    if request.method == "GET":
        if session.get('user_email'):
            return redirect(url_for('dashboard'))
        return render_template('login.html')
    elif request.method == "POST":
        user_passowrd = request.form.get("name")
        user_email = request.form.get("email")
        user = db.session.get(User, user_email)
        if user:
            # user.password == user_passowrd
            session['user_email'] = user.email
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('dashboard'))
        return redirect(url_for('register'))
    '''

@app.route('/logout', methods=["GET"])
def logout():
    if session.get('user_email'):
        session['user_email'] = None
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    logged_in = session.get('user_email')
    if logged_in:
        user = db.session.get(User, session.get('user_email'))
        return render_template('user/dashboard.html')
    else:
        return redirect('/')