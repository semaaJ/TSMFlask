import os
import tweepy

from flask import render_template
from app import app

# Set up Twitter
CON_KEY = 'hO1xjwg0YcI1YSQZBJBhbCGyG'
CON_SEC = 'aPJlGid4V5Tl54TdZg0cJoGNGqaGFAxK9IPLlOn262DGWSrO23'
ACC_TOK = '822896244200734720-Ettkj1QkZmYBHK0wSRMWvSeWyyykEje'
ACC_SEC = 'RfpK24UGnCXs01rSTVoMYDv9FRMq0ATh0tyL5UBWUhQdv'

auth = tweepy.OAuthHandler(CON_KEY, CON_SEC)
auth.set_access_token(ACC_TOK, ACC_SEC)
twitter = tweepy.API(auth)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/DonaldTrump')
def donald_trump():
    latest_tweet = twitter.user_timeline(screen_name='realDonaldTrump', count=1)[0]

    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]

    d = {'Donald Trump - 6/9/2017': {'legend': 'Trump',
                                     'labels': ["January", "February", "March",
                                                "April", "May", "June", "July", "August"],
                                     'values': [10, 9, 8, 7, 6, 4, 7, 8]
                                     }}

    return render_template('generic.html',
                           title='Donald Trump',
                           **d,
                           legend='Donald Trump - 6/9/2017')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

