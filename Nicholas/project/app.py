# This is the backend
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('base1.html')

@app.route('/profile1')
def profile1():
    return render_template('profile1.html')

@app.route('/login1')
def login1():
    return render_template('login1.html')

@app.route('/signup1')
def signup1():
    return render_template('signup1.html')

if __name__ == "__main__":
    app.run()