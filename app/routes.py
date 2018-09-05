from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index(): 
    user = {'username' : 'Sergio'}
    posts = [
        {
            'author': {'username': 'LeBron'},
            'body': 'Beautiful day in Los Angeles!'
        },
        {
            'author': {'username': 'Amanda'},
            'body': 'Sorry to Bother You was a good movie!'
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
