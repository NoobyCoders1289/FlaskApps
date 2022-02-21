from flask import Flask, render_template

app=Flask(__name__)

posts = [
    {
        'author':'Charan Cherry',
        'title':'Blog Post 1',
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
    return render_template('home.html',posts=posts,title='All Posts')

@app.route('/about')
def about():
     return render_template('about.html')

#To run the app.py in debug Mode
if __name__ =="__main__":
    app.run(debug=True)