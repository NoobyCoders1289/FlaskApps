from distutils.log import debug
from turtle import home
from flask import Flask, redirect, render_template, url_for, flash

from forms import RegistrationForm, LoginForm

app=Flask(__name__)

app.config['SECRET_KEY']='673b02697ceecbac65a9591ffeb47c0d'

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
# * ! danger
if __name__=='__main__':
    app.run(debug=True)