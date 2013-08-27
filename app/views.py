from app import app , db
from flask import render_template , request , flash , redirect , url_for
from models import Users

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

@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html' , title="Register for LocalJobs Account")
	email = request.form['email']
	if db.users.find_one({'email':email}):
		flash('User exist with email id %s' % email,'error')
		return redirect(url_for('register'))
	user = Users(request.form['email'],request.form['password'],request.form['linkedinUrl'],request.form['skills'])
	user_id = db.users.insert(user.__dict__ , w=1)
	flash(u'User created with id %s' % user_id)
	return redirect(url_for('signin'))
