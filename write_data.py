import pandas as pd
import numpy as np
from predict import get_teams_by_name

try:
    games = pd.read_csv("nba_games.csv", header=0)
except:
    games = pd.read_csv("game_predictor/nba_games.csv", header=0)

try:
    wr = pd.read_csv("win_rate.csv", header=0)
    wr.set_index("team_id")
except:
    wr = pd.read_csv("game_predictor/win_rate.csv", header=0)
    wr.set_index("team_id")

def home_adv():
    df = wr
    df['home_W/L'] = 0
    df['away_W/L'] = 0
    for index, row in games.iterrows():
         if (row['away_PTS'] < row['home_PTS']):
            home_name = games['Home/Neutral'].values[index]
            df.loc[df['Row.names'] == home_name,'home_W/L'] = df.loc[df['Row.names'] == home_name,'home_W/L'] + 1
    df['home_W/L'] = (df['home_W/L'])/(df['W/L']*82)
    df['away_W/L'] = 1 - df['home_W/L']
    df.to_csv('win_rate.csv', index=False, header=True)

home_adv()