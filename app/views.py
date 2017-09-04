from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}

    return render_template('index.html',
                           user=user)

@app.route('/DonaldTrump')
def donald_trump():
    return render_template('index.html',
                           title='Donald Trump')
