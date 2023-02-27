from flask import Flask, render_template, request
from test import predict_by_name

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
        home_odds, away_odds = predict_by_name(home_team,away_team)
        form_data = {'away_team':away_team,'away_odds':away_odds,'home_team':home_team,'home_odds':home_odds}
        return render_template('result.html',form_data = form_data)

