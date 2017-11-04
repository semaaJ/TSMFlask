import json
import threading
import smtplib

from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit',  methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        handle = request.form['handle']

        threading.Thread(target=email_data, args=(name, handle,)).start()

        return render_template('index.html')

    return render_template('submit.html')


@app.route('/donaldtrump')
def donald_trump():
    data = return_data('JohnFreakingSmi')
    return render_template('generic.html',
                           title='Donald Trump',
                           info=f'Donald John Trump is the 45th and current President of the United States,'
                                f' in office since January 20, 2017. Before entering politics,'
                                f' he was a businessman and television personality.',
                           data=json.dumps(data))


@app.route('/lebronjames')
def lebron_james():
    data = return_data('KingJames')
    return render_template('generic.html',
                           title='Le Bron James',
                           info=f'LeBron Raymone James, born December 30 1984, is an American professional'
                                f' basketball player for the Cleveland Cavaliers of the National Basketball'
                                f' Association (NBA)',
                           data=json.dumps(data))


@app.route('/justinbieber')
def justin_bieber():
    data = return_data('justinbieber')
    return render_template('generic.html',
                           title='Justin Bieber',
                           info=f'Justin Drew Bieber born March 1, 1994 is a Canadian singer and songwriter.'
                                f' Bieber has won numerous awards, including the American Music Award for Artist'
                                f' of the Year in 2010 and 2012.',
                           data=json.dumps(data))


@app.route('/katyperry')
def katy_perry():
    data = return_data('ketyperry')
    return render_template('generic.html',
                           title='Katy Perry',
                           info=f'Donald John Trump is the 45th and current President of the United States,'
                                f' in office since January 20, 2017. Before entering politics,'
                                f' he was a businessman and television personality.',
                           data=json.dumps(data))


@app.route('/rihanna')
def rihanna():
    data = return_data('rihanna')
    return render_template('generic.html',
                           title='Rihanna',
                           info=f'Robyn Rihanna Fenty February 20, 1988 is a Barbadian singer, songwriter, and actress.'
                                f' With sales exceeding 230 million records worldwide, Rihanna is one of the'
                                f' best-selling artists of all time.',
                           data=json.dumps(data))


@app.route('/eminem')
def eminem():
    data = return_data('eminem')
    return render_template('generic.html',
                           title='Eminem',
                           info=f'Marshall Bruce Mathers III born October 17, 1972 known professionally as Eminem'
                                f' is an American rapper, record producer, and actor. Eminem is the best-selling artist'
                                f' of the 2000s in the United States. With US sales of 45.1 million albums and'
                                f' 42 million tracks as of June 2014,',
                           data=json.dumps(data))

@app.route('/elizabethwarren')
def elizabeth_warren():
    data = return_data('senwarren')

    return render_template('generic.html',
                           title='Elizabeth Warren',
                           info=f'Elizabeth Ann Warren is an American academic and politician. A member of the Democratic Party,'
                                f' she is the senior United States Senator from Massachusetts. Warren was formerly a professor of law,'
                                f' and taught at the University of Texas School of Law, the University of Pennsylvania Law School,'
                                f' and most recently at Harvard Law School.',
                           data=json.dumps(data))

@app.route('/nicolasmaduro')
def nicolas_maduro():
    data = return_data('senwarren')

    return render_template('generic.html',
                           title='Nicolas Maduro',
                           info=f'Nicolás Maduro Moros, born 23 November 1962 is a Venezuelan politician who has been the President of Venezuela'
                                f' since assuming office in 2013. A former bus driver, Maduro rose to become a trade union leader, before being elected'
                                f" to the National Assembly in 2000. As a result of Chávez's policies and Maduro's continuation of them,"
                                f" Venezuela's socioeconomic status declined, with crime, inflation, poverty and hunger increasing.",
                           data=json.dumps(data))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404


def email_data(name, handle):
    try:
        text = f'A new Celebrity has just been submitted. {name} - {handle}'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("EMAIL", "PASSWORD")
        server.sendmail("EMAIL", "PASSWORD", text)
        server.quit()

    except smtplib.SMTPException as error:
        print(error)


def return_data(handle):
    """Gets all the current companies being monitored
       by the handle arg

       data_type = current/old json file"""

    with open(r'/root/Monitor/Files/monitor.json', 'r') as f:
        current_data = json.load(f)

    with open(r'/root/Monitor/Files/monitor.json', 'r') as f:
        past_data = json.load(f)

    data = {
        "current companies being monitored": {
            "empty": "We are not currently monitoring any companies!",
        },
        "past companies monitored": {
            "empty": "Sorry, nothing to show here!",
        }
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
