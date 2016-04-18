import sys
import sqlite3
from flask import Flask, redirect, url_for, request
from flask import render_template
from datetime import datetime, date

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.execute("SELECT username,fullname,email,password from allusers")
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

@app.route('/insert_user')
def insert_user():
    return render_template('insert_user_form.html')


@app.route('/show_users')
def show_users():
    data = get_data
    return render_template('show_user_table.html', data = data)

@app.route('/login')
def login():
    return render_template('login_form.html')


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
