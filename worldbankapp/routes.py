from worldbankapp import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/project-one')
def project_one():
    return render_template('project_one.html')

@app.route('/virtual-reality')
def virtual_reality():
    return render_template('virtual_reality.html')

@app.route('/data-dashboard')
def data_dashboard():
    return render_template('data_dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')
