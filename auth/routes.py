from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth_bp
from db import get_db_connection
import sqlite3

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (request.form['username'],)).fetchone()
        if user and check_password_hash(user['password'], request.form['password']):
            session['user'] = user['username']
            session['user_id'] = user['id']
            return redirect(url_for('tasks.index'))
        flash('Invalid login')
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        conn = get_db_connection()
        try:
            hashed_pw = generate_password_hash(request.form['password'])
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                         (request.form['username'], hashed_pw))
            conn.commit()
            flash("Account created.")
            return redirect(url_for('auth.login'))
        except sqlite3.IntegrityError:
            flash("Username already exists.")
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for('auth.login'))