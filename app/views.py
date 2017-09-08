import json

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/DonaldTrump')
def donald_trump():
    data = return_data('JohnFreakingSmi')
    return render_template('generic.html',
                           title='Donald Trump',
                           info=f'Donald John Trump is the 45th and current President of the United States,'
                                f' in office since January 20, 2017. Before entering politics,'
                                f' he was a businessman and television personality.',
                           data=json.dumps(data))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404


def return_data(handle):
    """Gets all the current companies being monitored
       by the handle arg

       data_type = current/old json file"""

    with open(r'C:\Users\James\Desktop\CTSM\Monitor\Files\monitor.json', 'r') as f:
        current_data = json.load(f)

    with open(r'C:\Users\James\Desktop\CTSM\Monitor\Files\past_companies.json', 'r') as f:
        past_data = json.load(f)

    data = {
        "current companies being monitored": {},
        "past companies monitored": {}
    }

    for item in current_data:
        if current_data[item]["handle"] == handle:
            data["current companies being monitored"][item] = {}
            data["current companies being monitored"][item].update(current_data[item])

    for item in past_data:
        if past_data[item]["handle"] == handle:
            data["past companies monitored"][item] = {}
            data["past companies monitored"][item].update(past_data[item])

    return data
