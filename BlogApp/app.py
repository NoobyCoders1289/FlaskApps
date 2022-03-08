from distutils.log import debug
from turtle import home
from flask import Flask, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

import psycopg2
conn_string = "host='localhost' dbname='blogappdb' user='postgres' password='123123123'"
conn = psycopg2.connect(conn_string)



app=Flask(__name__)
app.config['SECRET_KEY']='673b02697ceecbac65a9591ffeb47c0d'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

#sqlalchemy database for users
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"

#sqlalchemy database for posts
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author':'Charan Cherry',
        'title':'Blog Post ',
        'content':'Fisrt post on my website',
        'date_posted': 'April 20, 2021'
    },
    {
        'author':'Ramya Hasini',
        'title':'Blog Post 2',
        'content':'Second post on my website',
        'date_posted': 'April 22, 2021'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts,)

@app.route('/about')
def about():
    title = "About"
    return render_template('about.html',title=title)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    title= 'Register'
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title=title, form=form)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    title= 'Login'
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash(f'You have been Loggedin Successfully!!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Loggin UnSuccessful. Please check email and password', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html',title=title, form=form)






#To run the app.py in debug Mode
if __name__=='__main__':
    app.run(debug=True)