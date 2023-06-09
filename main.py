from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('secret.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        
    else:
        flash('Wrong credentials!')
    return home()

@app.route('/logout', methods=['POST'])
def do_admin_logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    
    app.run(debug=True,host='0.0.0.0', port=5000)