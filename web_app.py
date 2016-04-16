import sys
import sqlite3
from flask import render_template
#from flask import Flask, redirect, url_for, request
#from datetime import datetime, date

app = Flas(__name__)

@app.route('/')
def index():
#    return render_template('index.html')
    return "index"

@app.route('/insert_user')
def insert_user():
#    return render_template('insert_user_form.html')
    return "insert_user"

@app.route('/show_users')
def show_users():
#    return render_template('show_users_table.html')
    return "show_users"

@app.route('/login')
def login():
#    return render_template('login_form.html')
    return "login"

if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
