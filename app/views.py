from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html',title="Welcome to LocalJobs -- Location Aware Job Search Application")


@app.route('/about')
def about():
	return render_template('about.html',title="About LocalJobs")


@app.route('/contact')
def contact():
	return render_template('contact.html' , title="Contact Us")

@app.route('/signin')
def signin():
	return render_template('signin.html' , title="Signin to LocalJobs")

@app.route('/register')
def register():
	return render_template('register.html' , title="Register for LocalJobs Account")