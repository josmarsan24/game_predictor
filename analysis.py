from predict import *
import pandas as pd

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

def home_win_rate(n):
    test_games = games.sample(n)
    home_wins = 0
    for index, row in test_games.iterrows():
        if (row['away_PTS'] < row['home_PTS']):
            home_wins += 1
    return home_wins

n = 600
print("Home team win rate: ", 100*home_win_rate(n)/n, "%")
print("Total games: ", n)

