import json

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/DonaldTrump')
def donald_trump():
    current_data = return_data('JohnFreakingSmi')
    #past_data = return_past_data('realDonaldTrump')

    if len(current_data) == 0:
        current_data = None

    return render_template('generic.html',
                           title='Donald Trump',
                           info=f'Donald John Trump is the 45th and current President of the United States,'
                                f' in office since January 20, 2017. Before entering politics,'
                                f' he was a businessman and television personality.',
                           data=json.dumps(current_data),
                           pastdata=None)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404


def return_data(handle):
    """Gets all the current companies being monitored
       by the handle arg"""

    with open(r'C:\Users\James\Desktop\CTSM\Monitor\Files\monitor.json', 'r') as f:
        data = json.load(f)

    new_data = {}

    for item in data:
        if data[item]["handle"] == handle:
            new_data[item] = {}
            new_data[item].update(data[item])

    return new_data
