from flask import Flask, render_template, url_for, flash, redirect
from forms import *
import os,config
app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY
post = [
    {
        'author': 'Test 1',
        'title': 'Post 1',
        'content': 'First Post',
        'date': 'April 20,2020'
    },
    {
        'author': 'Test 1',
        'title': 'Post 1',
        'content': 'First Post',
        'date': 'April 20,2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=post)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@test.com' and form.password.data == 'password':
            flash('You have logged in.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect Username or Password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=config.DEBUG)
