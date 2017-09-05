from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}

    # Adding a comment for a git test

    return render_template('index.html',
                           user=user)


@app.route('/DonaldTrump')
def donald_trump():
    return render_template('generic.html',
                           title='Donald Trump',
                           info="Donald Trump is the current president of the USA.")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404
