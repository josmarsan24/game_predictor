from predict import *
import pandas as pd

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

try:
    data = pd.read_csv("nba_data_norm.csv", header=0)
    wr = pd.read_csv("win_rate.csv", header=0)
    data.set_index("team_id")
except:
    data = pd.read_csv("game_predictor/nba_data_norm.csv", header=0)
    wr = pd.read_csv("game_predictor/win_rate.csv", header=0)
    data.set_index("team_id")

def home_win_rate(n):
    test_games = games.sample(n)
    home_wins = 0
    for index, row in test_games.iterrows():
        if (row['away_PTS'] < row['home_PTS']):
            home_wins += 1
    return home_wins

def stats_analysis(data,wr):
    df = data
    df['W/L'] = wr['W/L']
    ignore_cols = ['team_id','Row.names','W/L']
    print(df.head())
    print("")
    for col in df.columns:
        if col not in ignore_cols:
            df[col] = (df[col] - df['W/L']).abs()
    print(df.head())
    print("")
    print(df.mean(axis=0,numeric_only=True))

stats_analysis(data,wr)


