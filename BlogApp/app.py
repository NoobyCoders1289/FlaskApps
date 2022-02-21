from flask import Flask

app=Flask(__name__)


@app.route('/')
@app.route('/home')
def hello():
    return "<h1>Hello World!!!</h1>"

@app.route('/about')
def about():
     return "<h1>About Page</h1>"


#To run the app.py in debug Mode
if __name__ =="__main__":
    app.run(debug=True)