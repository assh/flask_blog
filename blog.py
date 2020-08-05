from flask import Flask, render_template,url_for
app = Flask(__name__)


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
    return render_template('home.html',posts=post)


@app.route("/about")
def about():
    return render_template('about.html',title = 'About')


if __name__ == '__main__':
    app.run(debug=True)
