from predict import *
import pandas as pd

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

def test(test_games):
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

def test_adv_home_adv(test_games):
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
        home_odds, away_odds = predict_with_advanced_home_adv(home,away)
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

def test_home_adv(test_games,home_adv):
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
        home_odds, away_odds = predict_with_custom_home_adv(home,away,home_adv)
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

def test_no_fg_no_3p(test_games):
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
        home_odds, away_odds = predict_without_FG3P(home,away)
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

def print_test(desc,a,b,c,d):
    print(desc)
    print("SUCCESS RATE: ", 100*a/(a+b),"%")
    print("RIGHT PREDICTIONS: ", a)
    print("WRONG PREDICTIONS: ", b)
    print(" OF WHICH:")
    print(" MISTAKES IN ACCEPTABLE MARGAIN: ", d)
    print(" MISTAKES IN DECENT MARGAIN: ", b - (c + d))
    print(" MISTAKES IN UNACCEPTABLE MARGAIN: ", c)

test_games = games.sample(n=500)
print("GAMES PREDICTED: ", 500)

a,b,c,d = test(test_games)
print_test('USING DEFAULT FORMULA',a,b,c,d)

a,b,c,d = test_home_adv(test_games,1.1)
print_test('USING 1.1% HOME ADVANTAGE',a,b,c,d)
a,b,c,d = test_home_adv(test_games,1.05)
print_test('USING 1.05 HOME ADVANTAGE',a,b,c,d)
a,b,c,d = test_home_adv(test_games,1.075)
print_test('USING 1.075% HOME ADVANTAGE',a,b,c,d)
a,b,c,d = test_adv_home_adv(test_games)
print_test('USING ADVANCED HOME ADVANTAGE',a,b,c,d)
a,b,c,d = test_no_fg_no_3p(test_games)
print_test('IGNORING FG% AND 3P%',a,b,c,d)