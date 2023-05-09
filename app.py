from flask import Flask, render_template, request
from predict import predict_by_name

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

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
        form_data = {'away_team':away_team,'away_odds':round(away_odds,2),'home_team':home_team,'home_odds':round(home_odds,2), 'away_url': away_url, 'home_url': home_url}
        return render_template('result.html',form_data = form_data)

