from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisismysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:921016@localhost/guestbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))


@app.route('/')
def index():
    result = Comments.query.all()

    return render_template('index.html', result=result)


@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/process', methods=['POST'])
def process():

    name = request.form['name']
    comment = request.form['comment']

    data = Comments(name=name, comment=comment)
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    links = ['https://www.youtube.com', 'https://www.bing.com',
             'https://www.python.org', 'https://www.enkato.com']
    return render_template('example.html', myvar='Flask example', links=links)


if __name__ == '__main__':
    app.run(debug=True)
