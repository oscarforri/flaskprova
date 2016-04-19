import sys
import sqlite3
from flask import Flask, redirect, url_for, request
from flask import render_template
from datetime import datetime, date

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('mydatabase.db')
    #return hola
    cursor = conn.execute("SELECT username,fullname,email,password FROM allusers")
    data = [row for row in cursor]
    conn.close()
    return data

def save_data(username,fullname,email,password):
    conn = sqlite3.connect('mydatabase.db')
    try:
        conn.execute("insert into allusers (username,fullname,email,password) values (?, ?, ?, ?)",
                 (username,
                  fullname,
                  email,
                  password))
        conn.commit()
        conn.close()
        return True
    except:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert_user', methods=['GET','POST'])
def insert_user():
    if request.method == 'GET':
        return render_template('insert_user_form.html')
    elif request.method == 'POST':
	    username = request.form.get('username')
	    fullname = request.form.get('fullname')
	    email = request.form.get('email')
	    password = request.form.get('password')
          save_data(username,fullname,email,password)
	    return "hola"

@app.route('/show_users')
def show_users():
    data = get_data()
    return render_template('show_user_table.html',data=data)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login_form.html')
    elif request.method == 'POST':
        user_login = request.form.get('username')
        pass_login = request.form.get('password')
        data = get_data()
        for info in data:
            (username,fullname,email,password) = info
            if (user_login == username and pass_login == password):
                return "login correctly!"
            else
                return "login error"

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
