from flask import render_template 
from app import app
from logic import * 

@app.route('/')
@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/result')
def result():
	return render_template("result.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/creators')
def creators():
	return render_template("creators.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")