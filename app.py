from flask import Flask
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "MAD1Bootcamp"

db.init_app(app)

with app.app_context():
    db.create_all()
    
    # adding the admin
    admin_name = 'Admin'
    admin_email = 'admin@qmaster.com'
    admin_pwd = 'admin123'
    if not User.query.filter_by(email=admin_email).first():
        admin = User(name=admin_name, email=admin_email,  password=admin_pwd ,role='admin')
        db.session.add(admin)
        db.session.commit()
        print('Created admin')
    else:
        print('Admin user already exists')

from routes import *  

if __name__ == '__main__':
    app.run(debug=True)