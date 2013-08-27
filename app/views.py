from app import app , db , login_manager
from flask import render_template , request , flash , redirect , url_for ,g
from models import Users
from flask.ext.login import login_user , logout_user , current_user , login_required
from bson.objectid import ObjectId

@app.route('/')
@login_required
def index():
	return render_template('index.html',title="Welcome to LocalJobs -- Location Aware Job Search Application")


@app.route('/about')
def about():
	return render_template('about.html',title="About LocalJobs")


@app.route('/contact')
def contact():
	return render_template('contact.html' , title="Contact Us")

@app.route('/signin' , methods=['GET','POST'])
def signin():
	if request.method == 'GET':
		return render_template('signin.html' , title="Signin to LocalJobs")

	email = request.form['email']
	password = request.form['password']
	remember_me = False
	if 'rememberme' in request.form:
		remember_me = True
	users_dict = db.users.find_one({'email':email , 'password':password})
	if users_dict is None:
		flash('Email or password is invalid' , 'error')
		return redirect(url_for('signin'))
	registered_user = Users(users_dict.get('email'),users_dict.get('password'),users_dict.get('linkedin_profile_url'),users_dict.get('skills'))
	registered_user.id = users_dict.get('_id')
	login_user(registered_user, remember = remember_me)
	flash('Logged in successfully')
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/register' , methods=['GET','POST'])
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index')) 

@login_manager.user_loader
def load_user(id):
	users_dict = db.users.find_one({"_id": ObjectId(str(id))})
	registered_user = Users(users_dict.get('email'),users_dict.get('password'),users_dict.get('linkedin_profile_url'),users_dict.get('skills'))
	registered_user.id = users_dict.get('_id')
	return registered_user

@app.before_request
def before_request():
    g.user = current_user
