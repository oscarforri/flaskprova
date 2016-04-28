import sys
from flask import Flask, request
from flask import render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base

app = Flask(__name__)

#Declare functions
def get_userORM():
    engine = create_engine('sqlite:///sqlalchemy_users.db', echo=True)
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    data = session.query(User.username, User.fullname, User.email, User.password).all()
    return data

def save_userORM(username, fullname, email, password):
    engine = create_engine('sqlite:///sqlalchemy_users.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    ed_user = User(username, fullname, email, password)
    session.add(ed_user)
    session.commit()

#Home Page.
@app.route('/')
def index():
    return render_template('index.html')

#Formpage to register new users.
@app.route('/insert_user', methods=['GET','POST'])
def insert_user():
 if request.method == 'GET':
          return render_template('insert_user_form.html')
 elif request.method == 'POST':
 	username = request.form.get('username')
	fullname = request.form.get('fullname')
	email = request.form.get('email')
	password = request.form.get('password')
        save_userORM(username,fullname,email,password)
	return render_template('registered_correctly.html')

#Shows information of all users that are registered in our database.
@app.route('/show_users')
def show_users():
    data = get_userORM()
    return render_template('show_user_table.html', data=data)

#Login Form to enter to private content.
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html')
    elif request.method == 'POST':
        user_login = request.form.get('username')			#User from web
        pass_login = request.form.get('password')			#Pass from web
        data = get_userORM()						#Get all the content of the database
        for info in data:						#Iterate "usercontent" for "usercontent" to all the database content
            (username,fullname,email,password) = info
            if (username == user_login and password == pass_login):	#If the user and pass from the web matches with one "usercontent" of the database:
                return render_template('login_correctly.html')			#Call login_correctly.html
                break
        return render_template('login_error.html')			#Else: call login_error.html


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
