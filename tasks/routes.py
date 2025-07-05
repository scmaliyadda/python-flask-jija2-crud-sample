from flask import render_template, request, redirect, url_for, session, flash
from functools import wraps
from . import tasks_bp
from db import get_db_connection

def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash("Login required")
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return wrapper

@tasks_bp.route('/')
@login_required
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks WHERE user_id = ?', (session['user_id'],)).fetchall()
    return render_template('index.html', tasks=tasks)

@tasks_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        title = request.form['title']
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (title, user_id) VALUES (?, ?)', (title, session['user_id']))
        conn.commit()
        return redirect(url_for('tasks.index'))
    return render_template('add.html')

@tasks_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ? AND user_id = ?', (id, session['user_id'])).fetchone()
    if request.method == 'POST':
        conn.execute('UPDATE tasks SET title = ? WHERE id = ?', (request.form['title'], id))
        conn.commit()
        return redirect(url_for('tasks.index'))
    return render_template('edit.html', task=task)

@tasks_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ? AND user_id = ?', (id, session['user_id']))
    conn.commit()
    return redirect(url_for('tasks.index'))