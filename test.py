from predict import *
import pandas as pd

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

def test():
    test_games = games.sample(n=400)
    right = 0
    wrong = 0
    small_mistake = 0
    big_mistake = 0
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
            big_mistake += 1
        elif (away_odds - home_odds < 10 and winner==home_name) or (home_odds - away_odds < 10 and winner==away_name):
            wrong += 1
            small_mistake += 1
        else:
            wrong += 1
    return right, wrong, big_mistake, small_mistake
            
a,b,c,d = test()
print("GAMES PREDICTED: ", a+b)
print("SUCCESS RATE: ", 100*a/(a+b),"%")
print("RIGHT PREDICTIONS: ", a)
print("WRONG PREDICTIONS: ", b)
print(" OF WHICH:")
print(" MISTAKES IN ACCEPTABLE MARGAIN: ", d)
print(" MISTAKES IN DECENT MARGAIN: ", b - (c + d))
print(" MISTAKES IN UNACCEPTABLE MARGAIN: ", c)