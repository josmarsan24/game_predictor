from flask import Flask, render_template, request
from predict import predict_by_name, get_message
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'GET':
        return f"The URL /result is accessed directly. Try going to '/predict' "
    if request.method == 'POST':
        away_team = request.form['away_team']
        home_team = request.form['home_team']
        v = request.form['v']
        rtg = request.form['rtg']
        season = request.form['season']
        season = str(season.split('-')[1])
        home_odds, away_odds = predict_by_name(home_team,away_team,v,rtg,season)
        home_url = "static/" + home_team.replace(" ","") + ".png"
        away_url = "static/" + away_team.replace(" ","") + ".png"
        warning = ''
        message = get_message(home_team,away_team,float(home_odds),float(away_odds))
        print(message)

        if away_team == home_team:
            warning = 'Warning: You have chosen the same team twice so the results might not make sense'

        form_data = {'away_team':away_team,'away_odds':round(away_odds,2),'home_team':home_team,'home_odds':round(home_odds,2), 'away_url': away_url, 'home_url': home_url, 'warning': warning, 'message': message}
        return render_template('result.html',form_data = form_data)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    return render_template("500.html", e=e), 500

