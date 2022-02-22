from distutils.log import debug
from flask import Flask, render_template, url_for

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
def hello():
    return render_template('home.html',posts=posts,)

@app.route('/about')
def about():
    title = "About"
    return render_template('about.html',title=title)


@app.route('/register')
def register():
    form = RegistrationForm()
    title= 'Register'
    return render_template('register.html',title=title, form=form)




@app.route('/login')
def login():
    form = LoginForm()
    title= 'Login'
    return render_template('login.html',title=title, form=form)






#To run the app.py in debug Mode
# * ! danger
if __name__=='__main__':
    app.run(debug=True)