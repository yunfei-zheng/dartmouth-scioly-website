from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/registration')
def registration():
    return render_template('registration.html', title="Registration")