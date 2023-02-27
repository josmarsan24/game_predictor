from predict import *
import pandas as pd

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

def test():
    test_games = games.sample(n=300)
    right = 0
    wrong = 0
    really_wrong = 0
    for index, row in test_games.iterrows():
        home_name = row['Home/Neutral']
        away_name = row['Visitor/Neutral']
        if (row['away_PTS'] > row['home_PTS']):
            winner = away_name
        else:
            winner = home_name
        home, away = get_teams_by_name(home_name,away_name)
        home_odds, away_odds = predict(home,away)
        if (away_odds > home_odds and winner==away_name) or (away_odds < home_odds and winner==home_name):
            right += 1
        elif (away_odds - home_odds > 20 and winner==home_name) or (home_odds - away_odds > 20 and winner==away_name):
            wrong += 1
            really_wrong += 1
        else:
            wrong += 1
    return right, wrong, really_wrong
            
a,b,c = test()
print("GAMES PREDICTED: ", a+b)
print("RIGHT PREDICTIONS: ", a)
print("WRONG PREDICTIONS: ", b)
print("REALLY WRONG PREDICTIONS: ", c)