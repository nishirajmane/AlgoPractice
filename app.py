# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os
from werkzeug.utils import secure_filename
from pathlib import Path
import sys, tempfile, subprocess

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'
DATABASE = 'algopractice.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS algorithms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        filename TEXT NOT NULL,
        uploader_id INTEGER,
        source TEXT NOT NULL,
        FOREIGN KEY(uploader_id) REFERENCES users(id)
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash('Username and password required.', 'error')
            return render_template('register.html')
        conn = get_db()
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                      (username, generate_password_hash(password)))
            conn.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists.', 'error')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        flash('Login required to upload algorithms.', 'error')
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        code = request.form['code']
        if not name or not category or not code:
            flash('All fields are required.', 'error')
            return render_template('upload.html')
        if category not in ['DSA', 'MLA']:
            flash('Invalid category.', 'error')
            return render_template('upload.html')
        filename = secure_filename(f"{name.replace(' ', '_')}_{session['user_id']}.py")
        upload_folder = 'uploads'
        os.makedirs(upload_folder, exist_ok=True)
        filepath = os.path.join(upload_folder, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        conn = get_db()
        c = conn.cursor()
        c.execute('''INSERT INTO algorithms (name, category, filename, uploader_id, source) VALUES (?, ?, ?, ?, ?)''',
                  (name, category, filename, session['user_id'], 'user'))
        conn.commit()
        conn.close()
        flash('Algorithm uploaded successfully!', 'success')
        return redirect(url_for('upload'))
    return render_template('upload.html')

def get_algorithms():
    dsa_dir = Path('DSA')
    mla_dir = Path('MLA')
    dsa_algos = []
    mla_algos = []
    for f in dsa_dir.glob('*.py'):
        dsa_algos.append({'name': f.stem.replace('_', ' ').title(), 'filename': f.name, 'source': 'local'})
    for f in mla_dir.glob('*.py'):
        mla_algos.append({'name': f.stem.replace('_', ' ').title(), 'filename': f.name, 'source': 'local'})
    conn = get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM algorithms WHERE category = ? ORDER BY id DESC', ('DSA',))
    for row in c.fetchall():
        dsa_algos.append({'name': row['name'], 'filename': row['filename'], 'source': 'user'})
    c.execute('SELECT * FROM algorithms WHERE category = ? ORDER BY id DESC', ('MLA',))
    for row in c.fetchall():
        mla_algos.append({'name': row['name'], 'filename': row['filename'], 'source': 'user'})
    conn.close()
    return {'DSA': dsa_algos, 'MLA': mla_algos}

@app.route('/algorithms')
def algorithms():
    algos = get_algorithms()
    return render_template('algorithms.html', algorithms=algos)

@app.route('/algorithm/<category>/<filename>')
def view_algorithm(category, filename):
    if category not in ['DSA', 'MLA']:
        flash('Invalid category.', 'error')
        return redirect(url_for('algorithms'))
    if category == 'DSA':
        path = Path('DSA') / filename
    else:
        path = Path('MLA') / filename
    if not path.exists():
        path = Path('uploads') / filename
        if not path.exists():
            flash('Algorithm not found.', 'error')
            return redirect(url_for('algorithms'))
    with open(path, encoding='utf-8') as f:
        content = f.read()
    return render_template('algorithm_view.html', category=category, filename=filename, content=content)

@app.route('/code_editor')
def code_editor():
    algos = get_algorithms()
    return render_template('code_editor.html', algorithms=algos)

@app.route('/api/algorithm/<path:category_and_filename>')
def api_algorithm(category_and_filename):
    try:
        category, filename = category_and_filename.split('/', 1)
    except Exception:
        return jsonify({'error': 'Invalid path'}), 400
    if category not in ['DSA', 'MLA']:
        return jsonify({'error': 'Invalid category'}), 400
    if category == 'DSA':
        path = Path('DSA') / filename
    else:
        path = Path('MLA') / filename
    if not path.exists():
        path = Path('uploads') / filename
        if not path.exists():
            return jsonify({'error': 'Algorithm not found'}), 404
    with open(path, encoding='utf-8') as f:
        content = f.read()
    return jsonify({'content': content})

@app.route('/api/execute', methods=['POST'])
def api_execute():
    data = request.get_json()
    code = data.get('code', '')
    if not code:
        return jsonify({'success': False, 'error': 'No code provided.'})
    try:
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.py', encoding='utf-8') as tmp:
            tmp.write(code)
            tmp_path = tmp.name
        result = subprocess.run([sys.executable, tmp_path], capture_output=True, text=True, timeout=5)
        output = result.stdout
        error = result.stderr
        os.unlink(tmp_path)
        if result.returncode == 0:
            return jsonify({'success': True, 'output': output})
        else:
            return jsonify({'success': False, 'error': error or output})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True) 